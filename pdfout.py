#!/usr/bin/env python3
import os
import re

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

class PDF_OUT:
    def __init__(self):
        pass  # no auto-run

    def txt_to_pdf(self, input_file, output_file):
        if not os.path.isfile(input_file):
            print(f"[-] Input file not found: {input_file}")
            return False

        try:
            c = canvas.Canvas(output_file, pagesize=letter)
            width, height = letter

            font_size = 6
            line_height = 10
            current_font = "Courier-Bold"
            c.setFont(current_font, font_size)

            y_position = height - inch

            with open(input_file, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            clean_content = re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', content)
            lines = clean_content.splitlines()
            total_lines = len(lines)
            print(f"[+] Processing {total_lines} lines with font: {current_font}")

            for line in lines:
                if y_position < inch:
                    c.showPage()
                    c.setFont(current_font, font_size)
                    y_position = height - inch

                if not line.strip():
                    y_position -= 5
                    continue

                if len(line) > 200:
                    chunks = [line[i:i+120] for i in range(0, len(line), 120)]
                    for chunk in chunks:
                        if y_position < inch:
                            c.showPage()
                            c.setFont(current_font, font_size)
                            y_position = height - inch
                        c.drawString(inch, y_position, chunk)
                        y_position -= line_height
                elif len(line) > 120:
                    display_line = line[:117] + "..."
                    c.drawString(inch, y_position, display_line)
                    y_position -= line_height
                else:
                    c.drawString(inch, y_position, line)
                    y_position -= line_height

            c.save()
            print(f"[+] PDF successfully saved as {output_file}")
            return True

        except Exception as e:
            print(f"[-] Error: {e}")
            return False
