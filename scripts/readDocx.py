# Chapter 13
# Getting all text in a docx file in a single string

#! python3

import docx

def getText(filename):
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return'\n'.join(fullText)