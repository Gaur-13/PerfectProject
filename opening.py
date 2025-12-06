import docx

def open(d):
    f = docx.Document(d)
    t = []
    for i in len(f.paradraphs):
        t.upend(f.paragraphs[i].text)
    return t