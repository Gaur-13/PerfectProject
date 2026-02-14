from docx import Document
import os

def open(d):
    f = Document(d)
    t = []
    for i in f.paragraphs:
        t.append(i.text)
    return t

doc = Document()
rights = []

def add(str):
    doc.add_paragraph(str)

def writerights():
    print(rights)
    varnow = rights[0][0]
    answers = "Вар 1. "
    for list in rights:
        if list[0] != varnow:
            varnow = list[0]
            answers += f"Вар {varnow}. "
        answers += f"{list[1]} - {list[2]}), "
    doc.add_paragraph(answers)

def addright(qes, ans, var):
    rights.append([var, qes, ans])

def savedoc():
    writerights()
    doc.save("test.docx")
    os.startfile('test.docx')
