import opening
import random
from PyQt5.QtWidgets import QApplication, QFileDialog
import sys
import with_serv
import tkinter as tk
from tkinter import font
from tkinter import font, scrolledtext
#format disciption of some of variables: 1) promezh[]: list of uncorrect answer; 2) masq[]: question, [uncorrect answers,], correct answer; 3) nqs: number of questions we have; 4) nq: number of questions we need; 5) ourq: list of questions in right order6) our_ans_list: list of answers in right order;


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


def sort(numbers_string):
    return sorted([int(x.strip()) for x in numbers_string.split(',')])

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
        

def preobr(masq, getnm, head):
    nqs = int(len(masq) / 3)
    nvar = getnm[0]
    nq = getnm[1]
    varnow = 0
    for i in range (nvar):
        varnow += 1
        nomervopr = 0
        opening.addcenter(head)
        opening.addcenter(f"Вариант {varnow}")
        ourq = random.sample(range(0, nqs), nq)
        for k in ourq:
            nomervopr += 1
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
    root.configure(bg='#2c3e50')

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 700) // 2
    y = (screen_height -500) // 2
    root.geometry(f"700x500+{x}+{y}")

    main_font = font.Font(size=12)

    main_frame = tk.Frame(root, bg='#2c3e50')
    main_frame.pack(expand=True, fill="both", padx=30, pady=30)

    input_frame = tk.Frame(main_frame, bg='#2c3e50')
    input_frame.pack(expand=True, fill="both")

    labels = ["Номера вопросов:", "Количество вариантов:", "Количество вопросов:", "Название теста:"]

    for i, label_text in enumerate(labels):
        label = tk.Label(
            input_frame,
            text=label_text,
            font=main_font,
            bg='#2c3e50',
            anchor="e",
            fg='white'
        )
        label.grid(row=i, column=0, padx=(0, 10), pady=10, sticky="e")
    left_entry1 = tk.Entry(
        input_frame,
        font=main_font,
        bg='#34495e',
        relief="solid",
        bd=1,
        fg='white'
    )
    left_entry1.grid(row=0, column=1, padx=(0, 20), pady=10, sticky="ew")
    left_entry1.focus_set()
    left_entry2 = tk.Entry(
        input_frame,
        font=main_font,
        bg='#34495e',
        relief="solid",
        bd=1,
        fg='white'
    )
    left_entry2.grid(row=1, column=1, padx=(0, 20), pady=10, sticky="ew")
    left_entry3 = tk.Entry(
        input_frame,
        font=main_font,
        bg='#34495e',
        relief="solid",
        bd=1,
        fg='white'
    )
    left_entry3.grid(row=2, column=1, padx=(0, 20), pady=10, sticky="ew")
    left_entry4 = tk.Entry(
        input_frame,
        font=main_font,
        bg='#34495e',
        relief="solid",
        bd=1,
        fg='white'
    )
    left_entry4.grid(row=3, column=1, padx=(0, 20), pady=10, sticky="ew")

    input_frame.grid_columnconfigure(1, weight=1, minsize=150)
    input_frame.grid_columnconfigure(2, weight=1, minsize=150)

    button_frame = tk.Frame(main_frame, bg='#2c3e50')
    button_frame.pack(fill="x", pady=(30, 0))
    def vihod():
        start(totalmas, sort(left_entry1.get()), [int(left_entry2.get()), int(left_entry3.get())], left_entry4.get(), root)

    submit_button = tk.Button(
        button_frame,
        text="Далее",
        font=font.Font(size=14, weight="bold"),
        bg='#3498db',
        fg="white",
        padx=30,
        pady=10,
        relief="raised",
        bd=2,
        cursor="hand2",
        command = vihod,
        activebackground='#2980b9',
        activeforeground='white'
    )
    submit_button.pack(side="right")
    foc_now = 1
    def set_focus():
        global foc_now
        if foc_now==1:
            left_entry2.focus_set()
            foc_now = 2
        if foc_now==2:
            foc_now = 3
            left_entry3.focus_set()
        if foc_now==3:
            foc_now = 4
            left_entry4.focus_set()
    root.bind("<Return>", set_focus)

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

def get_from_serv():
    root = tk.Tk()
    root.title("Ввод IP")
    root.configure(bg='#2c3e50')

    root.update_idletasks()
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w - 500) // 2
    y = (screen_h - 200) // 2
    root.geometry(f"{500}x{200}+{x}+{y}")

    main_frame = tk.Frame(root, bg='#2c3e50')
    main_frame.pack(expand=True, fill='both', padx=40, pady=30)

   
    input_row = tk.Frame(main_frame, bg='#2c3e50')
    input_row.pack(pady=10)

    label = tk.Label(
        input_row,
        text="IP-адрес:",
        font=('Arial', 12, 'bold'),
        fg='white',
        bg='#2c3e50'
    )
    label.pack(side='left', padx=(0, 10))

    ip_entry = tk.Entry(
        input_row,
        font=('Arial', 12),
        bg='#34495e',
        fg='white',
        insertbackground='white',
        relief='solid',
        bd=1
    )
    ip_entry.pack(side='left')
    ip_entry.focus_set()

    def servpreobr():
        ipa = ip_entry.get()
        root.destroy()
        getting(with_serv.getserv(ipa, "test1"))

    btn = tk.Button(
        main_frame,
        text="Далее",
        command=servpreobr,
        font=('Arial', 12, 'bold'),
        fg='white',
        bg='#3498db',
        activebackground='#2980b9',
        activeforeground='white',
        relief='raised',
        bd=2,
        cursor='hand2',
        width=12
    )
    btn.pack(pady=20)

    root.mainloop()


