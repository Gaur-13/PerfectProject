from docx import Document

def open(d):
    f = Document(d)
    t = []
    for i in f.paragraphs:
        t.append(i.text)
    return t