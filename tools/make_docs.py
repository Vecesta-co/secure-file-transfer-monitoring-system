"""Generate evidence-driven diagrams, report, and editable presentation."""
from __future__ import annotations
import hashlib, json, os, re, subprocess, sys, xml.etree.ElementTree as ET, zipfile
from collections import Counter
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from PIL import Image as PILImage
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor as DocRGB
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor as SlideRGB
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches as SI, Pt as SP

ROOT=Path(__file__).resolve().parents[1]; DOCS=ROOT/"docs"; EVIDENCE=ROOT/"evidence"
NAVY="0B1220"; CARD="111B2E"; CARD2="16233B"; BORDER="24324D"; WHITE="E8EEF7"; MUTED="9FB0C8"
CYAN="22D3EE"; TEAL="14B8A6"; INFO="60A5FA"; MEDIUM="FBBF24"; HIGH="F97316"; CRITICAL="EF4444"; SUCCESS="22C55E"
FONT="Segoe UI"; MONO="Consolas"


def read_events(path):
    out=[]
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try: out.append(json.loads(line))
            except json.JSONDecodeError: pass
    return out


def load_run(n):
    frozen=EVIDENCE/"final"/f"run{n}"
    base=frozen if frozen.exists() else ROOT
    lp=base/"logs"/"file_events.jsonl"; ap=base/"logs"/"alerts.log"
    vp=base/"verify_all.txt" if frozen.exists() else EVIDENCE/"verify_all.txt"
    events=read_events(lp); alerts=ap.read_text(encoding="utf-8").splitlines() if ap.exists() else []
    verify=vp.read_text(encoding="utf-8") if vp.exists() else ""
    return {"base":base,"events":events,"alerts":alerts,"verify":verify,
            "types":Counter(e.get("event_type","UNKNOWN") for e in events),
            "severities":Counter(e.get("severity","INFO") for e in events)}


def verify_count(text):
    m=re.search(r"Result:\s*(\d+/\d+)",text); return m.group(1)+" checks" if m else "not captured"


def counts(counter): return ", ".join(f"{k}={v}" for k,v in sorted(counter.items())) or "none"


def test_result(n):
    for path in (EVIDENCE/"final"/f"pytest_run{n}.txt",EVIDENCE/f"pytest_run{n}.txt"):
        if path.exists(): return path.read_text(encoding="utf-8",errors="replace").strip().splitlines()[-1]
    return "not captured"


def read_help():
    return subprocess.run([sys.executable,str(ROOT/"main.py"),"--help"],capture_output=True,text=True,check=True).stdout.strip()


def make_diagrams():
    plt.rcParams.update({"font.family":"DejaVu Sans","text.color":"#"+WHITE})
    fig,ax=plt.subplots(figsize=(15,6),facecolor="#"+NAVY); ax.set_facecolor("#"+NAVY); ax.set_xlim(0,15); ax.set_ylim(0,6); ax.axis("off")
    ax.text(.4,5.3,"SECURE FILE TRANSFER MONITORING  /  ARCHITECTURE",fontsize=16,weight="bold",color="#"+CYAN)
    stages=[("Configured folders","watch roots",CYAN),("watchdog observer","filesystem events",INFO),("Monitor + hash index","copy · move · integrity",TEAL),("Policy rules R0–R6","classify · authorize",MEDIUM),("JSONL + alerts","timestamped findings",HIGH),("Audit report","MD · HTML · CSV",SUCCESS)]
    xs=[.35,2.85,5.35,7.85,10.35,12.85]
    for i,(title,sub,color) in enumerate(stages):
        ax.add_patch(FancyBboxPatch((xs[i],2.25),1.8,1.55,boxstyle="round,pad=.12,rounding_size=.12",facecolor="#"+CARD,edgecolor="#"+color,linewidth=2))
        ax.text(xs[i]+.9,3.15,title,ha="center",va="center",fontsize=10.5,weight="bold")
        ax.text(xs[i]+.9,2.65,sub,ha="center",va="center",fontsize=8.3,color="#"+MUTED,wrap=True)
        if i<5: ax.add_patch(FancyArrowPatch((xs[i]+1.85,3.02),(xs[i+1]-.08,3.02),arrowstyle="-|>",mutation_scale=14,color="#"+CYAN,linewidth=1.5))
    ax.text(5.45,1.55,"policy.json",fontsize=10,family="monospace",color="#"+MUTED)
    ax.text(7.5,1.55,"baseline.json",fontsize=10,family="monospace",color="#"+MUTED)
    ax.text(9.6,1.55,"file_events.jsonl  +  alerts.log",fontsize=10,family="monospace",color="#"+MUTED)
    fig.savefig(DOCS/"architecture.png",dpi=300,bbox_inches="tight",facecolor=fig.get_facecolor()); plt.close(fig)

    fig,ax=plt.subplots(figsize=(11,11),facecolor="#"+NAVY); ax.set_facecolor("#"+NAVY); ax.set_xlim(0,12); ax.set_ylim(0,12); ax.axis("off")
    ax.text(.5,11.3,"EVENT DECISION FLOW",fontsize=16,weight="bold",color="#"+CYAN)
    def node(x,y,w,h,label,fill=CARD):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.08,rounding_size=.12",facecolor="#"+fill,edgecolor="#"+BORDER,linewidth=1.4))
        ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=10,weight="bold",wrap=True)
    def arrow(a,b,label="",color=CYAN):
        ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=13,color="#"+color,linewidth=1.35))
        if label: ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.1,label,ha="center",fontsize=9,weight="bold",color="#"+color,bbox={"facecolor":"#"+NAVY,"edgecolor":"none","pad":1})
    node(4.4,9.9,3.2,.7,"1  Monitor filesystem"); node(4.4,8.55,3.2,.85,"2  Classify path + event",CARD2)
    node(4.4,7.1,3.2,.85,"Sensitive or external?",CARD2); node(.6,5.65,3,.8,"NO  ·  log INFO",CARD2)
    node(4.4,5.55,3.2,1,"YES  ·  hash + authorization"); node(4.4,4.05,3.2,.85,"Authorized user?",CARD2)
    node(.6,2.6,3,.8,"YES  ·  log result",CARD2); node(8.4,2.6,3,.8,"NO  ·  R6 alert","301C2D")
    node(4.4,2.55,3.2,.9,"Hash match?",CARD2); node(4.4,.95,3.2,.8,"Final audit report","12302E")
    node(8.4,.95,3,.8,"NO  ·  R3 CRITICAL","301C2D")
    arrow((6,9.9),(6,9.4)); arrow((6,8.55),(6,7.95)); arrow((4.4,7.5),(3.6,6.05),"NO",INFO)
    arrow((6,7.1),(6,6.55),"YES",SUCCESS); arrow((6,5.55),(6,4.9)); arrow((4.4,4.45),(3.6,3),"YES",SUCCESS)
    arrow((7.6,4.45),(8.4,3),"NO",CRITICAL); arrow((3.6,3),(4.4,2.95)); arrow((6,2.55),(6,1.75),"YES",SUCCESS)
    arrow((7.6,3),(8.4,1.35),"NO",CRITICAL); arrow((8.4,1.35),(7.6,1.35),"LOG",CRITICAL)
    ax.text(.65,4.1,"NO branch skips hashing when no policy trigger applies.",fontsize=9,color="#"+MUTED)
    fig.savefig(DOCS/"flowchart.png",dpi=300,bbox_inches="tight",facecolor=fig.get_facecolor()); plt.close(fig)
    for name,kind in (("architecture.drawio","architecture"),("flowchart.drawio","flowchart")): write_drawio(name,kind)