def start(totalmas, qn, getnm, head, root):
    masq = []  # question we need
    root.destroy()
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
    preobr(masq, getnm, head)

def pre_start():
    totalmas = opening.open(getway())
    getting(totalmas)

def viborotk():
    root = tk.Tk()
    root.title("Выбор источника данных")
    root.geometry("500x350")
    root.configure(bg='#2c3e50')

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 500) // 2
    y = (screen_height - 350) // 2
    root.geometry(f"500x350+{x}+{y}")

    button_style = {
        'font': ('Arial', 12, 'bold'),
        'fg': 'white',
        'bg': '#3498db',
        'activebackground': '#2980b9',
        'activeforeground': 'white',
        'relief': 'raised',
        'bd': 2,
        'width': 15,
        'height': 2,
        'cursor': 'hand2'
    }

    title_label = tk.Label(root, text="Выберите способ загрузки данных", font=('Arial', 16, 'bold'), fg='white', bg='#2c3e50')
    title_label.pack(pady=(50, 30))

    button_frame = tk.Frame(root, bg='#2c3e50')
    button_frame.pack(expand=True, fill='both', padx=50)

    btn_file = tk.Button(button_frame, text="📁 Свой файл", command=pre_start, **button_style)
    btn_server = tk.Button(button_frame, text="🌐 С сервера", command=get_from_serv, **button_style)

    button_frame.grid_columnconfigure(0, weight=1)
    button_frame.grid_columnconfigure(1, weight=1)
    button_frame.grid_rowconfigure(0, weight=1)

    btn_file.grid(row=0, column=0, padx=10, pady=20, sticky='e')
    btn_server.grid(row=0, column=1, padx=10, pady=20, sticky='w')

    def on_enter(event, button):
        button.config(bg='#2980b9')

    def on_leave(event, button):
        button.config(bg='#3498db')

    btn_file.bind("<Enter>", lambda e: on_enter(e, btn_file))
    btn_file.bind("<Leave>", lambda e: on_leave(e, btn_file))
    btn_server.bind("<Enter>", lambda e: on_enter(e, btn_server))
    btn_server.bind("<Leave>", lambda e: on_leave(e, btn_server))

    footer_label = tk.Label(root, text="Выберите источник данных для продолжения", font=('Arial', 9), fg='#bdc3c7', bg='#2c3e50')
    footer_label.pack(side='bottom', pady=20)

    root.mainloop()


def instr():
    root = tk.Tk()
    root.title("О разработчике")
    root.geometry("600x750")

    text1 = "Чтобы сделать тест необходимо подготовить файл формата .docx, в котором будут вопросы, пронумерованные от 1 до некоторого числа. Варианты ответа должны быть указаны в формате буква+)+пробел+вариант ответа. У правильного ответа вместо скобки должна стоять дробь /. С сервера можно получить тест по математике."

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

    text_widget.insert("1.0", text1)
    text_widget.config(state="disabled")

    button2 = tk.Button(
        root,
        text="Назад",
        bg="lightgreen",
        height=2,
        width=20,
        command =lambda: root.destroy()+startmenu())
    button2.pack(pady=10, expand=True)

    root.mainloop()



def razrab():
    root = tk.Tk()
    root.title("О разработчике")
    root.geometry("600x750")

    text1 = "Годовой проект по информатике ученика Президентского физико-математического лицея №239 города Санкт-Петербурга Гаврилова Александра"

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

    text_widget.insert("1.0", text1)
    text_widget.config(state="disabled")

    button2 = tk.Button(
        root,
        text="Назад",
        bg="lightgreen",
        height=2,
        width=20,
        command =lambda: root.destroy()+startmenu())
    button2.pack(pady=10, expand=True)

    root.mainloop()

def startmenu():
    root = tk.Tk()
    root.title("Преобразователь тестов")
    root.geometry("700x500")
    root.configure(bg='#2c3e50')

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - 700) // 2
    y = (screen_height - 500) // 2
    root.geometry(f"700x500+{x}+{y}")
    large_font = font.Font(size=16, weight="bold")

    output_label = tk.Label(
        root,
        text="Приветствуем вас в нашей программе!",
        font=font.Font(family="Segoe Script", size=16, slant="italic"),
        justify="center",
        bg='#2c3e50',
        fg="white"
    )
    output_label.pack(
        pady=20,
        padx=20,
        fill="x",
        ipady=10
    )

    button_frame = tk.Frame(root? bg='#2c3e50')
    button_frame.pack(expand=True, fill="both", padx=20, pady=10)

    button1 = tk.Button(
        button_frame,
        text="Сделать тест",
        font=large_font,
        command = lambda: root.destroy()+viborotk(),
        bg='#3498db',
        height=2,
        width=20,
        fg='white',
        activebackground='#2980b9',
        activeforeground='white',
        relief='raised',
        bd=2,
        cursor='hand2'
    )
    button1.pack(pady=10, expand=True)

    button2 = tk.Button(
        button_frame,
        text="Посмотреть инструкцию",
        font=large_font,
        bg='#3498db',
        height=2,
        width=20,
        fg='white',
        command = lambda: root.destroy()+instr(),
        activebackground='#2980b9',
        activeforeground='white',
        relief='raised',
        bd=2,
        cursor='hand2'
    )
    button2.pack(pady=10, expand=True)

    button3 = tk.Button(
        button_frame,
        text="О разработчике",
        font=large_font,
        bg='#3498db',
        command = lambda: root.destroy()+razrab(),
        height=2,
        width=20,
        fg='white',
        activebackground='#2980b9',
        activeforeground='white',
        relief='raised',
        bd=2,
        cursor='hand2'
    )
    button3.pack(pady=10, expand=True)

    root.mainloop()

if __name__ == "__main__":
    startmenu()
