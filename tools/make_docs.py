"""Generate project diagrams, the internship report, and the slide deck."""
from __future__ import annotations
import json
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image as PILImage
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from pptx import Presentation
from pptx.dml.color import RGBColor as SlideRGB
from pptx.util import Inches as SlideInches, Pt as SlidePt

ROOT = Path(__file__).resolve().parents[1]
DOCS, EVIDENCE = ROOT / "docs", ROOT / "evidence"


def _box(ax, x, y, w, h, text, color="#e9f1f8", edge="#315878", size=10):
    patch = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor=color, edgecolor=edge, linewidth=1.5)
    ax.add_patch(patch); ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=size, wrap=True, color="#15283b")


def _arrow(ax, a, b, label=""):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=13, linewidth=1.2, color="#556a7e", connectionstyle="arc3,rad=0"))
    if label: ax.text((a[0]+b[0])/2, (a[1]+b[1])/2+0.08, label, ha="center", fontsize=8, color="#425466")


def make_diagrams():
    fig, ax = plt.subplots(figsize=(12, 4.5)); ax.set_xlim(0, 12); ax.set_ylim(0, 4.5); ax.axis("off")
    items = [(0.3,"Configured\nfolders"),(2.0,"watchdog\nobserver"),(3.9,"Event classifier\nand hash index"),(6.2,"Policy rules\nR0–R6"),(8.4,"JSONL events\nand alerts"),(10.4,"Audit reports\nMD / HTML / CSV")]
    for x, label in items: _box(ax,x,1.6,1.45,1.1,label)
    for i in range(len(items)-1): _arrow(ax,(items[i][0]+1.45,2.15),(items[i+1][0],2.15))
    ax.set_title("Secure File Transfer Monitor — Architecture", fontsize=16, weight="bold", pad=14)
    fig.savefig(DOCS / "architecture.png", dpi=180, bbox_inches="tight"); plt.close(fig)

    fig, ax = plt.subplots(figsize=(12, 8)); ax.set_xlim(0,12); ax.set_ylim(0,10); ax.axis("off")
    nodes = {
      "monitor": (4.7,8.8,2.3,.65,"Monitor filesystem"),
      "question": (4.55,7.4,2.6,.72,"Sensitive or\nexternal?","#fff1cc"),
      "info": (.5,6.1,2.5,.7,"No: log INFO"),
      "check": (4.55,6.05,2.6,.8,"Yes: hash +\nauthorization check"),
      "auth": (4.55,4.6,2.6,.7,"Authorized?","#fff1cc"),
      "ok": (.5,3.3,2.5,.7,"Yes: log OK"),
      "alert": (8.8,3.3,2.7,.7,"No: alert + log","#ffe3e0"),
      "integrity": (4.55,2.0,2.6,.75,"Integrity match?","#fff1cc"),
      "mismatch": (8.8,.7,2.7,.7,"No: integrity alert","#ffe3e0"),
      "report": (4.55,.65,2.6,.75,"Final audit report","#dff3e5")
    }
    for name, data in nodes.items(): _box(ax,*data[:4],data[4],data[5] if len(data)>5 else "#e9f1f8",size=9)
    _arrow(ax,(5.85,8.8),(5.85,8.12)); _arrow(ax,(4.55,7.75),(3.0,6.45),"No"); _arrow(ax,(5.85,7.4),(5.85,6.85),"Yes")
    _arrow(ax,(5.85,6.05),(5.85,5.3)); _arrow(ax,(4.55,4.95),(3.0,3.65),"Yes"); _arrow(ax,(7.15,4.95),(8.8,3.65),"No")
    _arrow(ax,(3.0,3.65),(4.55,2.38)); _arrow(ax,(8.8,3.65),(7.15,2.38)); _arrow(ax,(7.15,2.38),(8.8,1.05),"No")
    _arrow(ax,(5.85,2.0),(5.85,1.4),"Yes"); _arrow(ax,(8.8,1.05),(7.15,1.02))
    # The non-sensitive path reaches the same final report around the left edge.
    ax.plot([.5,.2,.2],[6.45,6.45,1.02],color="#556a7e",linewidth=1.2)
    _arrow(ax,(.2,1.02),(4.55,1.02)); ax.text(.25,3.8,"INFO path",rotation=90,fontsize=8,color="#425466",ha="left")
    ax.set_title("Event handling and decision flow", fontsize=16, weight="bold", pad=12)
    fig.savefig(DOCS / "flowchart.png", dpi=180, bbox_inches="tight"); plt.close(fig)


