import opening

def getstartnumber(a):
    for i in range(a.lenght):
        if not a[i] in numbers:
            break
    if i==0: return -1
    else: return int(a[0: i])

def start():
    totalmas = opening.open('test1.docx')
    qn = []; #question numbers
    nq = int(input()); #number of questions
    for i in range(nq):
        qn.append(int(input()))
    masq = [] #question we need
    isq = False
    promezh = []
    for str in totalmas:
        if getstartnumber(str) in qn:
            isq = True
            masq.append(str)
        elif getstartnumber(str)!=-1:
            if promezh!=[]:
                masq.append(promezh)
        if isq:
            promezh.append(str)
if __name__=="__main__":
    start()