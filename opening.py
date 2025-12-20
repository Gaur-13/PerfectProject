from docx import Document

def open(d):
    f = Document(d)
    t = []
    for i in f.paragraphs:
        t.append(i.text)
    return t

doc = Document()

def writein(str):
    global doc
    doc.add_paragrath(str)

def savedoc():
    doc.save("test.docx")