import time

import customtkinter
import tkinter
from tkinter import Tk, messagebox
from customtkinter import *
from tkinter import *
from PIL import *
import mysql.connector
from CTkMessagebox import *
import subprocess
import sys
import mysql.connector
from tkinter import messagebox
from doctorMain import doctorMainPage

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="bercan2003",
    database="MediCareHub",
)
username ="alice_williams"
password="docpass123"
mycursor = mydb.cursor()

# Update the column name based on your table schema
query = "SELECT Doctor_ID,password FROM loginpagedoctor WHERE username = %s"
mycursor.execute(query, (username,))

myresult = mycursor.fetchall()
print(myresult[0][0])

if myresult:
    real_password = myresult[0][0]

    if real_password == password:

        CTkMessagebox(title="Info", message="Welcome to MediCareHub Services!")
