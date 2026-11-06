"""Render an actual terminal transcript as a readable dark-theme PNG."""
from __future__ import annotations
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def render(source: Path, output: Path) -> None:
    text = source.read_text(encoding="utf-8", errors="replace")
    lines = text.expandtabs(4).splitlines() or [""]
    font_path = next((p for p in [Path("C:/Windows/Fonts/consola.ttf"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"), Path("/System/Library/Fonts/Menlo.ttc")] if p.exists()), None)
    font = ImageFont.truetype(str(font_path), 16) if font_path else ImageFont.load_default()
    max_chars = min(max(len(line) for line in lines), 150)
    width, line_h, margin = max(760, max_chars * 10 + 48), 24, 24
    height = max(120, min(len(lines), 90) * line_h + margin * 2)
    image = Image.new("RGB", (width, height), "#111827")
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((12, 12, width - 12, height - 12), radius=10, fill="#182230", outline="#324154", width=2)
    draw.ellipse((28, 26, 40, 38), fill="#ff5f57"); draw.ellipse((50, 26, 62, 38), fill="#febc2e"); draw.ellipse((72, 26, 84, 38), fill="#28c840")
    for i, line in enumerate(lines[:90]):
        if len(line) > max_chars: line = line[:max_chars - 3] + "..."
        color = "#f2f5f8"
        if "CRITICAL" in line or "FAIL" in line: color = "#ff7770"
        elif "HIGH" in line or "PASS" in line: color = "#ffd166"
        draw.text((margin, 54 + i * line_h), line, font=font, fill=color)
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("transcript", type=Path); parser.add_argument("output", type=Path)
    args = parser.parse_args(); render(args.transcript, args.output); print(f"Saved {args.output}"); return 0


if __name__ == "__main__": raise SystemExit(main())
