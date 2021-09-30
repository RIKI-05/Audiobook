# PYPDF2 
# Pyttsx3

import pyttsx3
import PyPDF2

# speaker = pyttsx3.init()
# speaker.say("hi how are you")

book = open("dafinkers.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker =pyttsx3.init()
for num in range(pages):
    page=pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    print(text)
    speaker.runAndWait()
    