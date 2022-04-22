from tkinter import *
import sqlite3


# Main window stuff
mainWindow = Tk()
mainWindow.title("Contacts Database GUI")
mainWindow.iconbitmap("blackBox.ico")
mainWindow.configure(background='black')


# Main Functions
def update_edit():
    rFrame_listbox.delete(0, END)

    db = sqlite3.connect("contacts.db")
    conn = db.cursor()
    row = ''
    for row in conn.execute("SELECT * FROM contacts"):
        list_convert = list(row)
        l_first_name = list_convert[0]
        l_last_name = list_convert[1]
        justName = l_first_name + " " + l_last_name
        rFrame_listbox.insert(0, justName)

    db.commit()
    db.close()


def update_db():

    update_db2 = sqlite3.connect("contacts.db")
    update_conn = db.cursor()

    row = ''
    list_convert2 = []

    for row_update in update_conn.execute("SELECT *, oid FROM contacts"):
        list_convert2 = list(row_update)

    id_numbers = list_convert2
    new_f_name = id_numbers[0]
    new_l_name = id_numbers[1]
    new_data = new_f_name + " " + new_l_name
    rFrame_listbox.insert(0, new_data)

    update_db2.commit()
    update_db2.close()


def left_frame_button():
    """Main function that submits user input to database"""
    # Connecting to Database
    db = sqlite3.connect("contacts.db")
    conn = db.cursor()

    conn.execute("INSERT INTO contacts VALUES (:f_name, :l_name, :phone, :address)",
                 {
                     'f_name': first_name_input.get(),
                     'l_name': last_name_input.get(),
                     'phone': phone_number_input.get(),
                     'address': address_input.get()
                 })
    db.commit()
    db.close()

    first_name_input.delete(0, END)
    last_name_input.delete(0, END)
    phone_number_input.delete(0,END)
    address_input.delete(0, END)
    update_db()


def submit_button():
    """Second submit function belonging to the second submit button that takes what the user clicked and
        configures it onto the GUI"""
    button_db = sqlite3.connect("contacts.db")
    button_conn = db.cursor()

    for row3 in button_conn.execute("SELECT *, oid FROM contacts"):
        list_records = list(row3)
        first_name = list_records[0]
        last_name = list_records[1]

        first_last = first_name + " " + last_name

        mainList = rFrame_listbox.get(ANCHOR)

        if mainList == first_last:

            first_name = list_records[0]
            last_name = list_records[1]
            first_last = first_name + " " + last_name
            phone = list_records[2]
            address = list_records[3]
            id_num = str(list_records[4])
            print(first_last + " " + "ID Number: " + id_num)   # TODO remove after program finished

            output_name_label.config(text=first_last)
            output_phone_number_label.config(text=phone)
            output_address_label.config(text=address)

    button_db.commit()
    button_db.close()


