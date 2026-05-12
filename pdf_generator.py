from fpdf import FPDF
import datetime

# Read AI report
with open("ai_report.txt", "r", encoding="utf-8") as file:
    report_text = file.read()

# Clean markdown symbols
report_text = report_text.replace("**", "")
report_text = report_text.replace("#", "")

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add page
pdf.add_page()

# Title
pdf.set_font("Helvetica", "B", 18)
pdf.cell(
    0,
    10,
    "Cisco Sales Analysis Report",
    new_x="LMARGIN",
    new_y="NEXT",
    align="C"
)

# Date
pdf.set_font("Helvetica", "", 11)

today = datetime.date.today()

pdf.cell(
    0,
    8,
    f"Generated on: {today}",
    new_x="LMARGIN",
    new_y="NEXT",
    align="C"
)

pdf.ln(10)

# Main content
pdf.set_font("Helvetica", "", 12)

for line in report_text.split("\n"):

    line = line.strip()

    # Empty line spacing
    if not line:
        pdf.ln(5)
        continue

    # Remove weird extra spaces
    line = " ".join(line.split())

    try:
        pdf.multi_cell(190, 8, txt=line)
        pdf.ln(1)

    except:
        continue

# Save PDF
pdf.output("sales_report.pdf")

print("Professional PDF report generated successfully!")