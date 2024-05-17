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







class patientpdfMaker:
    def __init__(self, patientName, patientSurname, patient_id, age, gender, bloodtype, admission_date, test_results, doctor_notes):
        self.patientName = patientName
        self.patientSurname = patientSurname
        self.patient_id = patient_id
        self.age = age
        self.gender = gender
        self.bloodtype = bloodtype
        self.admission_date = admission_date
        self.test_results = test_results
        self.doctor_notes = doctor_notes

    def generatepatient_report(self, output_filename):
        c = canvas.Canvas(output_filename, pagesize=letter)
        width, height = letter

        # Page 1 - Textual Information
        # Header
        c.setFont("Helvetica-Bold", 18)
        c.drawString(72, height - 72, "Blood Test Report")

        # Patient Details
        c.setFont("Helvetica", 12)
        c.drawString(72, height - 100, f"Patient Name: {self.patientName} {self.patientSurname}")
        c.drawString(72, height - 120, f"Patient ID: {self.patient_id}")
        c.drawString(72, height - 140, f"Age: {self.age}")
        c.drawString(72, height - 160, f"Gender: {self.gender}")
        c.drawString(72, height - 180, f"Blood Type: {self.bloodtype}")
        c.drawString(72, height - 200, f"Admission Date: {self.admission_date}")

        # Table Header
        y_position = height - 240
        c.setFont("Helvetica-Bold", 12)
        c.drawString(72, y_position, "Test Name")
        c.drawString(200, y_position, "Result")
        c.drawString(300, y_position, "Normal Range")
        c.line(72, y_position - 2, width - 72, y_position - 2)
        y_position -= 20

        # Test Results Table
        c.setFont("Helvetica", 12)
        for test_name, result, normal_range in self.test_results:
            c.drawString(72, y_position, test_name)
            c.drawString(200, y_position, result)
            c.drawString(300, y_position, normal_range)
            y_position -= 20

        # Doctor Notes Section
        c.setFont("Helvetica-Bold", 12)
        c.drawString(72, y_position, "Doctor Notes")
        c.line(72, y_position - 2, width - 72, y_position - 2)
        y_position -= 20

        c.setFont("Helvetica", 12)
        for line in self.doctor_notes:
            c.drawString(72, y_position, line)
            y_position -= 15

        c.showPage()  # Start a new page

        # Page 2 - Graphical Representation
        c.setFont("Helvetica-Bold", 18)
        c.drawString(72, height - 72, "Graphical Representation of Test Results")

        d = Drawing(450, 250)
        bar = VerticalBarChart()
        bar.x = 0
        bar.y = 0
        bar.height = 250
        bar.width = 450
        bar.data = [[float(result.split()[0].replace(',', '').replace('>', '').replace('<', '')) for _, result, _ in self.test_results]]
        bar.categoryAxis.categoryNames = [test[0] for test in self.test_results]
        bar.bars[0].fillColor = colors.blue
        d.add(bar)
        d.drawOn(c, 72, height - 350)

        c.showPage()
        c.save()

# Example usage
test_results = [
    ("Hemoglobin", "13.5 g/dL", "12.0 - 16.0 g/dL"),
    ("WBC", "5,600 /uL", "4,000 - 11,000 /uL"),
    ("Platelets", "150,000 /uL", "150,000 - 400,000 /uL"),
    ("Glucose", "90 mg/dL", "70 - 110 mg/dL"),
    ("Cholesterol", "180 mg/dL", "< 200 mg/dL"),
    ("HDL", "55 mg/dL", "40 - 60 mg/dL"),
    ("LDL", "100 mg/dL", "< 130 mg/dL"),
    ("Triglycerides", "140 mg/dL", "< 150 mg/dL"),
    ("Creatinine", "1.0 mg/dL", "0.6 - 1.2 mg/dL"),
    ("Bilirubin", "0.8 mg/dL", "0.1 - 1.0 mg/dL"),
    ("Alkaline Phosphatase", "90 U/L", "30 - 120 U/L"),
    ("ALT (SGPT)", "25 U/L", "10 - 40 U/L"),
    ("AST (SGOT)", "30 U/L", "10 - 40 U/L"),
    ("Albumin", "4.1 g/dL", "3.5 - 5.5 g/dL"),
    ("Total Protein", "7.0 g/dL", "6.0 - 8.0 g/dL"),
    ("Uric Acid", "5.5 mg/dL", "3.5 - 7.0 mg/dL")
]
doctor_notes = [
    "Patient shows generally stable blood results.",
    "Recommend a follow-up in 6 months for routine testing.",
    "Advise a balanced diet and regular exercise."
]
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


output_filename = "melisa_yurtekin_blood_test_report.pdf"
prescription = "prescription_report.pdf"
report= prescriptionpdfMaker("Alp Eren ", "Çakmak", 6 , 6, Prescription_inc, 6 )
report.generateprescription_report(prescription)

# Create an instance of patientpdfMaker
#report = patientpdfMaker("Melisa", "Yurtekin", 280320, 22, "Female", "B+", "08/05/2024", test_results, doctor_notes)

# Generate the report
#report.generatepatient_report(output_filename)