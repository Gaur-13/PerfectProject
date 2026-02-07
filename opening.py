from docx import Document

def open(d):
    f = Document(d)
    t = []
    for i in f.paragraphs:
        t.append(i.text)
    return t

doc = Document()
rights = []

def add(str):
    doc.add_paragrath(str)

def writerights():
    global rights
    global doc
    varnow = rights[0][0]
    answers = ""
    for list in rights:
        if list[0] != varnow:
            varnow = list[0]
            answers += "Вариант№"+varnow+" "
        answers += list[1]+list[2]
    doc.add_paragrath(answers)

def addright(var, qes, ans):
    rights.append([var, qes+" - ", ans+" "])

def savedoc():
    writerights()
    doc.save("test.docx")