def _load_events():
    path = ROOT / "logs" / "file_events.jsonl"
    if not path.exists(): return []
    out=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        try: out.append(json.loads(line))
        except json.JSONDecodeError: pass
    return out


def _add_fit_image(slide, image, left, top, max_width, max_height):
    """Place a slide image inside a box without distorting its aspect ratio."""
    with PILImage.open(image) as source:
        ratio = source.width / source.height
    width = min(max_width, max_height * ratio)
    height = width / ratio
    x = left + (max_width - width) / 2
    y = top + (max_height - height) / 2
    slide.shapes.add_picture(str(image), x, y, width=width, height=height)


def make_docx(events):
    doc = Document(); sec=doc.sections[0]; sec.top_margin=Inches(.7); sec.bottom_margin=Inches(.7)
    normal=doc.styles["Normal"]; normal.font.name="Arial"; normal.font.size=Pt(10)
    normal.font.color.rgb=RGBColor(35,48,62)
    title_style=doc.styles["Title"]; title_style.font.name="Arial"; title_style.font.size=Pt(26); title_style.font.bold=True; title_style.font.color.rgb=RGBColor(0,0,0)
    for level in range(1,4):
        style=doc.styles[f"Heading {level}"]; style.font.name="Arial"; style.font.color.rgb=RGBColor(0,0,0)
    p=doc.add_paragraph(style="Title"); p.alignment=1; p.add_run("Secure File Transfer Monitoring System Project Report")
    p=doc.add_paragraph("Internship Project Report"); p.alignment=1; p.runs[0].font.size=Pt(16); p.runs[0].font.color.rgb=RGBColor(0,0,0)
    for value in ["[Your Name]", "[Company]", "[Supervisor]", "[Date]"]:
        p=doc.add_paragraph(value); p.alignment=1
    doc.add_page_break()
    def heading(text, level=1): doc.add_heading(text, level=level)
    heading("Abstract")
    doc.add_paragraph("This project implements a defensive Python utility that monitors configured folders, records file activity, applies path and user policy, compares file hashes, and produces audit reports. A deterministic synthetic demo exercises ordinary transfers, approved backup, USB and cloud movement, tampering, deletion, and bulk activity.")
    heading("1. Introduction and problem statement")
    doc.add_paragraph("Sensitive information can be copied, moved, changed, or removed without a clear audit trail. The system provides a local file-event record and rule-based alerts to make those actions easier to review. It does not inspect network traffic or enforce operating-system access controls.")
    heading("2. Objectives")
    for x in ["Log file creation, copy-like, move, delete, and modify activity.","Detect sensitive-file movement to unapproved and configured external folders.","Compare SHA-256 hashes to identify content changes.","Raise readable alerts and generate an audit report.","Verify the design using tests and repeatable synthetic scenarios."]: doc.add_paragraph(x,style="List Bullet")
    heading("3. Scope and tools")
    doc.add_paragraph("Python 3.10+, watchdog, pathlib, hashlib, argparse, JSON Lines, pytest, python-docx, python-pptx, Pillow, and matplotlib. The runtime uses no database, web service, or network connection. The demo touches only dummy text files inside the project.")
    heading("4. System architecture and workflow")
    doc.add_picture(str(DOCS/"architecture.png"),width=Inches(6.7)); doc.add_picture(str(DOCS/"flowchart.png"),width=Inches(6.5))
    heading("5. Implementation")
    for module, description in [("main.py","CLI dispatch for baseline, monitor, report, hashing, verification, and demo."),("hasher.py","Chunked SHA-256/MD5 hashing and stable-file retries."),("baseline.py","Initial per-file hash and filesystem metadata index."),("policy.py","Path resolution, sensitivity and zone classification, authorization, and rules."),("logger.py","Thread-safe JSONL and alert log writers."),("handler.py","Small watchdog adapter that sends changes to the monitor worker pool."),("monitor.py","Copy/move inference, integrity comparisons, and bulk aggregation."),("report.py","Markdown, HTML, and CSV audit report generation."),("demo/run_demo.py","Nine synthetic filesystem scenarios with polling-based event confirmation.")]:
        p=doc.add_paragraph(); p.add_run(module+" — ").bold=True; p.add_run(description)
    heading("6. Detection rules")
    table=doc.add_table(rows=1,cols=3); table.style="Light Shading Accent 1"
    for c,v in zip(table.rows[0].cells,["Rule","Condition","Severity"]): c.text=v
    for row in [("R1","Sensitive copy/move outside approved path","HIGH"),("R2","Transfer into USB/cloud/share zone","MEDIUM or HIGH"),("R3","Hash mismatch or changed file","CRITICAL"),("R4","More than threshold transfers in a time window","HIGH"),("R5","Sensitive-file deletion","HIGH"),("R6","Sensitive access by a non-authorized user","HIGH"),("R0","No violation found","INFO")]:
        cells=table.add_row().cells
        for c,v in zip(cells,row): c.text=v
    heading("7. Testing and observed results")
    counts={};
    for e in events: counts[e.get("event_type","UNKNOWN")]=counts.get(e.get("event_type","UNKNOWN"),0)+1
    alerts=ROOT/"logs"/"alerts.log"; alert_lines=alerts.read_text(encoding="utf-8").splitlines() if alerts.exists() else []
    doc.add_paragraph(f"Observed latest clean run: {len(events)} event records and {len(alert_lines)} alert lines. Event totals: " + ", ".join(f"{k}={v}" for k,v in sorted(counts.items())) + ". See evidence/run1 and evidence/run2 for transcripts and copied outputs.")
    for name in ["demo_start.png","usb_alert.png","integrity_alert.png","bulk_alert.png","pytest_result.png"]:
        image=EVIDENCE/"screenshots"/name
        if image.exists(): doc.add_picture(str(image),width=Inches(6.2))
    heading("8. Integrity evidence")
    doc.add_paragraph("The evidence folder includes a correct copy and an altered copy checked through the CLI. MATCH means both SHA-256 values are identical; MISMATCH means the content changed. All evidence files are synthetic.")
    heading("9. Limitations and future work")
    doc.add_paragraph("Filesystem notification behavior differs across operating systems; copy detection is inferred from hashes and moves may arrive as paired notifications. USB/cloud/share zones require explicit configured paths. Process attribution is best-effort. The Windows build does not record open/read access, and this session did not verify macOS or Linux. Future work could add platform-specific access auditing, retention controls, and signed reports.")
    heading("10. Conclusion")
    doc.add_paragraph("The project demonstrates a small, explainable pipeline from filesystem notification to policy evaluation, hash comparison, alert logging, and report generation. The synthetic scenarios and tests provide repeatable evidence for the stated scope.")
    heading("References")
    for ref in ["Python documentation — pathlib, hashlib, argparse: https://docs.python.org/3/","watchdog documentation: https://python-watchdog.readthedocs.io/","pytest documentation: https://docs.pytest.org/"]: doc.add_paragraph(ref,style="List Bullet")
    doc.save(DOCS/"Project_Report.docx")


