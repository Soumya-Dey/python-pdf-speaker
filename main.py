
import pyttsx3
import PyPDF2

book = open('test.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)

speaker = pyttsx3.init()
volume = speaker.getProperty('volume')
rate = speaker.getProperty('rate')

speaker.setProperty('volume', volume - 0.75)
speaker.setProperty("rate", rate - 60)

for num in range(0, pdfReader.numPages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    speaker.stop()
