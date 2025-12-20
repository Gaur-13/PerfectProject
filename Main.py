import opening
import random


def getstartnumber(a):
    i = 0
    numbers = [str(i) for i in range(10)]
    for i in range(len(a)):
        if not a[i] in numbers:
            break
    if i == 0:
        return -1
    else:
        return int(a[0: i])


def withoutbegin(a):
    return a[3: len(a)]


def realright(a):
    if a[1] == "/":
        return True
    else:
        return False

def getns1(): # Get NumberS 1
    nq = int(input("Write number of questions: "));  # number of questions
    print("Write question numbers: ")
    qn = []
    for i in range(nq):
        qn.append(int(input()))
    return qn

def getns2(): #Get NumberS 2
    nvar = int(input("Write number of versions: "))
    nq = int(input("Write number of questions in every test: "))
    return [nvar, nq]

def preobr(masq):
    getnm = getns2()
    nvar = getnm[0]
    nq = getnm[1]
    nqs = int(len(masq)/3)
    for i in range (nvar):
        ourq = random.sample(range(1, nqs+1), nq)

def start():
    totalmas = opening.open('test1.docx')
    qn = getns1();  # question numbers
    masq = []  # question we need
    isq = False
    promezh = []
    right = ""
    for str in totalmas:
        if getstartnumber(str) in qn:
            if not isq:
                isq = True
            else:
                masq.append(promezh)
                masq.append(right)
                promezh = []
            masq.append(withoutbegin(str))
        elif getstartnumber(str) != -1:
            if promezh != []:
                masq.append(promezh)
                masq.append(right)
                promezh = []
            isq = False
        else:
            if isq:
                if str != "":
                    if realright(str):
                        right = withoutbegin(str)
                    else:
                        promezh.append(withoutbegin(str))
    if isq:
        masq.append(promezh)
        masq.append(right)
    print(masq)
    preobr(masq)


if __name__ == "__main__":
    start()