def write_drawio(filename,kind):
    model=ET.Element("mxfile",{"host":"app.diagrams.net","version":"24.7.17","type":"device"})
    diagram=ET.SubElement(model,"diagram",{"id":kind,"name":kind.title()})
    graph=ET.SubElement(diagram,"mxGraphModel",{"dx":"1200","dy":"800","grid":"1","gridSize":"10","page":"1","pageScale":"1","pageWidth":"1200","pageHeight":"800"})
    root=ET.SubElement(graph,"root"); ET.SubElement(root,"mxCell",{"id":"0"}); ET.SubElement(root,"mxCell",{"id":"1","parent":"0"})
    labels=( ["Configured folders","watchdog observer","Monitor + hash index","Policy rules R0–R6","JSONL + alerts","Audit report MD / HTML / CSV"] if kind=="architecture" else
             ["Monitor filesystem","Classify event","Sensitive / external?","NO: log INFO","YES: hash + authorize","Authorized?","YES: log result","NO: R6 alert","Hash match?","YES: final report","NO: R3 alert"] )
    for i,label in enumerate(labels):
        if kind=="architecture": x,y=30+i*190,250
        else: x,y=(60 if i in (3,6) else 900 if i in (7,10) else 430),40+i*60
        cell=ET.SubElement(root,"mxCell",{"id":f"n{i}","value":label,"style":"rounded=1;whiteSpace=wrap;html=1;fillColor=#111B2E;fontColor=#E8EEF7;strokeColor=#22D3EE;","vertex":"1","parent":"1"})
        ET.SubElement(cell,"mxGeometry",{"x":str(x),"y":str(y),"width":"170" if kind=="architecture" else "220","height":"70" if kind=="architecture" else "55","as":"geometry"})
    if kind=="architecture":
        pairs=[(i-1,i,"") for i in range(1,len(labels))]
    else:
        pairs=[(0,1,""),(1,2,""),(2,3,"NO"),(2,4,"YES"),(4,5,""),(5,6,"YES"),(5,7,"NO"),(5,8,"YES"),(8,9,"YES"),(8,10,"NO"),(6,9,""),(7,9,""),(10,9,"")]
    for j,(source,target,label) in enumerate(pairs):
        edge=ET.SubElement(root,"mxCell",{"id":f"edge{j}","value":label,"style":"edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#22D3EE;fontColor=#22D3EE;","edge":"1","parent":"1","source":f"n{source}","target":f"n{target}"})
        ET.SubElement(edge,"mxGeometry",{"relative":"1","as":"geometry"})
    ET.indent(model,space="  "); (DOCS/filename).write_bytes(ET.tostring(model,encoding="utf-8",xml_declaration=True))


def set_shading(cell,fill):
    shd=OxmlElement("w:shd"); shd.set(qn("w:fill"),fill); cell._tc.get_or_add_tcPr().append(shd)


def set_margins(cell):
    mar=OxmlElement("w:tcMar")
    for k,v in (("top",100),("start",120),("bottom",100),("end",120)):
        e=OxmlElement("w:"+k); e.set(qn("w:w"),str(v)); e.set(qn("w:type"),"dxa"); mar.append(e)
    cell._tc.get_or_add_tcPr().append(mar)


def add_page_field(p):
    r=p.add_run(); begin=OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"),"begin")
    ins=OxmlElement("w:instrText"); ins.set(qn("xml:space"),"preserve"); ins.text=" PAGE "
    end=OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"),"end")
    for e in (begin,ins,end): r._r.append(e)


def setup_doc(doc):
    sec=doc.sections[0]; sec.top_margin=Inches(.72); sec.bottom_margin=Inches(.68); sec.left_margin=Inches(.78); sec.right_margin=Inches(.78)
    normal=doc.styles["Normal"]; normal.font.name=FONT; normal.font.size=Pt(10.5); normal.font.color.rgb=DocRGB(30,41,59)
    normal.paragraph_format.space_after=Pt(6); normal.paragraph_format.line_spacing=1.12
    for level,size in ((1,18),(2,14),(3,11.5)):
        st=doc.styles[f"Heading {level}"]; st.font.name=FONT; st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=DocRGB(0,0,0); st.paragraph_format.keep_with_next=True
    doc.styles["Title"].font.name=FONT; doc.styles["Title"].font.size=Pt(28); doc.styles["Title"].font.bold=True
    h=sec.header.paragraphs[0]; h.text="SECURE FILE TRANSFER MONITORING SYSTEM"; h.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    for r in h.runs: r.font.name=FONT; r.font.size=Pt(8); r.font.color.rgb=DocRGB(71,85,105)
    f=sec.footer.paragraphs[0]; f.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=f.add_run("Project report  ·  Page "); r.font.name=FONT; r.font.size=Pt(8); r.font.color.rgb=DocRGB(71,85,105); add_page_field(f)


def add_table(doc,headers,rows,widths=None):
    t=doc.add_table(rows=1,cols=len(headers)); t.style="Table Grid"; t.autofit=False
    for i,txt in enumerate(headers):
        c=t.rows[0].cells[i]; c.text=txt; set_shading(c,"17324D"); set_margins(c); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
        for p in c.paragraphs:
            for r in p.runs: r.font.name=FONT; r.font.size=Pt(9); r.font.bold=True; r.font.color.rgb=DocRGB(255,255,255)
    hdr=OxmlElement("w:tblHeader"); hdr.set(qn("w:val"),"true"); t.rows[0]._tr.get_or_add_trPr().append(hdr)
    for ri,row in enumerate(rows):
        cells=t.add_row().cells
        for i,txt in enumerate(row):
            c=cells[i]; c.text=str(txt); set_margins(c); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if ri%2: set_shading(c,"EFF4F8")
            for p in c.paragraphs:
                for r in p.runs: r.font.name=FONT; r.font.size=Pt(8.5)
    if widths:
        for row in t.rows:
            for i,w in enumerate(widths): row.cells[i].width=Inches(w)
    return t


def add_code(doc,text):
    p=doc.add_paragraph(); p.paragraph_format.left_indent=Inches(.18); p.paragraph_format.space_after=Pt(8)
    shd=OxmlElement("w:shd"); shd.set(qn("w:fill"),"EEF2F6"); p._p.get_or_add_pPr().append(shd)
    r=p.add_run(text); r.font.name=MONO; r.font.size=Pt(8.5)


def caption(doc,text):
    p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run(text); r.italic=True; r.font.name=FONT; r.font.size=Pt(9)


def add_picture(doc,path,width,text):
    if path.exists():
        p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run().add_picture(str(path),width=Inches(width)); caption(doc,text)