def edit_button():
    edit_window = Tk()
    edit_window.title("Contact Edit")
    edit_window.configure(background='black')
    edit_window.iconbitmap("blackBox.ico")

    edit_window_db = sqlite3.connect("contacts.db")
    edit_window_conn = edit_window_db.cursor()

    # Functions inside edit button
    def submit_edit():
        submit_button_edit_window = sqlite3.connect("contacts.db")
        submit_c = submit_button_edit_window.cursor()
        for row1 in submit_c.execute("SELECT *, oid FROM contacts"):
            list_records = list(row1)
            first_name = list_records[0]
            last_name = list_records[1]

            first_last = first_name + " " + last_name

            main_list = rFrame_listbox.get(ANCHOR)

            if main_list == first_last:
                id_number = list_records[4]
                too_str = str(id_number)
                print(id_number)

                name = edit_name_input.get()
                last = edit_last_input.get()
                new_number = edit_phone_input.get()
                new_address = edit_address_input.get()

                submit_c.execute("UPDATE contacts SET first_name = ? WHERE oid = ? ", (name, id_number))
                submit_c.execute("UPDATE contacts SET last_name = ? WHERE oid = ? ", (last, id_number))
                submit_c.execute("UPDATE contacts SET phone = ? WHERE oid = ? ", (new_number, id_number))
                submit_c.execute("UPDATE contacts SET address = ? WHERE oid = ? ", (new_address, id_number))

        submit_button_edit_window.commit()
        submit_button_edit_window.close()

        edit_name_input.delete(0, END)
        edit_last_input.delete(0, END)
        edit_phone_input.delete(0, END)
        edit_address_input.delete(0, END)
        update_edit()

    def quit_window():
        """Used .destroy() at first, but it gives me an error, so I decided to disable the close button
                and have it there just for looks"""
        edit_window.quit()

    # Edit Name Labels:
    edit_name_label = Label(edit_window, text='First Name:', bg='black', fg='cyan', font="Arial, 15")
    edit_name_label.grid(row=0, column=0, padx=(35, 0))

    edit_last_label = Label(edit_window, text='Last Name:', bg='black', fg='cyan', font="Arial, 15")
    edit_last_label.grid(row=0, column=1, padx=(35, 0))

    edit_phone_label = Label(edit_window, text='Phone:', bg='black', fg='cyan', font="Arial, 15")
    edit_phone_label.grid(row=0, column=2, padx=(35, 0))

    edit_address_label = Label(edit_window, text='Address:', bg='black', fg='cyan', font="Arial, 15")
    edit_address_label.grid(row=0, column=3, padx=(35, 35))

    # Edit Input Entries:
    edit_name_input = Entry(edit_window)
    edit_name_input.grid(row=1, column=0, padx=(35, 0))

    edit_last_input = Entry(edit_window)
    edit_last_input.grid(row=1, column=1, padx=(35, 0))

    edit_phone_input = Entry(edit_window)
    edit_phone_input.grid(row=1, column=2, padx=(35, 0))

    edit_address_input = Entry(edit_window)
    edit_address_input.grid(row=1, column=3, padx=(35, 35))

    submit_button = Button(edit_window, text="Submit", bg='black', fg='cyan', font='Arial, 15', command=submit_edit)
    submit_button.grid(row=2, column=1, padx=(0, 0), pady=(20, 0), ipadx=30)

    close_button = Button(edit_window, text="Close", bg='black', fg='cyan', font='Arial, 15', command=quit_window)
    close_button.grid(row=2, column=2, padx=(90, 0), pady=(20, 0), ipadx=30)

    for row1 in edit_window_conn.execute("SELECT *, oid FROM contacts"):
        list_records = list(row1)
        first_name = list_records[0]
        last_name = list_records[1]
        phone = list_records[2]
        address = list_records[3]
        id_number = list_records[4]

        first_last = first_name + " " + last_name + " " + phone + " " + address + " " + str(id_number)
        f_l = first_name + " " + last_name
        main_str = str(id_number)

        main_list = rFrame_listbox.get(ANCHOR)
        if main_list == f_l:
            for row_edit in edit_window_conn.execute("SELECT * FROM contacts WHERE oid = " + main_str):
                print(row_edit)
                edit_first_name = row_edit[0]
                edit_last_name = row_edit[1]
                edit_phone = row_edit[2]
                edit_address = row_edit[3]
                edit_name_input.insert(0, edit_first_name)
                edit_last_input.insert(0, edit_last_name)
                edit_phone_input.insert(0, edit_phone)
                edit_address_input.insert(0, edit_address)

    edit_window.mainloop()


def delete_button():
    del_db = sqlite3.connect("contacts.db")
    del_conn = del_db.cursor()
    for row1 in del_conn.execute("SELECT *, oid FROM contacts"):
        list_records = list(row1)
        first_name = list_records[0]
        last_name = list_records[1]

        first_last = first_name + " " + last_name

        main_list = rFrame_listbox.get(ANCHOR)

        if main_list == first_last:
            id_number = list_records[4]
            too_str = str(id_number)
            print(id_number)
            conn.execute("DELETE from contacts WHERE oid = " + too_str)

            id_num = str(list_records[4])
            print(first_last + " " + "ID Number: " + id_num)   # TODO remove after program finished
    rFrame_listbox.delete(ANCHOR)
    db.commit()


# Left frame stuff
leftFrame = Frame(mainWindow, height=300, width=300, background='black')
leftFrame.grid(row=0, column=0)

# Contacts GUI
contacts_gui_label = Label(leftFrame, text='Contacts Database', foreground='cyan', background='black', font='Arial, 30')
contacts_gui_label.grid(row=0, column=0, pady=5)

# First name label and input***********************
first_name_label = Label(leftFrame, text='First Name:', foreground='cyan', background='black', font='Arial, 15')
first_name_label.grid(row=1, column=0, sticky=W, pady=3, padx=5)

first_name_input = Entry(leftFrame, font='Arial, 10')
first_name_input.grid(row=2, column=0, sticky=W, pady=3, padx=8)

