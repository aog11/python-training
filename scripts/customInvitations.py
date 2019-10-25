# Chapter 13
# Custom Invitations As Word Documents Project

# Importing the needed modules
import os, docx

# Location to place the files
docDir = ''
os.chdir(docDir)

# Creating the docx document
doc = docx.Document('template.docx')

breaksAdded = 1

# Reading the names of the guests.
with open('guests.txt','r') as guestsFile:
    guests = guestsFile.readlines()
    for guest in guests:
        # Adding the paragraphs
        paraObj1 = doc.add_paragraph('It would be a pleasure to have the company of')
        paraObj1.style = 'BoldCursiveItalic'
        paraObj2 = doc.add_paragraph(guest.replace('\n',''))
        paraObj2.style = 'BoldRoman'
        paraObj3 = doc.add_paragraph('at 11010 Memory Lane on the Evening of')
        paraObj3.style = 'BoldCursiveItalic'
        paraObj4 = doc.add_paragraph('April 1st')
        paraObj4.style = 'BigRoman'
        paraObj5 = doc.add_paragraph('at 7 o\'clock')
        paraObj5.style = 'BoldCursiveItalic'
        # Adding the page break after the last paragraph
        # and avoiding a page break after the last guest
        if breaksAdded != len(guests):
            run = paraObj5.add_run()
            run.add_break(docx.enum.text.WD_BREAK.PAGE)
            breaksAdded+=1

# Saving the resulting invitations file
doc.save('invitations.docx')