from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart



class prescriptionpdfMaker:
    def __init__(self, patientName, patientSurname, Prescription_ID , Patient_Id, Prescription_inc, Doctor_ID  ):
        self.patientName = patientName
        self.patientSurname = patientSurname
        self.Prescription_ID = Prescription_ID
        self.Patient_Id = Patient_Id
        self.Prescription_inc = Prescription_inc
        self.Doctor_ID = Doctor_ID

    def generateprescription_report(self, output_filename):
        c = canvas.Canvas(output_filename, pagesize=letter)
        width, height = letter

        # Page 1 - Textual Information
        # Header
        c.setFont("Helvetica-Bold", 18)
        c.drawString(72, height - 72, "Prescription Report")

        # Patient Details
        c.setFont("Helvetica", 12)
        c.drawString(72, height - 100, f"Patient Name: {self.patientName} {self.patientSurname}")
        c.drawString(72, height - 120, f"Patient ID: {self.Patient_Id}")

        # Table Header
        y_position = height - 160
        c.setFont("Helvetica-Bold", 12)
        c.drawString(72, y_position, "Prescription_ID")
        c.drawString(200, y_position, "Medicine_ID")
        c.drawString(300, y_position, "Dosage")
        c.line(72, y_position - 2, width - 72, y_position - 2)
        y_position -= 20

        # Test Results Table
        c.setFont("Helvetica", 12)
        for Prescription_ID, Medicine_ID, Dosage in self.Prescription_inc:
            c.drawString(72, y_position, Prescription_ID)
            c.drawString(200, y_position, Medicine_ID)
            c.drawString(300, y_position, Dosage)
            y_position -= 20

        c.showPage()  # Start a new page

        c.save()

# Example usage
Prescription_inc= [
    ("1", "101", "2 pills daily"),
    ("2", "102", "1 tablet every 8 hours"),
    ("3", "103", "1 teaspoon twice a day"),
    ("4", "104", "1 spray in each nostril once daily"),
    ("5", "105", "1 injection per week"),
    ("6", "106", "3 drops in each eye every 6 hours"),
    ("7", "107", "1 patch applied to the skin every 24 hours"),
    ("8", "108", "1 capsule with meals"),
    ("9", "109", "1 suppository at bedtime"),
    ("10", "110", "1 lozenge every 4 hours as needed")
]

output_filename = "prescription_report.pdf"
report= prescriptionpdfMaker("Alp Eren ", "Çakmak", 6 , 6, Prescription_inc, 6 )
report.generateprescription_report(output_filename)
