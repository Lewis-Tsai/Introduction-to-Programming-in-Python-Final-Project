import sys, datetime, webbrowser
import tkinter, ctypes
import tkinter.ttk
#change system path before use!
sys.path.append(r"C:\Users\A3805\Desktop\HW\大二 第二學期\Python語言程式入門\109000129_蔡侑廷_hw4")
import matplotlib.pyplot as plt
from pyrecord import Record, Records
from pycategory import Categories

#--------------------------
def list_box_update():
    records_pack = records.view()
    records_listbox.delete(0, tkinter.END)
    for i in range(len(records_pack)):
        records_listbox.insert(tkinter.END, f'{records_pack[i][0]}  {records_pack[i][1]}  {records_pack[i][2]}  {records_pack[i][3]}')

def init_money_updte():
    if records.money_init == True:
        tkinter.messagebox.showwarning('pymoney', 'You have already initialized your money.')
    else:
        records.money_init = True
        records.update_value('money', int(init_money_str.get()))
        records.update_value('init_money', int(init_money_str.get()))
        list_box_update()
        now_money_str.set("Now you have " + str(records.get_value("money")) + " dollars.")

def add_to_record():
    #check date format
    try:
        formatted_date = str(datetime.date.fromisoformat(date_str.get()))
    except:
        tkinter.messagebox.showwarning('pymoney', "The format of date should be YYYY-MM-DD.\nFail to add a record.\n")
        return
    filtered_category = str(category_Combobox.get())
    filtered_category = filtered_category.replace(' ', '')
    filtered_category = filtered_category.replace('-', '')
    str_record = formatted_date + " " + filtered_category + " " + description_str.get() + " " + amount_str.get()
    #print(str_record)
    records.add(str_record, categories)
    #history_table = edit_history_table(history_table, 'add')
    #update
    list_box_update()
    now_money_str.set("Now you have " + str(records.get_value("money")) + " dollars.")

def delete_record():
    index_tuple = records_listbox.curselection()
    records.delete(index_tuple[0])
    #update
    list_box_update()
    now_money_str.set("Now you have " + str(records.get_value("money")) + " dollars.")

def find_category():
    target_categories = categories.find_subcategories(find_ctgry_str.get())
    result_list, result_money = records.find(target_categories)
    #update
    records_listbox.delete(0, tkinter.END)
    for i in range(len(result_list)):
        records_listbox.insert(tkinter.END, result_list[i])
    now_money_str.set(f'The total amount above is {result_money}.')

def list_box_reset():
    list_box_update()
    now_money_str.set("Now you have " + str(records.get_value("money")) + " dollars.")

def view_pie_chart():
    subcategories = 'meal', 'snack', 'drink', 'bus', 'railway'
    counts = []
    for i in range(len(subcategories)):
        subcat_expense = records.find(categories.find_subcategories(subcategories[i]), 'Pie Chart')
        counts.append(subcat_expense)
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lavender']
    explode = (0.1, 0, 0, 0, 0)
    plt.pie(counts, explode = explode, labels = subcategories, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
    plt.axis('equal')
    plt.show()

def video_play():
    webbrowser.open("https://www.youtube.com/watch?v=o-YBDTqX_ZU",new=1)

def on_closing():
    if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
        records.save()
        root.destroy()

categories = Categories()
records = Records()

# tklinker, with 10 rows, 7 columns
root = tkinter.Tk()
f = tkinter.Frame(root, borderwidth=5)
f.grid(row=0, column=0)
root.title("PyMoney")
root.tk.call('tk', 'scaling', 2)
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#stringVar
find_ctgry_str = tkinter.StringVar()
init_money_str = tkinter.StringVar()
init_money_str.set(records.get_value("init_money"))
now_money_str = tkinter.StringVar()
now_money_str.set("Now you have " + str(records.get_value("money")) + " dollars.")
date_str = tkinter.StringVar()
date_str.set(str(datetime.date.today().strftime('%Y-%m-%d')))
description_str = tkinter.StringVar()
amount_str = tkinter.StringVar()

#label
find_ctgry_label = tkinter.Label(f, text="Find Category")
now_money_label = tkinter.Label(f, textvariable=now_money_str)
init_money_label = tkinter.Label(f, text="Initial Money")
date_label = tkinter.Label(f, text="Date")
category_label = tkinter.Label(f, text="Category")
description_label = tkinter.Label(f, text="Description")
amount_label = tkinter.Label(f, text="Amount")

#entry
find_ctgry_entry = tkinter.Entry(f, textvariable=find_ctgry_str)
init_money_entry = tkinter.Entry(f, textvariable=init_money_str)
date_entry = tkinter.Entry(f, textvariable=date_str)
description_entry = tkinter.Entry(f, textvariable=description_str)
amount_entry = tkinter.Entry(f, textvariable=amount_str)

#button
find_ctgry_btn = tkinter.Button(f, text="Find", command=find_category)
find_ctgry_rst_btn = tkinter.Button(f, text="Reset", command=list_box_reset)
init_money_updte_btn = tkinter.Button(f, text="Update", command=init_money_updte)
add_record_btn = tkinter.Button(f, text="Add a record", command=add_to_record)
delete_btn = tkinter.Button(f, text="Delete", width=5, command=delete_record)
chart_btn = tkinter.Button(f, text="📊", width=5, command=view_pie_chart)
video_btn = tkinter.Button(f, text="🎥", width=5, command=video_play)

#listbox
records_listbox = tkinter.Listbox(f, width=45, height=12, selectmode=tkinter.SINGLE)
list_box_update()

#Combobox
ComboboxList = ['- expense','    - food','      - meal','      - snack','      - drink', 
                '    - transportation', '      - bus', '      - railway',
                '- income', '    - salary', '    - bonus']
category_Combobox = tkinter.ttk.Combobox(f, values=ComboboxList, width=17)

#grid
find_ctgry_label.grid(row=0, column=0)
find_ctgry_entry.grid(row=0, column=1)
find_ctgry_btn.grid(row=0, column=2)
find_ctgry_rst_btn.grid(row=0, column=3)

records_listbox.grid(row=1, column=0, rowspan=7, columnspan=4, pady=3)

init_money_label.grid(row=1, column=4)
init_money_entry.grid(row=1, column=5)

init_money_updte_btn.grid(row=2, column=5, sticky=tkinter.E, pady=3)

date_label.grid(row=3, column=4)
date_entry.grid(row=3, column=5, pady=3)

category_label.grid(row=4, column=4)
category_Combobox.grid(row=4, column=5, sticky="ew", pady=3)

description_label.grid(row=5, column=4)
description_entry.grid(row=5, column=5, pady=3)

amount_label.grid(row=6, column=4)
amount_entry.grid(row=6, column=5, pady=3)

add_record_btn.grid(row=7, column=5, sticky=tkinter.E, pady=3)

now_money_label.grid(row=8, column=0, columnspan=2, sticky=tkinter.W)
delete_btn.grid(row=8, column=3, sticky=tkinter.E)
video_btn.grid(row=8, column=4)
chart_btn.grid(row=8, column=5, sticky=tkinter.E)

root.protocol("WM_DELETE_WINDOW", on_closing)
tkinter.mainloop()