# Last name label and input***********************
last_name_label = Label(leftFrame, text='Last Name:', foreground='cyan', background='black', font='Arial, 15')
last_name_label.grid(row=3, column=0, sticky=W, pady=3, padx=5)

last_name_input = Entry(leftFrame, font='Arial, 10')
last_name_input.grid(row=4, column=0, sticky=W, pady=3, padx=8)

# Phone number label and input***********************
phone_number_label = Label(leftFrame, text='Phone Number:', foreground='cyan', background='black', font='Arial, 15')
phone_number_label.grid(row=5, column=0, sticky=W, pady=3, padx=5)

phone_number_input = Entry(leftFrame, font='Arial, 10')
phone_number_input.grid(row=6, column=0, sticky=W, pady=3, padx=8)

# Address label and input***********************
address_label = Label(leftFrame, text='Address:', foreground='cyan', background='black', font='Arial, 15')
address_label.grid(row=7, column=0, sticky=W, pady=3, padx=5)

address_input = Entry(leftFrame, font='Arial, 10')
address_input.grid(row=8, column=0, sticky=W, pady=3, padx=8)

# Submit button, left frame
left_frame_submit_button = Button(leftFrame, text='SUBMIT', foreground='cyan', background='black', font='Arial, 15',
                                  command=left_frame_button)
left_frame_submit_button.grid(row=9, column=0, sticky=W, pady=8, padx=8)

# Left frame info label
info_label = Label(leftFrame, text='This GUI adds your contacts to a local\ndatabase where you can look up\nsearch and'
                                   ' delete those contacts', foreground='cyan', background='black', font='Arial, 15')
info_label.grid(row=10, column=0, sticky=W, padx=5, pady=5)


# Right frame stuff ***************************************************************************
rightFrame = Frame(mainWindow, height=300, width=300, background='black')
rightFrame.grid(row=0, column=1)

# Right frame list box scroll-bar **********************************************************************
rFrame_scrollBar = Scrollbar(rightFrame, orient=VERTICAL)

# Right frame list box ***************************************************************************
rFrame_listbox = Listbox(rightFrame, height=15, width=50, bg='lightgrey', yscrollcommand=rFrame_scrollBar.set)
rFrame_listbox.grid(row=0, column=0, padx=5, pady=5)

# configure scrollbar
rFrame_scrollBar.config(command=rFrame_listbox.yview)
rFrame_scrollBar.grid(row=0, column=2, sticky="NS", pady=(0, 5))

db = sqlite3.connect("contacts.db")
conn = db.cursor()

row = ''
for row in conn.execute("SELECT * FROM contacts"):
    list_convert = list(row)
    l_first_name = list_convert[0]
    l_last_name = list_convert[1]
    justName = l_first_name + " " + l_last_name
    rFrame_listbox.insert(0, justName)

# Right frame submit button ***************************************************************************
right_frame_submit_button = Button(rightFrame, text='SUBMIT!', background='black', foreground='cyan',
                                   font='Arial, 15', command=submit_button)
right_frame_submit_button.grid(row=1, column=0, sticky=W, padx=5, pady=5)


# Right frame edit button ***************************************************************************
right_frame_edit_button = Button(rightFrame, text='EDIT!', background='black', foreground='cyan',
                                 font='Arial, 15', command=edit_button)
right_frame_edit_button.grid(row=1, column=0, pady=5)


# Right frame delete button ***************************************************************************
right_frame_delete_button = Button(rightFrame, text='DELETE!', background='black', foreground='cyan',
                                   font='Arial, 15', command=delete_button)
right_frame_delete_button.grid(row=1, column=0, sticky=E, padx=5, pady=5)


# Right frame name label ***************************************************************************
output_name_label = Label(rightFrame, text='Contact Name:', background='black', foreground='cyan', font='Arial, 15')
output_name_label.grid(row=2, column=0)

# Right frame phone number label ***************************************************************************
output_phone_number_label = Label(rightFrame, text='000-000-0000', background='black', foreground='cyan',
                                  font='Arial, 15')
output_phone_number_label.grid(row=3, column=0)

# Right frame name label ***************************************************************************
output_address_label = Label(rightFrame, text='123 Main Street Dr, 00000', background='black', foreground='cyan',
                             font='Arial, 15')
output_address_label.grid(row=4, column=0)

mainWindow.mainloop()