def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def make_docx(run1,run2):
    d=Document(); setup_doc(d)
    p=d.add_paragraph(style="Title"); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run("Secure File Transfer Monitoring System")
    p=d.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run("Project report and verification record"); r.font.size=Pt(15); r.font.color.rgb=DocRGB(35,86,120)
    p=d.add_paragraph("Blue Team  ·  Data Loss Prevention  ·  File Integrity Monitoring",style="Subtitle"); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for value in ("[Your Name]","[Company]","[Supervisor]","[Date]"):
        p=d.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run(value)
    d.add_page_break(); d.add_heading("Contents",1)
    p=d.add_paragraph(); r=p.add_run(); begin=OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"),"begin")
    ins=OxmlElement("w:instrText"); ins.set(qn("xml:space"),"preserve"); ins.text=' TOC \\o "1-3" \\h \\z \\u '
    sep=OxmlElement("w:fldChar"); sep.set(qn("w:fldCharType"),"separate"); t=OxmlElement("w:t"); t.text="Update this field in Word to populate the contents."
    end=OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"),"end")
    for x in (begin,ins,sep,t,end): r._r.append(x)
    d.add_page_break()
    def chapter(title):
        heading=d.add_heading(title,1)
        heading.paragraph_format.page_break_before=True
    d.add_heading("Abstract",1)
    d.add_paragraph(f"This report describes a local Python monitor that records file-system changes, classifies configured paths, compares SHA-256 hashes, applies rules R0–R6, and creates audit reports. The deterministic demo exercises ordinary and approved copies, simulated external destinations, file changes, deletion, and a 200-file burst. The final captured demo contains {len(run1['events'])} event rows. The tool is an audit aid: it does not block transfers or observe network protocols.")
    d.add_paragraph(f"The final automated suite reports {test_result(1)}. Two clean runs, independent hashes, sabotage checks, and the source limitations are detailed below.")

    chapter("1. Introduction and problem statement")
    d.add_paragraph("A file can leave an approved folder, change after transfer, or disappear without a single readable audit trail. Security teams need to see which file changed, where it went, when it happened, and which policy rule applies. This project demonstrates that record using local folder notifications and a small JSON policy.")
    d.add_paragraph("The monitor uses path labels to represent USB storage, cloud sync folders, and network shares. These are configured directories, not device-level or network-level detectors. The system records evidence for review; it does not prevent an operating-system action.")

    chapter("2. Objectives and learning outcomes")
    add_table(d,["Objective","Demonstration"],[["Activity logging","Timestamped JSONL records include source, destination, user, process, hashes, and policy result."],["DLP-style checks","R1/R2 mark sensitive transfers outside approved locations and into configured zones."],["Integrity","SHA-256 compares baseline and observed content; R3 flags a mismatch."],["Alerting and audit","Rules write console and log findings; reports summarize the timeline."],["Testing","Unit and watcher tests plus deterministic scenarios check behavior."]],[1.7,4.9])
    d.add_paragraph("A file-system transfer is a create, copy-like, move, delete, or modify event in a watched folder. A data-loss prevention rule applies policy to a file and its destination. A cryptographic hash is a content fingerprint: the same bytes should produce the same SHA-256 value. Monitoring records activity; auditing reviews those records to decide whether an action needs investigation.")

    chapter("3. Scope and tools")
    d.add_paragraph("The implementation uses Python, watchdog, pathlib, hashlib, argparse, JSON Lines, pytest, python-docx, python-pptx, Pillow, and matplotlib. The runtime writes local files and uses no database, web application, or external service. Demo data is synthetic and contains no real credentials or customer records.")
    d.add_paragraph("The project was exercised in Windows PowerShell from a OneDrive-synchronized folder whose path contains spaces and parentheses. Linux and macOS were not available for direct observation. Windows open/read auditing is outside the implementation.")
    add_table(d,["In scope","Out of scope"],[["Configured folder monitoring, classification, hashes, alerts, reports.","Blocking or quarantining a transfer."],["Folder paths as USB, cloud, and share examples.","Hardware-level USB detection or cloud APIs."],["Best-effort process field.","Reliable attribution when OS data is unavailable."]],[3.3,3.3])

    chapter("4. System architecture")
    d.add_paragraph("The observer forwards filesystem notifications to a worker pool. The monitor classifies the event, checks baseline state, hashes stable files, and appends a structured record. Rule findings also go to the alert log. The report builder reads the event log and writes Markdown, HTML, and CSV views.")
    add_picture(d,DOCS/"architecture.png",6.55,"Figure 1. Monitoring modules and evidence flow.")
    d.add_paragraph("The baseline maps each configured file to SHA-256, optional MD5, size, and modification time. The path index supports integrity checks; the hash index helps infer copies. A copy is inferred from notifications and matching content, not from a native copy signal supplied by watchdog.")

    chapter("5. Workflow and policy branches")
    d.add_paragraph("The monitor classifies every event. If no sensitive or external policy condition applies, it records ordinary activity. A trigger leads to hash and authorization checks. A disallowed user produces R6; a content mismatch produces R3. The event is logged on each branch so the report can preserve a complete timeline.")
    add_picture(d,DOCS/"flowchart.png",5.9,"Figure 2. Classification, authorization, and integrity decisions.")

    chapter("6. Implementation modules")
    for name,description in (("main.py","Argparse dispatch for hash, baseline, monitor, report, verify, and demo."),("hasher.py","Chunked hashes and stable-file polling."),("baseline.py","Initial hash and metadata index."),("policy.py","Path resolution, sensitive names, zones, authorization, and rules."),("handler.py","Watchdog adapter for filesystem notifications."),("monitor.py","Indexes, copy inference, rename correlation, and burst aggregation."),("logger.py","Thread-safe JSONL and alert output with optional ANSI color."),("report.py","Markdown, HTML, and CSV summaries and timelines."),("demo/run_demo.py","Nine synthetic scenarios with event checks.")):
        p=d.add_paragraph(); p.add_run(name+"  ").bold=True; p.add_run(description)

    chapter("7. Detection rules")
    add_table(d,["Rule","Condition","Severity / result"],[["R0","Routine or approved activity","INFO"],["R1","Sensitive copy or move outside approval","HIGH"],["R2","Transfer into configured USB, cloud, or share zone","MEDIUM or HIGH"],["R3","Observed SHA-256 differs from indexed content","CRITICAL"],["R4","Configured count exceeded in one time window","HIGH; one summary per window"],["R5","Sensitive file deletion","HIGH"],["R6","Sensitive event by user outside allow-list","HIGH"]],[.8,3.9,1.9])
    d.add_paragraph("Rules are additive: a sensitive USB transfer can match R1 and R2. The event row stores combined rule IDs and the strongest severity. The alert log stores a separate line for each finding.")

    chapter("8. Testing and verification")
    add_table(d,["Check","Run 1","Run 2"],[["Automated tests",test_result(1),test_result(2)],["Acceptance",verify_count(run1["verify"]),verify_count(run2["verify"])],["Event rows",str(len(run1["events"])),str(len(run2["events"]))],["Event types",counts(run1["types"]),counts(run2["types"])],["Severity totals",counts(run1["severities"]),counts(run2["severities"])]],[1.7,2.45,2.45])
    d.add_paragraph("Tests cover hash vectors, classification and authorization, integrity match/mismatch, copy inference, one alert per bulk window, report generation, watcher delivery, stable writes, event ordering, process path matching, and privacy-safe external paths. The sabotage record documents three deliberate faults and the failures they caused.")

    chapter("9. Demonstration results")
    d.add_paragraph("The nine scenarios cover normal copy, approved backup, USB copy, cloud copy, move, altered share copy, in-place tampering, sensitive deletion, and a 200-file burst. Every item is synthetic. Final logs and acceptance files are the source for the counts below.")
    add_table(d,["Measure","Run 1","Run 2"],[["Event records",str(len(run1["events"])),str(len(run2["events"]))],["Event types",counts(run1["types"]),counts(run2["types"])],["Severity",counts(run1["severities"]),counts(run2["severities"])],["Acceptance",verify_count(run1["verify"]),verify_count(run2["verify"])]],[1.3,2.65,2.65])
    for filename,caption_text in (("usb_alert.png","Figure 3. USB alert from final log."),("integrity_alert.png","Figure 4. Integrity mismatch from final log."),("bulk_alert.png","Figure 5. Aggregated 200-file alert.")):
        add_picture(d,EVIDENCE/"screenshots"/filename,6.35,caption_text)

    chapter("10. Integrity evidence")
    hashes={p.name:sha256(p) for p in sorted((EVIDENCE/"integrity").glob("*.txt"))}
    add_table(d,["File","SHA-256"],[[name,value] for name,value in hashes.items()],[2.1,4.5])
    d.add_paragraph("PowerShell Get-FileHash independently checked five files. The original and correct copy share a digest. The altered copy differs. The project verify command prints MATCH for the correct pair and MISMATCH for the altered pair.")
    add_code(d,"python main.py verify evidence/integrity/original.txt evidence/integrity/correct_copy.txt\npython main.py verify evidence/integrity/original.txt evidence/integrity/altered_copy.txt")

    chapter("11. Limitations")
    add_table(d,["Limit","Effect"],[["No enforcement","The monitor reports activity but cannot stop or reverse it."],["Folder-based zones","Zone labels depend on configured paths; there is no hardware or network inspection."],["No open/read audit","Windows notifications do not show every file access; R6 applies to observed events."],["Process field","All final demo records say unknown; psutil is not installed here."],["Platform variability","Windows was checked; other systems need their own verification."],["OneDrive sync","Sidecar and rename notifications can add noise; desktop.ini is ignored by default."]],[1.6,5.0])

    chapter("12. Future work")
    d.add_paragraph("A production extension could add Windows-specific access auditing, removable-drive identity, cloud-provider events, and SIEM forwarding. Deployment should also define log retention, access controls, alert ownership, and an incident review process. These features are outside this project and have not been tested.")

    chapter("13. Conclusion")
    d.add_paragraph("The project turns configured file-system changes into structured evidence. Hash comparisons identify changed content, policy rules mark risky paths and users, and the report ties individual events to a summary. The repeatable demo and tests show behavior within the stated path-based scope.")
    d.add_paragraph("For submission, replace the four identity placeholders, review the limits, and run the demo on the presentation computer before recording.")

    chapter("References")
    for ref in ("Python pathlib and hashlib: https://docs.python.org/3/","watchdog: https://python-watchdog.readthedocs.io/","pytest: https://docs.pytest.org/","python-docx: https://python-docx.readthedocs.io/","python-pptx: https://python-pptx.readthedocs.io/"): d.add_paragraph(ref,style="List Bullet")

    chapter("Appendix A. Policy sample")
    add_code(d,(ROOT/"config"/"policy.json").read_text(encoding="utf-8"))
    d.add_paragraph("Replace the sample folders with local paths. Keep approved destinations narrow and review the allow-list before monitoring sensitive files.")

    chapter("Appendix B. Command reference")
    add_code(d,read_help())
    add_table(d,["Command","Purpose"],[["python main.py baseline","Create a hash baseline."],["python main.py monitor","Watch configured folders until Ctrl+C."],["python main.py report","Rebuild reports from the current log."],["python main.py hash FILE","Print SHA-256 and MD5."],["python main.py verify SOURCE COPY","Compare SHA-256; mismatch exits 1."],["python main.py demo --clean --pace 3","Run the demo with recording pauses."],["python -m pytest -q","Run the automated suite."]],[3.0,3.6])

    chapter("Appendix C. Traceability and evidence")
    d.add_paragraph("See docs/TRACEABILITY_MATRIX.md for the requirement-to-test links. Each final run folder contains its console transcript, logs, reports, and acceptance result. The evidence/final directory also stores both test outputs, independent hashes, negative acceptance, sabotage checks, and the clean-clone record.")
    d.save(DOCS/"Project_Report.docx")


