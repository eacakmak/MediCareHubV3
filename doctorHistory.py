import customtkinter as ctk
from customtkinter import *
from tkinter import *
from tkinter import ttk
import mysql.connector
from CTkMessagebox import CTkMessagebox
from PIL import Image



class MedicaldocHistoryPage():
    def __init__(self,doktorid):
        self.doktorid = doktorid
        self.app=CTk()
        self.app.title('Doctors History')
        self.app.resizable(False,False)
        self.app.geometry('900x600')
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="alperen0519",
            database="MediCareHub",
            auth_plugin='mysql_native_password'
        )
        self.uihistory()





    def uihistory(self):
        main_frame = CTkFrame(master=self.app)
        main_frame.pack(fill=BOTH, expand=True)

        # Left Frame for Logo
        left_frame = CTkFrame(master=main_frame, width=200, height=600, fg_color="#2C3E50")
        left_frame.pack_propagate(0)
        left_frame.pack(side=LEFT, fill=Y)

        imgLogo = Image.open("images/logo.png")
        imgLogoicon = CTkImage(dark_image=imgLogo, light_image=imgLogo, size=(150, 150))
        logoLabel = CTkLabel(master=left_frame, text="", image=imgLogoicon)
        logoLabel.pack(pady=20)

        # Right Frame for Medical History
        right_frame = CTkFrame(master=main_frame, width=700, height=600, fg_color="#ECF0F1")
        right_frame.pack_propagate(0)
        right_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)

        label = CTkLabel(master=right_frame, text="Medical History", font=("Arial Bold", 20),text_color="#000000")
        label.pack(pady=10)

        columns = ("Record_ID", "Pre_Conditions")
        self.tree = ttk.Treeview(right_frame, columns=columns, show='headings', style="mystyle.Treeview")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, minwidth=0, width=150)

        self.tree.pack(expand=True, fill=BOTH, padx=10, pady=10)

        self.fetch_medical_history()

        # Customize Treeview Style
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Arial', 12))
        style.configure("mystyle.Treeview.Heading", font=('Arial Bold', 14))
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

    def fetch_medical_history(self):
        try:
            cursor = self.mydb.cursor()
            query = """
                SELECT 
                    Record_ID, 
                    Pre_Conditions
                FROM 
                    medical_history
                WHERE 
                    Doctor_ID = %s
            """
            cursor.execute(query, (self.doktorid,))
            rows = cursor.fetchall()

            for row in rows:
                self.tree.insert('', 'end', values=row)

            cursor.close()
        except mysql.connector.Error as e:
            CTkMessagebox(title="Database Error", message=f"An error occurred: {e}", icon="cancel")
    def run(self):
        self.app.mainloop()












