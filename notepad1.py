from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import speech_recognition as sr
import tkinter.font


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
##########################################################################################################
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
##########################################################################################################
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")

    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
##########################################################################################################
def find1():

    def find():
        word = find_input.get()
        TextArea.tag_remove('match','1.0',END)
        matches = 0
        if word :
            start_pos = '1.0'
            while True :
                start_pos = TextArea.search(word,start_pos,stopindex=END)
                if(not start_pos):
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                TextArea.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos=end_pos
                TextArea.tag_config('match',foreground='red',background='')

    def replace():
            word = find_input.get()
            replace_text = replace_input.get()
            content = TextArea.get(1.0, END)
            new_content = content.replace(word, replace_text)
            TextArea.delete(1.0, END)
            TextArea.insert(1.0, new_content)

    find_dialogue = Toplevel()
    photo = PhotoImage(file="download.png")
    find_dialogue.iconphoto(False, photo)
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.resizable(0, 0)

    ## frame
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find :')
    text_replace_label = ttk.Label(find_frame, text='Replace')

    ##entry boxes
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## Button
    find_button = Button(find_frame, text='Find', command=find)
    replace_button = Button(find_frame, text='Replace', command=replace)

    ##label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ##entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ##button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

##########################################################################################################
def quitApp():
    root.destroy()
##########################################################################################################
def cut():
    TextArea.event_generate(("<Control-x>"))
##########################################################################################################
def copy():
    TextArea.event_generate(("<Control-c>"))
##########################################################################################################
def paste():
    TextArea.event_generate(("<Control-v>"))
##########################################################################################################
def about():
   messagebox.showinfo("Notepad", "1.after clicking on CLICK ME FOR VOICE TO TEXT CONVERSION "
                                  "make sure you wait for a sec. and then start speaking. \n\n"
                                  "2.it will take some time beacuse untill you speak the program will listen you "
                                  "and it will only stop listing you when it got noting to "
                                  "listen means when you stop speaking.\n\n"
                                  "3.make sure you are connected with internet to avoid unaccepted errors.\n\n"
                                  "4.if you get any issue or any problem regarding this fell free to contact us on : \n"
                                  "shivam4ever.ss@gmail.com")
##########################################################################################################
def update():
    global current_font_family
    global current_font_size
    current_font_family = font_family.get()
    current_font_size = size_var.get()
    TextArea.config(font=(current_font_family,current_font_size))
##########################################################################################################
def speech():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print('I\'M LISTENING...')
        audio = rec.listen(source, phrase_time_limit=5)
    try:
        text = rec.recognize_google(audio, language='en-US')
        return TextArea.insert(1.0 , text)
    except:
        messagebox.showinfo("ERROR MESSSAGE",
                            "SOME UNCONDITIONAL ERROR OCCURED WE ARE UNABLE TO CONTACT "
                            "RECOGNIZE GOOGLE \n KINDLY CHECK YOUR ONLINE CONNECTION. \n\n\n"
                            "NOTE : TO RUN OUR VOICE RECOGNATION YOUR SYSTEM MUST CONNECTED WITH INTERNET")
##########################################################################################################
def change_bold():
    text_property=font.Font(font=TextArea['font'])
##upper line gives a dictionary whose attributes we are changing
    if text_property.actual()['weight']=='normal' :
        TextArea.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold' :
        TextArea.configure(font=(current_font_family,current_font_size,'normal'))
##########################################################################################################
def change_italic():
    text_property= font.Font(font=TextArea['font'])
##upper line gives a dictionary whose attributes we are changing
    if text_property.actual()['slant']=='roman' :
        TextArea.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic' :
        TextArea.configure(font=(current_font_family,current_font_size,'normal'))
##########################################################################################################
def underline():
    text_property = font.Font(font=TextArea['font'])
    ##upper line gives a dictionary whose attributes we are changing
    if text_property.actual()['underline'] == 0:
        TextArea.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        TextArea.configure(font=(current_font_family, current_font_size, 'normal'))
##########################################################################################################
def align_left():
    text_content = TextArea.get(1.0, 'end')
    TextArea.tag_config('left',justify=LEFT)
    TextArea.delete(1.0,END)
    TextArea.insert(INSERT,text_content,'left')
##########################################################################################################
def align_center():
    text_content = TextArea.get(1.0, 'end')
    TextArea.tag_config('center',justify=CENTER)
    TextArea.delete(1.0,END)
    TextArea.insert(INSERT,text_content,'center')
##########################################################################################################
def align_right():
    text_content = TextArea.get(0.0, 'end')
    TextArea.tag_config('right',justify=RIGHT)
    TextArea.delete(1.0,END)
    TextArea.insert(INSERT,text_content,'right')
##########################################################################################################
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        t0.pack_forget()
        show_toolbar =False

    else:
        TextArea.pack_forget()
        status_bar.pack_forget()
        t0.pack(side=TOP,fill=X)
        TextArea.pack(fill=BOTH,expand =True)
        status_bar.pack(side=BOTTOM)
        show_toolbar = True