def color(shape,fill,stroke=None):
    shape.fill.solid(); shape.fill.fore_color.rgb=SlideRGB.from_string(fill)
    if stroke: shape.line.color.rgb=SlideRGB.from_string(stroke); shape.line.width=SP(1)
    else: shape.line.fill.background()


def run_font(run,size,color_hex=WHITE,bold=False,font=FONT):
    run.font.name=font; run.font.size=SP(size); run.font.bold=bold; run.font.color.rgb=SlideRGB.from_string(color_hex)


def text(slide,value,x,y,w,h,size=16,color_hex=WHITE,bold=False,font=FONT,align=PP_ALIGN.LEFT):
    sh=slide.shapes.add_textbox(SI(x),SI(y),SI(w),SI(h)); tf=sh.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=SI(.04); tf.margin_right=SI(.04); tf.margin_top=SI(.02); tf.margin_bottom=SI(.02); tf.vertical_anchor=MSO_ANCHOR.MIDDLE
    p=tf.paragraphs[0]; p.alignment=align; r=p.add_run(); r.text=value; run_font(r,size,color_hex,bold,font); return sh


def rect(slide,x,y,w,h,fill=CARD,stroke=BORDER,rounded=True):
    sh=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,SI(x),SI(y),SI(w),SI(h)); color(sh,fill,stroke); return sh


def base_slide(prs,title):
    s=prs.slides.add_slide(prs.slide_layouts[6]); s.background.fill.solid(); s.background.fill.fore_color.rgb=SlideRGB.from_string(NAVY)
    rect(s,.65,.48,.08,.54,CYAN,CYAN,False); text(s,title,.88,.36,11.7,.75,32,WHITE,True)
    text(s,"SECURE FILE TRANSFER MONITORING",.68,7.08,8,.23,12,MUTED)
    text(s,f"{len(prs.slides):02d}",12.05,7.04,.55,.28,12,MUTED,align=PP_ALIGN.RIGHT)
    return s


def card(slide,x,y,w,h,title,body,accent=CYAN,body_size=16):
    rect(slide,x,y,w,h,CARD,BORDER); rect(slide,x+.18,y+.18,.07,h-.36,accent,accent,False)
    text(slide,title,x+.4,y+.17,w-.6,.42,18,WHITE,True)
    text(slide,body,x+.4,y+.68,w-.65,h-.84,body_size,MUTED)


def notes(slide,value): slide.notes_slide.notes_text_frame.text=value


