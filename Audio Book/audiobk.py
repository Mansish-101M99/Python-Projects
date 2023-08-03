# pip install PyPDF2     pip install pyttsx3
import PyPDF2
import pyttsx3

engine = pyttsx3.init()  # ------------>>  Initialize this class's object
file_pdf = open("sample.pdf", "rb")
rd_pdf = PyPDF2.PdfReader(file_pdf) 

for pgn in range(len(rd_pdf.pages)):
    text = rd_pdf.pages[pgn].extract_text()
    engine.say(text)
    # engine.runAndWait()
    engine.save_to_file(text, "audbk.mp3")
    engine.runAndWait()