##########################################################################################################
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar =False
    else:
        status_bar.pack(side=BOTTOM)
        show_statusbar=True

##########################################################################################################

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("1000x500")
    photo = PhotoImage(file="download.png")
    root.iconphoto(False, photo)

    current_font_family = 'Arial'
    current_font_size = 16

    font_family = StringVar()
    size_var = IntVar()

    t0 = Label(root, bg="black" , borderwidth = 12 )
    t0.pack(side=TOP,fill=X)

    #Add TextArea starts

    TextArea = Text(root)
    file = None
    TextArea.config(font=(current_font_family, current_font_size))
    TextArea.pack(expand=True, fill=BOTH)

    #add textarea ends

    #Adding Scrollbar to Textarea

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    #adding icon button starts
    #for BOLD
    bold_icon = PhotoImage(file='bold.png')
    bold_btn = Button(t0, image=bold_icon)
    bold_btn.grid(row=0, column=1, padx=5)
    bold_btn.configure(command=change_bold)

    #FOR ITALIC
    italic_icon = PhotoImage(file='italic.png')
    italic_btn = Button(t0, image=italic_icon)
    italic_btn.grid(row=0, column=2, padx=5)
    italic_btn.configure(command=change_italic)

    #FOR UNDERLINE
    underline_icon = PhotoImage(file='underline.png')
    underline_btn = Button(t0, image=underline_icon)
    underline_btn.grid(row=0, column=3, padx=5)
    underline_btn.configure(command=underline)

    #FOR ALIGN LEFT
    align_left_icon = PhotoImage(file='left.png')
    align_left_btn = Button(t0, image=align_left_icon, command=align_left)
    align_left_btn.grid(row=0, column=4 , padx=5)

    #FOR ALIGN CENTER
    align_center_icon = PhotoImage(file='center.png')
    align_center_btn = Button(t0, image=align_center_icon, command=align_center)
    align_center_btn.grid( row=0, column=6 , padx=5)

    #FOR ALIGN RIGHT
    align_right_icon = PhotoImage(file="right.png")
    align_right_btn = Button(t0, image=align_right_icon , command=align_right)
    align_right_btn.grid( row=0, column=7 , padx=5)

    #CODE FOR FONT COMBOBOX
    font_tuple = tkinter.font.families()
    font_box = ttk.Combobox(t0, width=30, textvariable=font_family, state='readonly')
    font_box['values'] = font_tuple
    font_box.current(font_tuple.index('Arial'))
    font_box.grid(row = 0 , column = 8 , padx = 10)

    ##CODE FOR FONT size box
    font_size = ttk.Combobox(t0, width=14, textvariable=size_var, state='readonly')
    font_size['values'] = tuple(range(8, 80, 2))
    font_size.current(4)
    font_size.grid(row=0 , column=9 , padx = 10)

    b1 = Button(t0 , text = "OK" ,padx=15, pady=10, command = update).grid(row=0 , column = 10 , padx =10)

    button = Button(t0, text="CLICK ME FOR VOICE TO TEXT CONVERSION", padx=15, pady=10, command=speech)
    button.grid(row=0,column=11)

    #adding icon buttonS ends

    # Lets create a menubar
    MenuBar = Menu(root)

    #filemenu start
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command = openFile)
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)

    #filemenu ends

    # Edit Menu Starts

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label = "Cut" , accelerator="Ctrl+X", command = cut)
    EditMenu.add_command(label = "Copy", command=copy , accelerator = "Ctrl-C")
    EditMenu.add_command(label = "Paste", command=paste , accelerator = "Ctrl-V")
    EditMenu.add_separator()
    EditMenu.add_command(label = "find and replace", command=find1)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    #view menu starts

    ViewMenu = Menu(MenuBar, tearoff=0)
    show_statusbar = BooleanVar()
    show_statusbar.set(True)
    show_toolbar = BooleanVar()
    show_toolbar.set(True)
    ViewMenu.add_checkbutton(label='Tool Bar', onvalue=True, offvalue=0, variable=show_toolbar,
                         compound=LEFT, command=hide_toolbar)
    ViewMenu.add_checkbutton(label='Status Bar', onvalue=1, offvalue=False, variable=show_statusbar,
                         compound=LEFT, command=hide_statusbar)
    MenuBar.add_cascade(label="View", menu=ViewMenu)

    #vies menu ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #our menu bar is created

    # status bar starts

    status_bar = Label(root, text='Status Bar')
    status_bar.pack(side=BOTTOM)
    text_changed = False


    def changed(event=None):
        global text_changed
        if TextArea.edit_modified():  ###checks if any character is added or not
            text_changed = True
            words = len(TextArea.get(1.0, 'end-1c').split())
            ##it even counts new line character so end-1c subtracts one char
            characters = len(TextArea.get(1.0, 'end-1c'))
            status_bar.config(text=f' Words: {words} Characters : {characters}')
        TextArea.edit_modified(False)


    TextArea.bind('<<Modified>>', changed)

    # status bar ends


    root.mainloop()