def make_pptx(run1,run2):
    prs=Presentation(); prs.slide_width=SI(13.333); prs.slide_height=SI(7.5)
    events=run1["events"]; types=run1["types"]; severities=run1["severities"]
    talktracks=[
      "Introduce the project as a small defensive file monitoring system. It watches folders that an administrator configures, applies path policy, compares file hashes, and records findings for later review. The demonstration uses synthetic data. Replace the four identity fields before submission. The design explains a blue team workflow rather than enforcing endpoint controls. Mention that the monitor writes local JSON Lines logs and readable reports.",
      "Explain the four examples shown here. A user might copy a sensitive file to removable storage, malware might alter a local file, a sync folder might replicate a confidential document, or a bulk transfer might move many files at once. The project models these actions with folders and dummy files. It does not inspect a physical USB device or cloud traffic. This keeps the demo honest while showing how path rules can support an audit.",
      "Walk through the five outcomes. The monitor records activity, flags movement outside approved destinations, compares SHA-256 values, writes alerts, and summarizes events. These pieces live in separate modules, which makes the behavior easier to inspect and test. The implemented label means the demo and unit suite exercise the feature. It does not mean every operating-system access mode is visible or that the tool blocks a transfer.",
      "Read the pipeline from left to right. Watchdog supplies filesystem notifications. The monitor classifies the event and checks the hash index. Policy rules decide whether the event is routine or needs attention. The logger appends structured records and alerts. The report builder produces review-friendly files. Each stage has a clear responsibility, and the logs preserve facts needed to trace a finding back to its source and destination.",
      "Describe the architecture modules and the two supporting files. The baseline stores the first-seen hash and metadata for each watched file. The policy describes watched folders, sensitive locations, approved destinations, external zones, ignored names, and thresholds. The monitor maintains indexes while it runs. Reports are generated from the event log after monitoring. The architecture is local, so it can be reviewed without an external account or database.",
      "Explain the decision branches. Every event is classified first. Ordinary events are logged as INFO. Sensitive or external activity goes through hash and authorization checks. An unauthorized user produces R6, and a content mismatch produces R3. The event is still recorded so the final report has a complete timeline. The current Windows watcher does not emit a reliable open/read event, so this branch applies to observed changes rather than every file access.",
      "Introduce the rule set. R0 records routine activity. R1 marks a sensitive transfer outside the approved destination. R2 marks a configured external zone. R3 indicates a SHA-256 mismatch. R4 summarizes a burst once in its configured time window. R5 records a sensitive deletion. R6 marks an observed sensitive event by a user outside the allow-list. One event can match more than one rule, such as R1 and R2 for a sensitive USB transfer.",
      "Show how copy inference works. The baseline index maps a hash to known paths. When a new file appears, the monitor hashes it and searches for matching content. A match suggests a copy, while a same-name mismatch can indicate altered content. This is an inference because the cross-platform notification library does not report a copy operation directly. The index should be validated against the exact filesystem and workload before operational use.",
      "Take the audience through all nine scenarios. The first two are controls: an ordinary copy and an approved sensitive backup should stay INFO. The next cases test USB, cloud, an unknown move, an altered share copy, in-place tampering, deletion, and a 200-file burst. Each case uses synthetic files. The scenario header appears before the action so the presenter can pause and explain the expected observation.",
      f"The figures on this slide come from the final captured event log. Run one contains {len(events)} records, and the editable chart groups those rows by event type. The event breakdown is {', '.join(f'{k} {v}' for k,v in sorted(types.items()))}. Severity totals are {', '.join(f'{k} {v}' for k,v in sorted(severities.items()))}. The paired run is compared in the verification evidence. The total includes one summary record for the bulk finding in addition to individual file records.",
      "The three terminal images are rendered from the final transcript and alert log. Point out that each alert has a timestamp, severity, rule identifier, message, and path context. The USB message comes from the configured zone. The integrity message comes from a mismatch. The bulk message reports the count for its configured window. These are terminal evidence images; diagrams and charts elsewhere in the deck remain editable PowerPoint objects.",
      "Compare the two digests. The original and correct copy have the same SHA-256 value, so the CLI reports MATCH. The altered copy has a different value, so the CLI reports MISMATCH. PowerShell Get-FileHash independently checked the evidence files. Hashes detect content changes; they do not prove who changed a file or whether the original content was trustworthy. The baseline and its handling need protection in a real deployment.",
      "Summarize repeatability. The automated suite runs twice, the deterministic demo runs twice, and the acceptance checker validates each captured run. Three deliberate code faults were introduced during the audit to confirm that relevant tests fail. The traceability matrix links requirements to tests and logs. These checks demonstrate repeatable behavior on this Windows machine; they do not replace a run on the eventual submission computer or production endpoint.",
      "Be direct about boundaries. The tool detects and records but does not block. External destinations are folder labels, not hardware or network identity. The current environment has no psutil, so process fields remain unknown. Windows open/read auditing is absent, and other operating systems were not tested. Future work could add native USB identification, cloud-provider events, signed log retention, or a SIEM adapter, each with its own validation plan.",
      "Close with the three main takeaways. A small local monitor can make file activity easier to review. Hash comparison provides a simple integrity check when a trusted baseline exists. A deterministic demo and an evidence trail make the implementation explainable. Invite questions about the rules, path-based limits, and tests. Before submission, update the identity placeholders, record a real desktop demonstration, review speaker notes, and export the report to PDF if needed.",
    ]

    s=base_slide(prs,"Secure File Transfer Monitoring System")
    text(s,"Blue Team  ·  Data Loss Prevention  ·  File Integrity Monitoring",.9,1.42,8,.42,18,CYAN,True)
    for i,label in enumerate(("[Your Name]","[Company]","[Supervisor]","[Date]")): text(s,label,.95,2.35+i*.43,4.6,.32,15,MUTED)
    for x,y,r,c in ((9.6,2.1,.78,CYAN),(10.9,3.05,.56,TEAL),(9.25,4.15,.44,INFO),(11.25,5,.84,SUCCESS),(8.5,3.1,.34,MEDIUM)):
        sh=s.shapes.add_shape(MSO_SHAPE.OVAL,SI(x),SI(y),SI(r),SI(r)); color(sh,CARD2,c)
    for x1,y1,x2,y2 in ((9.95,2.6,10.95,3.2),(9.3,3.35,9.45,4.2),(9.7,4.4,11.25,5.2),(11.2,3.6,11.55,5),(9.7,2.4,8.8,3.2)):
        con=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,SI(x1),SI(y1),SI(x2),SI(y2)); con.line.color.rgb=SlideRGB.from_string(BORDER); con.line.width=SP(2)
    notes(s,talktracks[0])

    s=base_slide(prs,"File movement creates audit gaps")
    for i,(title,body,c) in enumerate((("INSIDER COPY","Sensitive file moved to removable storage",HIGH),("MALWARE CHANGE","Content changes after a trusted baseline",CRITICAL),("SYNC EXPOSURE","Confidential file enters a sync folder",MEDIUM),("MASS TRANSFER","Many files arrive in one short window",INFO))): card(s,.75+(i%2)*6,1.55+(i//2)*2.25,5.55,1.85,title,body,c)
    notes(s,talktracks[1])

    s=base_slide(prs,"Five monitoring objectives")
    for i,(num,label) in enumerate((("01","Log activity"),("02","Flag movement"),("03","Check integrity"),("04","Raise alerts"),("05","Build audit reports"))):
        x=.8+(i%3)*4.12; y=1.65+(i//3)*2.15; rect(s,x,y,3.65,1.55,CARD,BORDER)
        text(s,num,x+.22,y+.22,.66,.5,22,CYAN,True,MONO); text(s,label,x+.95,y+.25,2.4,.46,18,WHITE,True)
        text(s,"IMPLEMENTED  ✓",x+.95,y+.91,2.4,.3,12,SUCCESS,True)
    notes(s,talktracks[2])

    s=base_slide(prs,"Six-step event workflow")
    for i,(num,label) in enumerate((("01","Monitor"),("02","Classify"),("03","Hash"),("04","Authorize"),("05","Log + alert"),("06","Report"))):
        x=.72+i*2.1; rect(s,x,2.4,1.65,1.45,CARD2,CYAN if i<4 else TEAL)
        text(s,num,x+.12,2.58,1.4,.35,15,CYAN,True,MONO,PP_ALIGN.CENTER); text(s,label,x+.12,3,1.4,.48,15,WHITE,True,align=PP_ALIGN.CENTER)
        if i<5:
            ar=s.shapes.add_shape(MSO_SHAPE.CHEVRON,SI(x+1.73),SI(2.86),SI(.28),SI(.43)); color(ar,CYAN)
    text(s,"One record keeps source, destination, user, process, hashes and policy result.",.95,4.6,11.4,.65,18,MUTED,align=PP_ALIGN.CENTER)
    notes(s,talktracks[3])

    s=base_slide(prs,"System architecture")
    for i,(title,sub) in enumerate((("watchdog","event source"),("monitor","classifier + index"),("policy / hasher","rules + SHA-256"),("logger","JSONL + alerts"),("report","MD / HTML / CSV"))):
        x=.78+i*2.52; rect(s,x,2.25,2,1.42,CARD2,BORDER); text(s,title,x+.1,2.5,1.8,.38,17,CYAN,True,align=PP_ALIGN.CENTER); text(s,sub,x+.08,3,1.84,.38,13,MUTED,align=PP_ALIGN.CENTER)
        if i<4: text(s,"›",x+2.07,2.63,.35,.52,28,TEAL,True,align=PP_ALIGN.CENTER)
    rect(s,2.15,4.5,3.55,.8,CARD,BORDER); text(s,"policy.json",2.3,4.68,3.25,.34,15,WHITE,True,MONO,PP_ALIGN.CENTER)
    rect(s,7.6,4.5,3.55,.8,CARD,BORDER); text(s,"baseline.json",7.75,4.68,3.25,.34,15,WHITE,True,MONO,PP_ALIGN.CENTER)
    notes(s,talktracks[4])

    s=base_slide(prs,"Policy and integrity branches")
    rect(s,4.85,1.45,3.6,.62,CARD2,CYAN); text(s,"Classify event",5,1.55,3.3,.38,16,WHITE,True,align=PP_ALIGN.CENTER)
    dia=s.shapes.add_shape(MSO_SHAPE.DIAMOND,SI(5.05),SI(2.45),SI(3.2),SI(1.05)); color(dia,CARD2,CYAN); text(s,"Sensitive / external?",5.45,2.75,2.4,.38,14,WHITE,True,align=PP_ALIGN.CENTER)
    card(s,.95,2.7,3,1.05,"NO","Log INFO",INFO,14); card(s,8.95,2.7,3.25,1.05,"YES","Hash and check user",SUCCESS,14)
    text(s,"YES",4.15,2.75,.72,.3,12,SUCCESS,True,align=PP_ALIGN.CENTER); text(s,"NO",8.18,2.75,.58,.3,12,INFO,True,align=PP_ALIGN.CENTER)
    for kind,x,y,w,h,c in ((MSO_SHAPE.LEFT_ARROW,4.03,2.98,.72,.24,INFO),(MSO_SHAPE.RIGHT_ARROW,8.32,2.98,.55,.24,SUCCESS),(MSO_SHAPE.DOWN_ARROW,6.47,3.55,.3,.38,CYAN)):
        sh=s.shapes.add_shape(kind,SI(x),SI(y),SI(w),SI(h)); color(sh,c)
    text(s,"Authorized?",5.45,4.05,2.4,.42,18,WHITE,True,align=PP_ALIGN.CENTER)
    card(s,.95,4.85,3,.92,"YES","Continue + log",SUCCESS,14); card(s,4.85,4.85,3.2,.92,"HASH MATCH","R0 or transfer rules",CYAN,14)
    card(s,8.95,4.85,3.25,.92,"NO","R6 alert",CRITICAL,14)
    for kind,x,y,w,h,c in ((MSO_SHAPE.LEFT_ARROW,4.03,5.18,.72,.24,SUCCESS),(MSO_SHAPE.RIGHT_ARROW,8.32,5.18,.55,.24,CRITICAL),(MSO_SHAPE.DOWN_ARROW,6.47,4.5,.3,.32,CYAN)):
        sh=s.shapes.add_shape(kind,SI(x),SI(y),SI(w),SI(h)); color(sh,c)
    text(s,"Hash mismatch → R3 CRITICAL",4.65,6.12,4,.36,14,CRITICAL,True,align=PP_ALIGN.CENTER)
    notes(s,talktracks[5])

    s=base_slide(prs,"Detection rules R0–R6")
    rules=(("R0","Routine activity",INFO),("R1","Sensitive path outside approval",HIGH),("R2","USB / cloud / share zone",MEDIUM),("R3","SHA-256 mismatch",CRITICAL),("R4","Bulk window exceeded",HIGH),("R5","Sensitive deletion",HIGH),("R6","User outside allow-list",HIGH))
    for i,(rid,body,c) in enumerate(rules):
        x=.78+(i%2)*6.25; y=1.35+(i//2)*1.32; rect(s,x,y,5.7,1,CARD,BORDER); rect(s,x+.2,y+.21,.78,.55,c,c)
        text(s,rid,x+.25,y+.25,.68,.35,15,NAVY,True,MONO,PP_ALIGN.CENTER); text(s,body,x+1.18,y+.21,4.25,.55,15,WHITE)
    notes(s,talktracks[6])

    s=base_slide(prs,"Copy detection uses the hash index")
    card(s,.85,2,3.15,2,"BASELINE INDEX","SHA-256 → known path",CYAN); card(s,5.1,2,3.15,2,"NEW FILE","Hash the observed content",TEAL); card(s,9.35,2,3.15,2,"MATCH FOUND","Infer COPY of source",SUCCESS)
    for x in (4.25,8.5):
        ar=s.shapes.add_shape(MSO_SHAPE.CHEVRON,SI(x),SI(2.75),SI(.48),SI(.56)); color(ar,CYAN)
    text(s,"The event API reports changes; matching content helps infer the operation.",1.15,4.8,11,.5,17,MUTED,align=PP_ALIGN.CENTER)
    notes(s,talktracks[7])

    s=base_slide(prs,"Nine synthetic scenarios")
    scenarios=(("1","Copy R0"),("2","Backup R0"),("3","USB R1/R2"),("4","Cloud R1/R2"),("5","Move R1"),("6","Share R3"),("7","Tamper R3"),("8","Delete R5"),("9","Bulk 200 R4"))
    for i,(num,label) in enumerate(scenarios):
        x=.8+(i%3)*4.1; y=1.3+(i//3)*1.62; rect(s,x,y,3.55,1,CARD,BORDER); text(s,num,x+.18,y+.21,.5,.5,20,CYAN,True,MONO); text(s,label,x+.78,y+.2,2.55,.58,15,WHITE,True)
    notes(s,talktracks[8])

    s=base_slide(prs,"Final run results")
    card(s,.75,1.2,2.8,1.05,"EVENT ROWS",str(len(events)),CYAN,20); card(s,3.78,1.2,2.8,1.05,"RULE ALERTS",str(len(run1["alerts"])),HIGH,20)
    card(s,6.8,1.2,2.8,1.05,"CHECKS",verify_count(run1["verify"]).replace(" checks",""),SUCCESS,20)
    testmatch=re.search(r"(\d+) passed",test_result(1)); card(s,9.82,1.2,2.8,1.05,"TESTS",testmatch.group(1) if testmatch else "?",INFO,20)
    data=CategoryChartData(); labels=list(sorted(types)); data.categories=labels; data.add_series("Event rows",[types[k] for k in labels])
    chart=s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED,SI(2),SI(2.65),SI(9.2),SI(3.65),data).chart; chart.has_legend=False; chart.has_title=False
    chart.category_axis.tick_labels.font.name=FONT; chart.category_axis.tick_labels.font.size=SP(13); chart.category_axis.tick_labels.font.color.rgb=SlideRGB.from_string(WHITE)
    chart.value_axis.tick_labels.font.name=FONT; chart.value_axis.tick_labels.font.size=SP(12); chart.value_axis.tick_labels.font.color.rgb=SlideRGB.from_string(MUTED)
    chart.value_axis.has_major_gridlines=True; chart.value_axis.major_gridlines.format.line.color.rgb=SlideRGB.from_string(BORDER)
    plot=chart.plots[0]; plot.has_data_labels=True; plot.data_labels.font.name=FONT; plot.data_labels.font.size=SP(12); plot.data_labels.font.color.rgb=SlideRGB.from_string(WHITE)
    notes(s,talktracks[9])

    s=base_slide(prs,"Required alerts in the terminal")
    for i,(file,label) in enumerate((("usb_alert.png","USB transfer"),("integrity_alert.png","Integrity mismatch"),("bulk_alert.png","Bulk transfer"))):
        x=.82; y=1.35+i*1.72; rect(s,x,y,11.7,1.5,CARD2,BORDER)
        for j,c in enumerate((CRITICAL,MEDIUM,SUCCESS)):
            dot=s.shapes.add_shape(MSO_SHAPE.OVAL,SI(x+.18+j*.2),SI(y+.14),SI(.12),SI(.12)); color(dot,c)
        text(s,label,x+.9,y+.12,2.1,.32,14,CYAN,True)
        img=EVIDENCE/"screenshots"/file
        if img.exists():
            with PILImage.open(img) as im: ratio=im.height/im.width
            width=10.8; height=min(.92,width*ratio)
            pic=s.shapes.add_picture(str(img),SI(x+.2),SI(y+.48),width=SI(width),height=SI(height))
            pic._element.nvPicPr.cNvPr.set("descr",label+" captured terminal transcript")
    notes(s,talktracks[10])

    s=base_slide(prs,"Integrity evidence: MATCH and MISMATCH")
    hf={p.name:sha256(p) for p in sorted((EVIDENCE/"integrity").glob("*.txt"))}; good=hf.get("original.txt","0"*64); altered=hf.get("altered_copy.txt","0"*64)
    card(s,.8,1.6,5.8,3.6,"MATCH  ·  original / correct copy",good+"\n"+hf.get("correct_copy.txt","0"*64),SUCCESS,14)
    card(s,6.9,1.6,5.6,3.6,"MISMATCH  ·  altered copy",altered,CRITICAL,14)
    text(s,"Independent check: PowerShell Get-FileHash -Algorithm SHA256",2.1,5.75,9.2,.4,14,MUTED,False,MONO,PP_ALIGN.CENTER)
    notes(s,talktracks[11])

    s=base_slide(prs,"Verification is repeatable")
    card(s,.85,1.55,3.65,1.55,"PYTEST × 2",test_result(1)+"\n"+test_result(2),INFO,14)
    card(s,4.85,1.55,3.65,1.55,"DEMO × 2",f"{len(run1['events'])} / {len(run2['events'])} event rows",CYAN,16)
    card(s,8.85,1.55,3.65,1.55,"ACCEPTANCE",verify_count(run1["verify"]),SUCCESS,16)
    text(s,"Three sabotage checks  ·  independent hashes  ·  clean clone",1,4.2,11.2,.55,18,MUTED,True,align=PP_ALIGN.CENTER)
    text(s,"Requirement-to-test links: docs/TRACEABILITY_MATRIX.md",1,5,11.2,.44,14,CYAN,False,MONO,PP_ALIGN.CENTER)
    notes(s,talktracks[12])

    s=base_slide(prs,"Current limits and possible extensions")
    card(s,.8,1.55,5.75,3.7,"CURRENT LIMITS","No blocking\nZones use paths\nUnknown process\nNo file-read audit",MEDIUM,15)
    card(s,6.8,1.55,5.75,3.7,"FUTURE WORK","USB identity\nCloud event feeds\nSIEM + signed logs\nVerify Linux / macOS",TEAL,15)
    notes(s,talktracks[13])

    s=base_slide(prs,"Conclusion and questions")
    for i,(title,body) in enumerate((("ACTIVITY","A clear local event record"),("INTEGRITY","SHA-256 detects content changes"),("EVIDENCE","Tests connect rules to results"))): card(s,.85+i*4.12,2,3.6,1.75,title,body,(CYAN,TEAL,SUCCESS)[i],16)
    text(s,"Questions?",4.25,5,4.8,.7,30,CYAN,True,align=PP_ALIGN.CENTER); notes(s,talktracks[14])
    prs.save(DOCS/"Final_Presentation.pptx")
    fix_chart_axis_ids(DOCS/"Final_Presentation.pptx")
    validate_pptx(DOCS/"Final_Presentation.pptx")


def fix_chart_axis_ids(path):
    """Normalize signed python-pptx axis IDs for strict OOXML renderers."""
    temp=path.with_suffix(".normalized.pptx")
    with zipfile.ZipFile(path,"r") as source, zipfile.ZipFile(temp,"w",zipfile.ZIP_DEFLATED) as target:
        for info in source.infolist():
            data=source.read(info.filename)
            if info.filename.startswith("ppt/charts/chart") and info.filename.endswith(".xml"):
                root=ET.fromstring(data); mapping={}
                for element in root.iter():
                    if element.tag.endswith("axId") or element.tag.endswith("crossAx"):
                        old=element.get("val")
                        if old is not None:
                            if old not in mapping: mapping[old]=str(10000+len(mapping))
                            element.set("val",mapping[old])
                data=ET.tostring(root,encoding="utf-8",xml_declaration=True)
            target.writestr(info,data)
    os.replace(temp,path)


def validate_pptx(path):
    p=Presentation(path); assert len(p.slides)==15
    assert all(s.has_notes_slide and 60<=len(s.notes_slide.notes_text_frame.text.split())<=120 for s in p.slides)
    assert any(sh.has_chart for s in p.slides for sh in s.shapes)
    assert all(sh.left>=0 and sh.top>=0 and sh.left+sh.width<=p.slide_width and sh.top+sh.height<=p.slide_height for s in p.slides for sh in s.shapes)
    for i,s in enumerate(p.slides,1):
        body=[sh for sh in s.shapes if sh.has_text_frame and SI(1.1)<sh.top<SI(6.8) and sh.height>SI(.25)]
        assert len(" ".join(sh.text for sh in body).split())<=35, f"slide {i} too wordy"
        for sh in s.shapes:
            if sh.has_text_frame:
                for para in sh.text_frame.paragraphs:
                    for r in para.runs:
                        if r.font.size: assert r.font.size.pt>=12,(r.text,r.font.size.pt)


def write_traceability(run):
    rows=[("REQ-1 Event logging","watchdog + JSONL","test_watchdog_end_to_end_with_polling","logs/file_events.jsonl"),("REQ-2 Movement policy","Policy zones R1/R2/R5/R6","test_policy_rules_integrity_and_access","logs/alerts.log"),("REQ-3 Integrity","SHA-256 baseline and comparisons","test_hash_known_vector; test_copy_detection_and_integrity_mismatch","evidence/integrity/"),("REQ-4 Alerts","console and alert log","scenario acceptance checks","logs/alerts.log"),("REQ-5 Reports","Markdown, HTML, CSV","test_report_generation","reports/"),("REQ-6 Required messages","nine scenarios","tools/verify_all.py","console_transcript.txt"),("REQ-7 Workflow","monitor → classify → hash → authorize → log → report","tests/test_core.py","reports/audit_report.md"),("REQ-8 Deliverables","DOCX, PPTX, diagrams, evidence","structural and visual checks","docs/ and evidence/final/"),("REQ-9 Learning outcomes","walkthrough and report","manual review","docs/CODE_WALKTHROUGH.md")]
    lines=["# Traceability matrix","","All counts and evidence references derive from the final captured run.","","| Requirement | Feature | Test / check | Evidence |","|---|---|---|---|"]
    for req,feat,test,proof in rows: lines.append(f"| {req} | {feat} | `{test}` | `evidence/final/run1/{proof}` |")
    lines += ["",f"Run 1: {len(run['events'])} rows; events {counts(run['types'])}; severity {counts(run['severities'])}.",f"Acceptance: {verify_count(run['verify'])}."]
    (DOCS/"TRACEABILITY_MATRIX.md").write_text("\n".join(lines)+"\n",encoding="utf-8")


def write_double_check(run1,run2):
    same=run1["types"]==run2["types"] and run1["severities"]==run2["severities"] and len(run1["events"])==len(run2["events"])
    lines=["# Double-run verification summary","",f"- Run 1 rows: {len(run1['events'])}.",f"- Run 2 rows: {len(run2['events'])}.",f"- Run 1 event types: {counts(run1['types'])}.",f"- Run 2 event types: {counts(run2['types'])}.",f"- Run 1 severity: {counts(run1['severities'])}.",f"- Run 2 severity: {counts(run2['severities'])}.",f"- Event and severity totals match: {'yes' if same else 'no'}.",f"- Run 1 acceptance: {verify_count(run1['verify'])}.",f"- Run 2 acceptance: {verify_count(run2['verify'])}.","","| Run | Rule IDs | Alert messages |","|---|---|---|"]
    for i,run in ((1,run1),(2,run2)):
        ids=sorted(set(re.findall(r"\] (R\d+):","\n".join(run["alerts"]))))
        msgs=sorted(set(re.findall(r"\] R\d+: (.*?) \|","\n".join(run["alerts"]))))
        lines.append(f"| {i} | {', '.join(ids)} | {'; '.join(msgs)} |")
    (EVIDENCE/"final"/"double_check_summary.md").write_text("\n".join(lines)+"\n",encoding="utf-8")


def write_readme(run):
    text=f'''# Secure File Transfer Monitoring System

A local defensive monitor that records configured file activity, checks sensitive-file movement and SHA-256 integrity, and writes reviewable audit reports. The synthetic demo uses dummy files and makes no network calls.

## Features

- Recursive folder monitoring with watchdog.
- JSONL activity, human-readable alerts, and Markdown / HTML / CSV reports.
- Path-based sensitive, approved, USB, cloud, and network-share zones.
- SHA-256 checks, copy inference, user allow-list, and bulk-window alerting.
- Nine repeatable scenarios and automated acceptance checks.

## Architecture

![Architecture diagram](docs/architecture.png)

## Quick start

```powershell
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
python -m pip install -r requirements.txt
```

Run the demo, tests, and report:

```powershell
python main.py demo --clean
python -m pytest -q
python main.py report
```

## Demo evidence

The latest frozen demo contains **{len(run['events'])} event rows** ({counts(run['types'])}) and passed **{verify_count(run['verify'])}**. Numbers are generated from the captured event log.

![USB alert](evidence/screenshots/usb_alert.png)

![Integrity alert](evidence/screenshots/integrity_alert.png)

![Bulk transfer alert](evidence/screenshots/bulk_alert.png)

## Commands

| Command | Purpose |
|---|---|
| `python main.py baseline [--policy FILE]` | Build the hash baseline. |
| `python main.py monitor [--policy FILE]` | Watch configured folders until Ctrl+C. |
| `python main.py report [--policy FILE]` | Regenerate reports from the current log. |
| `python main.py hash FILE` | Print SHA-256 and MD5. |
| `python main.py verify SOURCE COPY` | Compare SHA-256; mismatch returns exit code 1. |
| `python main.py demo --clean --pace 3` | Run all cases with three seconds between scenario starts. |
| `python main.py demo --clean --no-color` | Run without ANSI color. |
| `python -m pytest -q` | Run automated tests. |
| `python tools/verify_all.py` | Check scenarios and acceptance output. |

## Configure real folders

Edit `config/policy.json` or pass a separate policy with `--policy`. Set watched and sensitive locations, approved backup folders, and external zones for a USB drive letter, OneDrive/Dropbox folder, or network share. Review `authorized_users` and `ignore_patterns`. The example policy uses placeholder paths; replace them before use. Do not point the demo at real sensitive files.

Example alert:

```text
[HIGH] R2: Sensitive file copied to USB drive
```

## Limitations

This tool detects and records activity; it does not block transfers. External zones are configured paths, not hardware identity or network inspection. Windows open/read auditing is not implemented. Process fields remain `unknown` here because psutil is unavailable. Filesystem notifications vary by platform and sync software. Windows was checked; test other systems before relying on them.

## Project structure

```text
main.py                 command-line entry point
config/                 active and example policies
src/ftmon/              hashing, monitoring, policy, logs and reports
demo/run_demo.py        synthetic nine-scenario demonstration
tests/                  unit and watcher checks
tools/                  acceptance and artifact generation
docs/                   report, presentation, diagrams, and guides
evidence/final/          frozen runs and verification
```

## License

MIT. See [LICENSE](LICENSE).
'''
    (ROOT/"README.md").write_text(text,encoding="utf-8")


def write_screenshot_inputs(run):
    out=EVIDENCE/"screenshots"; out.mkdir(parents=True,exist_ok=True)
    groups={"usb_alert.txt":[x for x in run["alerts"] if "Sensitive file copied to USB drive" in x],"integrity_alert.txt":[x for x in run["alerts"] if "Integrity Failure: File hash mismatch detected" in x],"bulk_alert.txt":[x for x in run["alerts"] if "Suspicious movement: 200 files transferred to unknown directory" in x]}
    for name,lines in groups.items(): (out/name).write_text("SECURE FILE TRANSFER MONITORING SYSTEM\n"+"\n".join(lines)+"\n",encoding="utf-8")


def main():
    DOCS.mkdir(exist_ok=True); (EVIDENCE/"final").mkdir(parents=True,exist_ok=True)
    r1,r2=load_run(1),load_run(2)
    if not r1["events"] or not r2["events"]: raise SystemExit("Final evidence run1/run2 logs are required before generation")
    make_diagrams(); write_screenshot_inputs(r1); write_traceability(r1); write_double_check(r1,r2)
    make_docx(r1,r2); make_pptx(r1,r2); write_readme(r1)
    d=Document(DOCS/"Project_Report.docx"); p=Presentation(DOCS/"Final_Presentation.pptx")
    print(f"Generated 300-dpi diagrams, {len(d.paragraphs)} DOCX paragraphs, {len(d.tables)} tables, {len(p.slides)} slides.")


if __name__=="__main__": main()
