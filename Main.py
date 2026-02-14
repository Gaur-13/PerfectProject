import opening
import random
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
#format disciption of some of variables: 1) promezh[]: list of uncorrect answer; 2) masq[]: question, [uncorrect answers,], correct answer; 3) nqs: number of questions we have; 4) nq: number of questions we need; 5) ourq: list of questions in right order6) our_ans_list: list of answers in right order; 6)


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
    
def addingAns(our_ans_list, right, nomervopr, varnow):
    nomer = 0
    nomer_right = random.randint(1, len(our_ans_list)+1)
    for a in our_ans_list:
        nomer += 1
        if nomer == nomer_right:
            opening.add(f"{nomer}) {right}")
            nomer += 1
            opening.addright(nomervopr, nomer_right, varnow)
        opening.add(f"{nomer}) {a}")
    if nomer_right == len(our_ans_list)+1:
        opening.add(f"{nomer_right}) {right}")
        opening.addright(nomervopr, nomer_right, varnow)
        

def preobr(masq):
    getnm = getns2()
    nvar = getnm[0]
    nq = getnm[1]
    nqs = int(len(masq)/3)
    varnow = 0;
    for i in range (nvar):
        varnow += 1
        nomervopr = 0
        opening.add(f"Вариант {varnow}")
        ourq = random.sample(range(0, nqs), nq)
        for k in ourq:
            nomervopr += 1
            print(k)   #delete later
            qes = masq[k*3]
            ans = masq[k*3+1]
            right = masq[k*3+2]
            our_ans_list = random.sample(ans, len(ans))
            opening.add(f"{nomervopr}. {qes}")
            addingAns(our_ans_list, right, nomervopr, varnow)
    opening.savedoc()

def getway():
    app = QApplication(sys.argv)

    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Выберите документ",
        "",
        "*.docx"
    )

    return file_path

    app.exit()
            

def start():
    totalmas = opening.open(getway())
    qn = getns1()  # question numbers
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
