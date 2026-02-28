import opening
import random
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
import tkinter as tk
from tkinter import font
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

def get_heading():
    head = input("Write test heading: ")
    return head

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
    nqs = int(len(masq) / 3)
    getnm = getns2()
    nvar = getnm[0]
    nq = getnm[1]
    head = get_heading()
    varnow = 0;
    for i in range (nvar):
        varnow += 1
        nomervopr = 0
        opening.addcenter(head)
        opening.addcenter(f"Вариант {varnow}")
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
        opening.new_page()
    opening.savedoc()

def getting(totalmas):
    root = tk.Tk()
    root.title("Окно с вводом данных")
    root.geometry("700x500")
    root.configure(bg="#f0f0f0")

    main_font = font.Font(size=12)

    main_frame = tk.Frame(root, bg="#f0f0f0")
    main_frame.pack(expand=True, fill="both", padx=30, pady=30)

    input_frame = tk.Frame(main_frame, bg="#f0f0f0")
    input_frame.pack(expand=True, fill="both")

    labels = ["Номера вопросов:", "Количество вариантов:", "Количество вопросов:", "Название теста:"]
    left_entries = []
    right_entries = []

    for i, label_text in enumerate(labels):
        label = tk.Label(
            input_frame,
            text=label_text,
            font=main_font,
            bg="#f0f0f0",
            anchor="e"
        )
        label.grid(row=i, column=0, padx=(0, 10), pady=10, sticky="e")

        left_entry = tk.Entry(
            input_frame,
            font=main_font,
            bg="white",
            relief="solid",
            bd=1
        )
        left_entry.grid(row=i, column=1, padx=(0, 20), pady=10, sticky="ew")
        left_entries.append(left_entry)

        right_entry = tk.Entry(
            input_frame,
            font=main_font,
            bg="white",
            relief="solid",
            bd=1
        )
        right_entry.grid(row=i, column=2, padx=0, pady=10, sticky="ew")
        right_entries.append(right_entry)

    input_frame.grid_columnconfigure(1, weight=1, minsize=150)
    input_frame.grid_columnconfigure(2, weight=1, minsize=150)

    button_frame = tk.Frame(main_frame, bg="#f0f0f0")
    button_frame.pack(fill="x", pady=(30, 0))
    def vihod():
        root.destroy()
        start(totalmas)

    submit_button = tk.Button(
        button_frame,
        text="Далее",
        font=font.Font(size=14, weight="bold"),
        bg="#4CAF50",
        fg="white",
        padx=30,
        pady=10,
        relief="raised",
        bd=2,
        cursor="hand2",
        command = lambda: vihod()
    )
    submit_button.pack(side="right")

    root.mainloop()

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
            

def start(totalmas):
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

def pre_start():
    totalmas = opening.open(getway())
    getting(totalmas)


import tkinter as tk
from tkinter import font, scrolledtext


def razrab():
    root = tk.Tk()
    root.title("О разработчике")
    root.geometry("600x400")

    poem_text = "Годовой проект по информатике ученика Президентского физико-математического лицея №239 города Санкт-Петербурга Гаврилова Александра"

    text_widget = scrolledtext.ScrolledText(
        root,
        font=font.Font(family="Arial", size=14),
        wrap="word",
        padx=20,
        pady=20,
        bg="#fef9e7",
        fg="#34495e",
        bd=2,
        relief="solid"
    )
    text_widget.pack(expand=True, fill="both", padx=20, pady=20)

    text_widget.insert("1.0", poem_text)
    text_widget.config(state="disabled")

    root.mainloop()

def startmenu():
    root = tk.Tk()
    root.title("Преобразователь тестов")
    root.geometry("600x500")

    large_font = font.Font(size=16, weight="bold")

    output_entry = tk.Entry(
        root,
        font=large_font,
        justify="center",
        bg="lightgray",
        fg="black"
    )
    output_entry.pack(
        pady=20,
        padx=20,
        fill="x",
        ipady=10
    )
    output_entry.insert(0, "Приветствуем вас в нашей программе!")

    button_frame = tk.Frame(root)
    button_frame.pack(expand=True, fill="both", padx=20, pady=10)

    button1 = tk.Button(
        button_frame,
        text="Сделать тест",
        font=large_font,
        command = lambda: pre_start(),
        bg="lightblue",
        height=2,
        width=20
    )
    button1.pack(pady=10, expand=True)

    button2 = tk.Button(
        button_frame,
        text="Посмотреть инструкцию",
        font=large_font,
        bg="lightgreen",
        height=2,
        width=20
    )
    button2.pack(pady=10, expand=True)

    button3 = tk.Button(
        button_frame,
        text="О разработчике",
        font=large_font,
        bg="lightcoral",
        command = lambda: razrab(),
        height=2,
        width=20
    )
    button3.pack(pady=10, expand=True)

    root.mainloop()

if __name__ == "__main__":
    startmenu()