def make_pptx(events):
    prs=Presentation(); prs.slide_width=SlideInches(13.333); prs.slide_height=SlideInches(7.5)
    def slide(title, bullets=None, image=None, sub=None):
        s=prs.slides.add_slide(prs.slide_layouts[6]); s.background.fill.solid(); s.background.fill.fore_color.rgb=SlideRGB(248,250,252)
        band=s.shapes.add_shape(1,0,0,prs.slide_width,SlideInches(.9)); band.fill.solid(); band.fill.fore_color.rgb=SlideRGB(25,57,84); band.line.fill.background()
        tf=band.text_frame; tf.text=title; p=tf.paragraphs[0]; p.font.size=SlidePt(32); p.font.bold=True; p.font.color.rgb=SlideRGB(255,255,255)
        if sub:
            box=s.shapes.add_textbox(SlideInches(.7),SlideInches(1.15),SlideInches(11.8),SlideInches(.5)); box.text_frame.text=sub; box.text_frame.paragraphs[0].font.size=SlidePt(15)
        if bullets:
            both = bool(image and image.exists())
            box=s.shapes.add_textbox(SlideInches(.8),SlideInches(1.65 if sub else 1.35),SlideInches(5.2 if both else 11.6),SlideInches(5.4)); tf=box.text_frame; tf.word_wrap=True
            for i,item in enumerate(bullets):
                p=tf.paragraphs[0] if i==0 else tf.add_paragraph(); p.text=item; p.level=0; p.font.size=SlidePt(21); p.space_after=SlidePt(18); p.font.color.rgb=SlideRGB(35,48,62)
        if image and image.exists():
            if bullets: _add_fit_image(s,image,SlideInches(6.25),SlideInches(1.45),SlideInches(6.45),SlideInches(5.35))
            else: _add_fit_image(s,image,SlideInches(.65),SlideInches(1.4),SlideInches(12.0),SlideInches(5.6))
        return s
    screen=EVIDENCE/"screenshots"
    slide("Secure File Transfer Monitoring System",["Defensive file activity monitoring","Internship Project — [Your Name]","[Company] · [Supervisor] · [Date]"])
    slide("Problem",["File movement can be hard to audit across local folders.","Sensitive files need clear path policy and integrity checks.","This project creates readable local evidence for review."])
    slide("Objectives",["Log create, copy-like, move, delete, and modify events.","Alert on sensitive and external-zone movement.","Compare hashes and report audit results."])
    slide("Architecture",image=DOCS/"architecture.png")
    slide("Workflow",image=DOCS/"flowchart.png")
    slide("Detection rules",["R1/R2: unapproved and external-zone movement.","R3: SHA-256 mismatch; R4: bulk transfer window.","R5/R6: sensitive deletion and unauthorized user.","R0: ordinary or approved activity."])
    slide("Demo scenarios",["Approved backup and ordinary internal copy.","USB, cloud, network share, and unknown-folder movement.","Changed copy, in-place tamper, and sensitive deletion.","Two hundred tiny files in one destination window."])
    slide("Observed results",[f"{len(events)} event records in the latest clean run.","Required USB, integrity, and bulk alerts appeared.","Markdown, standalone HTML, and CSV reports were generated."],image=screen/"report_summary.png")
    slide("Integrity evidence",["MATCH: correct copy has the same SHA-256.","MISMATCH: altered dummy copy has a different SHA-256.","Before/after values are saved in evidence/integrity."],image=screen/"integrity_examples.png")
    slide("Testing",["Automated suite covers hash, policy, rules, copy inference, reports, and watchdog events.","Two test transcripts and two clean demo runs are kept under evidence/.","Acceptance checklist verifies 14 scenarios/objective checks."])
    slide("Limitations and conclusion",["Path-based external zones; no network-protocol inspection.","Process attribution and filesystem events vary by platform.","Windows verified here; Linux/macOS need their own run.","A small, explainable monitor with repeatable audit evidence."])
    prs.save(DOCS/"Final_Presentation.pptx")


def main():
    DOCS.mkdir(exist_ok=True); make_diagrams(); events=_load_events(); make_docx(events); make_pptx(events)
    # Re-open generated files to verify they are structurally readable.
    doc=Document(DOCS/"Project_Report.docx"); deck=Presentation(DOCS/"Final_Presentation.pptx")
    assert len(deck.slides)==11 and len(doc.sections)>=1
    assert sum(1 for p in doc.inline_shapes)>=2
    print(f"Generated diagrams, DOCX ({len(doc.inline_shapes)} images), and PPTX ({len(deck.slides)} slides).")


if __name__=="__main__": main()
