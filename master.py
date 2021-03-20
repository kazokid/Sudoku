from tkinter import *
import tkinter.messagebox
from tkinter import font
import random
from time import sleep


root = Tk()
root.geometry('1050x620+430+230')
root.resizable(False, False)
root.title('Sudoku')
root.iconbitmap('C:\\Users\\Lovroslov\\Documents\\python\\sudoku\\sudoku_ico.ico')

background_colour = root.cget('bg')
hard_lvls_unsolved = [['X','X','X','X','8','X','X','X','7','X','X','8','X','4','X','9','X','X','X','9','X','6','X','7','X','3','X','X','X','1','X','X','X','X','X','X','X','X','X','4','X','X','X','6','1','7','6','2','X','9','3','8','X','X','X','X','X','7','X','X','X','X','3','X','X','X','X','3','6','1','7','X','X','X','X','9','X','X','4','X','X'],
                      ['X','X','X','X','X','X','X','3','X','8','X','3','X','X','1','5','X','X','4','X','X','8','X','X','X','6','1','X','7','8','X','X','X','X','X','3','X','X','X','X','3','8','X','X','9','3','X','X','2','4','X','6','X','X','X','X','X','X','8','X','X','1','X','2','X','6','9','X','X','X','7','X','X','X','4','X','X','7','X','X','2'],
                      ['X','X','5','8','X','X','X','9','X','X','1','X','5','X','X','X','X','7','4','X','X','X','X','X','8','X','X','X','5','X','6','9','X','X','3','4','X','X','9','X','1','5','X','X','X','3','X','X','X','X','7','X','X','X','X','9','X','X','X','1','X','X','2','8','X','3','X','4','X','9','X','1','X','X','X','X','X','X','X','X','6'],
                      ['X','X','X','7','X','X','X','3','4','X','X','X','3','X','9','6','X','1','X','X','X','X','X','1','9','2','X','X','3','4','X','X','X','X','1','6','X','X','X','X','X','5','X','X','X','8','2','X','9','X','X','X','X','X','X','8','X','X','X','3','X','X','X','X','X','X','6','X','X','X','9','X','6','X','9','X','X','X','X','X','5'],
                      ['X','X','X','9','X','X','8','7','X','X','X','9','X','7','X','X','X','X','5','X','2','X','X','X','4','X','X','X','X','X','X','2','X','X','7','X','4','6','X','X','X','X','8','X','X','3','X','X','X','7','6','X','5','X','X','X','X','X','6','X','X','X','9','X','9','X','X','X','5','3','X','X','X','7','X','2','X','1','X','X','3','X','X'],
                      ['X','X','2','8','X','X','X','1','3','X','X','X','X','X','4','X','X','X','5','3','X','X','X','X','X','X','X','X','X','6','X','3','2','X','X','X','X','9','X','X','X','X','X','X','X','X','4','X','X','5','X','X','X','7','9','X','X','X','X','X','6','X','X','X','6','X','X','8','X','X','3','X','X','X','X','X','X','3','1','5','7']]
hard_lvls_solved = [['1','5','3','2','8','9','6','4','7','6','7','8','3','4','5','9','1','2','2','9','4','6','1','7','5','3','8','3','4','1','5','6','8','7','2','9','9','8','5','4','7','2','3','6','1','7','6','2','1','9','3','8','5','4','8','1','6','7','5','4','2','9','3','4','2','9','8','3','6','1','7','5','5','3','7','9','2','1','4','8','6'],
                    ['1','6','7','4','2','5','9','3','8','8','9','3','6','7','1','5','2','4','4','2','5','8','9','3','7','6','1','9','7','8','1','5','6','2','4','3','6','4','2','7','3','8','1','5','9','3','5','1','2','4','9','6','8','7','7','3','9','5','8','2','4','1','6','2','8','6','9','1','4','3','7','5','5','1','4','3','6','7','8','9','2'],
                    ['2','6','5','8','7','4','1','9','3','9','1','8','5','3','2','6','4','7','4','3','7','1','6','9','8','2','5','1','5','2','6','9','8','7','3','4','7','4','9','3','1','5','2','6','8','3','8','6','4','2','7','5','1','9','6','9','4','7','5','1','3','8','2','8','7','3','2','4','6','9','5','1','5','2','1','9','8','3','7','4','6'],
                    ['5','9','1','7','6','2','8','3','4','2','7','8','3','4','9','6','5','1','4','6','3','8','5','1','9','2','7','9','3','4','2','8','7','5','1','6','7','1','6','4','3','5','2','8','9','8','2','5','9','1','6','7','4','3','1','8','7','5','9','3','4','6','2','3','5','2','6','7','4','1','9','8','6','4','9','1','2','8','3','7','5'],
                    ['1','6','3','9','4','2','8','7','5','4','8','9','5','7','1','2','3','6','5','7','2','8','3','6','4','1','9','8','9','1','3','2','5','7','6','4','6','5','7','4','1','8','9','2','3','2','3','4','7','6','9','5','8','1','3','4','5','6','8','7','1','9','2','9','1','8','2','5','3','6','4','7','7','2','6','1','9','4','3','5','8'],
                    ['6','7','2','8','9','5','4','1','3','1','8','9','3','7','4','5','6','2','5','3','4','2','1','6','7','9','8','8','5','6','7','3','2','9','4','1','2','9','7','1','4','8','3','5','6','3','4','1','6','5','9','8','2','7','9','1','3','5','2','7','6','8','4','7','6','5','4','8','1','2','3','9','4','2','8','9','6','3','1','7','5']]
medium_lvls_unsolved = [['x','8','x','6','x','x','x','x','5','3','x','6','x','x','7','9','8','x','x','4','x','x','x','x','x','1','x','9','x','x','x','5','3','x','x','7','x','x','x','1','x','2','x','x','9','x','6','x','x','x','4','1','x','x','x','1','2','x','9','x','3','x','x','x','7','x','x','2','8','x','x','x','x','x','5','x','x','x','4','6','x'],
                        ['4','2','X','1','X','X','X','5','X','9','X','3','X','X','6','X','7','X','X','7','6','X','X','X','8','3','X','X','X','7','X','X','9','X','8','X','X','X','5','X','7','X','X','X','X','3','9','X','X','X','5','6','X','7','7','8','X','X','9','X','5','X','X','X','3','X','X','2','X','7','X','X','1','X','4','7','X','3','2','9','X'],
                        ['9','8','7','1','X','X','6','X','5','X','X','X','6','X','X','9','X','X','4','X','X','X','X','9','X','X','X','6','X','X','5','2','7','8','1','X','X','2','X','X','X','8','X','X','X','7','5','X','9','X','X','4','X','X','X','6','5','X','X','X','X','3','4','X','X','X','X','X','X','2','X','X','X','9','X','7','6','X','X','5','8'],
                        ['X','X','6','9','3','X','5','8','X','X','X','X','X','X','X','X','X','1','X','4','2','8','X','6','X','X','X','X','1','5','X','X','X','7','X','9','X','X','7','X','X','X','X','X','X','X','X','X','6','X','5','8','X','X','X','X','8','3','X','X','X','X','7','3','6','X','X','X','X','1','X','8','X','X','X','4','8','9','2','3','X'],
                        ['9','4','1','3','X','X','X','X','X','2','X','X','X','X','X','X','X','8','X','5','X','X','X','4','X','2','X','X','X','X','X','9','X','X','X','X','8','2','9','X','X','X','X','7','X','X','1','3','X','X','6','X','X','9','X','X','X','X','X','X','2','8','X','X','X','X','1','6','X','X','X','7','X','X','5','9','8','X','1','X','4'],
                        ['X','7','X','X','X','X','X','3','8','X','X','X','X','X','3','X','X','9','8','X','X','X','7','9','X','5','2','5','1','9','3','X','X','X','6','X','6','8','4','1','X','7','X','X','X','X','X','2','9','X','X','X','X','X','X','4','X','X','1','5','X','X','X','X','X','6','X','X','2','X','X','4','X','X','X','X','X','X','X','2','6']]
medium_lvls_solved = [['1','8','7','6','4','9','2','3','5','3','5','6','2','1','7','9','8','4','2','4','9','3','8','5','7','1','6','9','2','1','8','5','3','6','4','7','7','3','4','1','6','2','8','5','9','5','6','8','9','7','4','1','2','3','4','1','2','5','9','6','3','7','8','6','7','3','4','2','8','5','9','1','8','9','5','7','3','1','4','6','2'],
                      ['4','2','8','1','3','7','9','5','6','9','1','3','8','5','6','4','7','2','5','7','6','9','4','2','8','3','1','2','4','7','6','1','9','3','8','5','8','6','5','3','7','4','1','2','9','3','9','1','2','8','5','6','4','7','7','8','2','4','9','1','5','6','3','6','3','9','5','2','8','7','1','4','1','5','4','7','6','3','2','9','8'],
                      ['9','8','7','1','3','2','6','4','5','5','3','2','6','7','4','9','8','1','4','1','6','8','5','9','3','7','2','6','4','3','5','2','7','8','1','9','1','2','9','3','4','8','5','6','7','7','5','8','9','1','6','4','2','3','8','5','6','2','9','1','7','3','4','3','7','1','4','8','5','2','9','6','2','9','4','7','6','3','1','5','8'],
                      ['1','7','6','9','3','2','5','8','4','9','8','3','7','5','4','6','2','1','5','4','2','8','1','6','9','8','3','8','1','5','2','4','3','7','6','9','6','2','7','1','9','8','3','4','5','4','3','9','6','7','5','8','1','2','2','9','8','3','6','1','4','5','7','3','6','4','5','2','7','1','9','8','7','5','1','4','8','9','2','3','6'],
                      ['9','4','1','3','2','8','7','5','6','2','3','7','6','5','9','4','1','8','6','5','8','7','1','4','9','2','3','7','6','4','8','9','1','5','3','2','8','2','9','5','4','3','6','7','1','5','1','3','2','7','6','8','4','9','1','9','6','4','3','7','2','8','5','4','8','2','1','6','5','3','9','7','3','7','5','9','8','2','1','6','4'],
                      ['9','7','5','2','6','1','4','3','8','4','2','1','5','8','3','6','7','9','8','6','3','4','7','9','1','5','2','5','1','9','3','4','8','2','6','7','6','8','4','1','2','7','3','9','5','7','3','2','9','5','6','8','4','1','2','4','7','6','1','5','9','8','3','3','5','6','8','9','2','7','1','4','1','9','8','7','3','4','5','2','6']]
easy_lvls_unsolved = [['3','4','1','x','x','2','x','x','x','x','2','x','x','1','4','3'],
                      ['1','x','x','x','x','x','x','4','x','x','2','x','x','3','x','x'],
                      ['X','X','X','X','1','X','X','X','X','X','3','X','X','2','X','4'],
                      ['X','X','1','X','3','X','X','X','4','X','X','X','X','X','2','X'],
                      ['4','X','X','X','X','X','3','X','X','X','1','X','3','X','X','X'],
                      ['X','X','3','1','X','X','X','X','X','X','X','X','4','X','2','X']]
easy_lvls_solved = [['3','4','1','2','1','2','3','4','4','3','2','1','2','1','4','3'],
                    ['1','4','3','2','3','2','1','4','4','1','2','3','2','3','4','1'],
                    ['2','3','4','1','1','4','2','3','4','1','3','2','3','2','1','4'],
                    ['2','4','1','3','3','1','4','2','4','2','3','1','1','3','2','4'],
                    ['4','3','2','1','1','2','3','4','2','4','1','3','3','1','4','2'],
                    ['2','4','3','1','1','3','4','2','3','2','1','4','4','1','2','3']]

text_font = font.Font(family = 'Fixedsys', size = 15)
number_font = font.Font(family = 'Fixedsys', size = 25)


zvj_0 = PhotoImage (file = 'zvjezdice_0_1.png')
zvj_1 = PhotoImage (file = 'zvjezdice_1_1.png')
zvj_2 = PhotoImage (file = 'zvjezdice_2_1.png')
zvj_3 = PhotoImage (file = 'zvjezdice_3_1.png')
locked = PhotoImage(file = 'lvl_locked.png')

slikica_0 = PhotoImage (file = 'zvjezde_0.png')
slikica_1 = PhotoImage (file = 'zvjezde_1.png')
slikica_2 = PhotoImage (file = 'zvjezde_2.png')
slikica_3 = PhotoImage (file = 'zvjezde_3.png')


dat = open ('provjera.txt')
l = dat.readline()
lista_provjera = l.split()
l = dat.readline()
lista_imena = l.split()
dat.close()


def clear():
    L = root.place_slaves()
    for i in range (len(L)):
        L[i].destroy()


def show_4sudoku_grid():
    clear()
    global pozadina
    global pozadina_label
    pozadina = PhotoImage(file = 'sudoku_4.png')
    pozadina_label = Label(root, image = pozadina, width = 504, height = 503)
    pozadina_label.place(relx = 0.5, rely = 0.45, anchor = 'center')
    global lista_entrya
    lista_entrya = []
    for i in range (16):
        lista_entrya.append('e'+ str(i))
    brx = 0.35
    bry = 0.348
    br = 0
    for y in range(4):
        for x in range(4):
            lista_entrya[br] = Entry(pozadina_label, bg = background_colour, bd = 0,
                                     font = "Times 26", justify = 'center')
            lista_entrya[br].place(width = 46, height = 45, relx = brx, rely = bry, anchor = 'center')
            if x == 1:
                brx += 0.105
            else:
                brx += 0.095
            br += 1
        brx = 0.35
        if y == 1:
            bry += 0.0995
        elif y == 2:
            bry += 0.1
        else:
            bry += 0.0965


def show_9sudoku_grid():
    clear()
    global pozadina
    global pozadina_label
    global lista_entrya
    pozadina = PhotoImage(file = 'sudoku_9.png')
    pozadina_label = Label(root, image = pozadina, width = 504, height = 503)
    pozadina_label.place(relx = 0.5, rely = 0.475, anchor = 'center')
    lista_entrya = []
    for i in range(1, 82):
        lista_entrya.append('e' + str(i))
    bry = 0.011
    brx = 0.0125
    br = 0
    for y in range(9):
        for x in range(9):
            lista_entrya[br] = Entry(pozadina_label, bg =background_colour, bd = 0,
                                     font = "Times 26", justify = 'center')
            lista_entrya[br].place(width = 50, height = 50, relx = brx, rely = bry)
            if x == 2:
                brx += 0.11
            elif x == 5:
                brx += 0.115
            else:
                brx += 0.109
            br += 1
        brx = 0.0125
        if y == 2:
            bry += 0.11
        elif y == 5:
            bry += 0.115
        else:
            bry += 0.109


def load_info(p):
    global ime_datoteke
    global brprof
    brprof = p
    if p == 0:
        ime_datoteke = 'korisnik_1.txt'
    elif p == 1:
        ime_datoteke = 'korisnik_2.txt'
    elif p == 2:
        ime_datoteke = 'korisnik_3.txt'
    elif p == 3:
        ime_datoteke = 'korisnik_4.txt'

    global zvjezdice_easy
    global zvjezdice_hard
    global zvjezdice_medium
    global otkljucani_lvls_easy
    global otkljucani_lvls_medium
    global otkljucani_lvls_hard
    global timer_v
    dat = open(ime_datoteke)
    l = dat.readline()
    zvjezdice_easy = l.split()
    l = dat.readline()
    zvjezdice_medium = l.split()
    l = dat.readline()
    zvjezdice_hard = l.split()
    l = dat.readline()
    otkljucani_lvls_easy = l.split()
    l = dat.readline()
    otkljucani_lvls_medium = l.split()
    l = dat.readline()
    otkljucani_lvls_hard = l.split()
    l = dat.readline()
    timer_v = int(l)
    dat.close()
    show_first_screen()


def save_name(l):
    ime_profila = name_e.get()
    if len(ime_profila) > 10:
        pazi['text'] = 'Max number of characters is 10'
    elif len(ime_profila) == 0:
        pazi['text'] = 'Please input a name'
    elif len(ime_profila) <= 10:
        lista_imena[l] = ime_profila
        lista_provjera[l] = 'True'
        load_info(l)


def customize_profile(l):
    clear()
    global pazi
    pazi = Label (root, text = '', font = 'Fixedsys 10', bd = 0, bg = background_colour)
    pazi.place(relx = 0.5, rely = 0.35, anchor = 'center')
    enter_name = Label (root, text = 'Enter your name:', font = text_font)
    enter_name.place (relx = 0.51, rely = 0.45, anchor = 'e')
    global name_e
    name_e = Entry (root, width = 10, font = text_font, bg = 'red')
    name_e.place(relx = 0.59, rely = 0.45,width = 150,  anchor = 'center')
    global save_pic
    save_pic = PhotoImage (file = 'save.png')
    save_b = Button (root, command = lambda : save_name(l), image = save_pic, bd = 0)
    save_b.place(relx = 0.68, rely = 0.6, anchor = 'e')
    global cancel_pic
    cancel_pic = PhotoImage (file = 'cancel.png')
    cancel_b = Button(root, command = select_profile, image = cancel_pic, bd = 0)
    cancel_b.place(relx = 0.47, rely = 0.6, anchor = 'e')


def select_profile():
    clear()
    global profil1_b
    global create_new
    global profil_s_imenom
    profil_s_imenom = PhotoImage (file = 'profil_s_imenom.png')
    create_new = PhotoImage (file = 'change_profile.png')
    profil1_b = Button (root, font = text_font, bd = 0, command = lambda: customize_profile(0), image = create_new)
    profil1_b.place(relx = 0.35, rely = 0.4, anchor = 'center')
    global profil2_b
    profil2_b = Button (root, font = text_font, bd = 0, command = lambda: customize_profile(1), image = create_new)
    profil2_b.place(relx = 0.65, rely = 0.4, anchor = 'center')
    global profil3_b
    profil3_b = Button (root, font = text_font, bd = 0, command = lambda: customize_profile(2), image = create_new)
    profil3_b.place(relx = 0.35, rely = 0.6, anchor = 'center')
    global profil4_b
    profil4_b = Button (root, font = text_font, bd = 0, command = lambda: customize_profile(3), image = create_new)
    profil4_b.place(relx = 0.65, rely = 0.6, anchor = 'center')
    global lista_profila
    lista_profila = [profil1_b,profil2_b, profil3_b, profil4_b]

    for i in range (4):
        if lista_provjera[i] == 'True':
            profil = lista_profila[i]
            if i ==0:
                profil['command'] = lambda: load_info(0)
            elif i == 1:
                profil['command'] = lambda:load_info(1)
            elif i == 2:
                profil['command'] = lambda:load_info(2)
            elif i == 3:
                profil['command'] = lambda:load_info(3)
            profil['image'] = profil_s_imenom
            profil['text'] = lista_imena[i]
            profil['compound'] = 'center'


def show_first_screen():
    clear()
    global slika_naslova
    slika_naslova = PhotoImage(file = 'sudoku_title 1.png')
    naslov_label = Label(root, image = slika_naslova, bg = background_colour, borderwidth = 0)
    naslov_label.place(relx = 0.5, rely = 0.20, relwidth = 0.8, relheight = 0.4 ,anchor = 'center')
    global htp
    htp = PhotoImage(file = 'how to play 5.png')
    how_to_play_b = Button(root, command = how_to_play, image = htp, bd = 0)
    how_to_play_b.place(relx = 0.5, rely = 0.47, anchor = 'center')
    global sd
    sd = PhotoImage (file = 'select difficulty 2.png')
    select_diff = Button(root, command = select_difficulty, image = sd, bd = 0)
    select_diff.place(relx = 0.5, rely = 0.58, anchor = 'center')
    global qi
    qi = PhotoImage (file = 'select_profile.png')
    profile = Button(root, image = qi, command = select_profile , bd = 0)
    profile.place(relx = 0.5, rely = 0.69, anchor = 'center')
    profile.bind('<Button-1>', save)
    global quit_i
    quit_i = PhotoImage(file = 'quit_real.png')
    quit = Button (root,image = quit_i , command = lambda: root.destroy(), bd = 0)
    quit.place(relx = 0.386, rely = 0.803, anchor = 'center')
    global options_i
    options_i = PhotoImage(file = 'options_real_1.png')
    options = Button(root, image = options_i, command = show_options, bd = 0)
    options.place(relx = 0.6145, rely = 0.803, anchor = 'center')
    global aktivni
    aktivni = PhotoImage (file = 'aktivni_p.png')
    profil = Label (root, bd =0, image = aktivni, text = lista_imena[brprof], compound = 'center', font = 'Fixedsys 20')
    profil.place(rely = 0.53 , relx = 0.15, anchor = 'center')


def change_profile_name():
    clear()
    global pazi
    pazi = Label(root, text = '', font = 'Fixedsys 10', bd = 0, bg = background_colour)
    pazi.place(relx = 0.5, rely = 0.35, anchor = 'center')
    enter_name = Label(root, text = 'Enter your name:', font = text_font)
    enter_name.place(relx = 0.51, rely = 0.45, anchor = 'e')
    global name_e
    name_e = Entry(root, width = 10, font = text_font, bg = 'red')
    name_e.place(relx = 0.59, rely = 0.45, width = 150, anchor = 'center')
    global save_pic
    save_pic = PhotoImage(file = 'save.png')
    save_b = Button(root, command = lambda:save_name(brprof), image = save_pic, bd = 0)
    save_b.place(relx = 0.68, rely = 0.6, anchor = 'e')
    global cancel_pic
    cancel_pic = PhotoImage(file = 'cancel.png')
    cancel_b = Button(root, command = show_options, image = cancel_pic, bd = 0)
    cancel_b.place(relx = 0.47, rely = 0.6, anchor = 'e')


def change_timer_v(h):
    global timer_v
    if h == 1:
        timer_v = 1
    elif h == 0:
        timer_v = 0

def show_options():
    clear()
    global change_pic
    change_pic = PhotoImage (file = 'change_name.png')
    change_name = Button (root,image = change_pic, command = change_profile_name, bd = 0)
    change_name.place(relx = 0.35, rely = 0.3, anchor = 'w')
    global timer_pic
    global pozadina_pic
    pozadina_pic = PhotoImage (file = 'pozadina.png')
    timer_pic = PhotoImage (file = 'show_timer.png')
    select_timer = Label (root,image = timer_pic, bd = 0, font = text_font)
    select_timer.place (relx = 0.5, rely = 0.4, anchor = 'center')
    tim1 = Radiobutton (root, text = 'Yes', variable = timer_v, value = 1, font = text_font, bg = '#a81015', activebackground = '#a81015', command = lambda: change_timer_v(1))
    tim2 = Radiobutton(root, text = 'No', variable = timer_v, value = 0, font = text_font, bg = '#a81015', activebackground = '#a81015', command = lambda: change_timer_v(0))
    tim1.place(relx = 0.595, rely =0.4, anchor = 'w')
    tim2.place(relx = 0.65, rely = 0.4, anchor = 'w')
    global back
    global back_p
    back_p = PhotoImage(file = 'back_lvls.png')
    back = Button(root, command = show_first_screen, image = back_p, bd = 0)
    back.place(relx = 0.298, rely = 0.75, anchor = 'w')


def how_to_play():
    clear()
    pravila = Text (root, font = text_font, bg = background_colour, bd = 0)
    pravila.insert(INSERT, '3X3 SUDOKU\n\n The objective is to fill out a 3x3 grid so that each column, each row, and each of the four 2x2 boxes contain the digits from 1 to 4.\n\n')
    pravila.insert(INSERT, '9X9 SUDOKU\n\n The objective is to fill out a 9x9 grid so that each column, each row, and each of the nine 3x3 boxes contain the digits from 1 to 9.\n\n')
    pravila.insert(INSERT, 'PRO tip\n\n If numbers dissapear while solving, minimize the window to refresh it.')
    pravila.config(state = 'disabled')
    pravila.place (relx = 0.5, rely = 0.4, height = 300, anchor = 'center')
    global back
    global back_p
    back_p = PhotoImage (file = 'back_lvls.png')
    back = Button (root, command = show_first_screen, image = back_p, bd = 0)
    back.place (relx = 0.191, rely = 0.75, anchor = 'center')


def select_difficulty():
    clear()
    global easy_b
    global easy_p
    easy_p = PhotoImage (file = 'easy.png')
    easy_b = Button (root, image = easy_p, command = show_easy_lvls, bd = 0)
    easy_b.place (relx = 0.31, rely = 0.45, anchor = 'center')
    global medium_b
    global medium_p
    medium_p = PhotoImage(file = 'medium.png')
    medium_b = Button (root, image = medium_p, command = show_medium_lvls, bd = 0)
    medium_b.place (relx = 0.5, rely = 0.45, anchor = 'center')
    global hard_b
    global hard_p
    hard_p = PhotoImage (file = 'hard.png')
    hard_b = Button (root, image = hard_p, command = show_hard_lvls, bd = 0)
    hard_b.place (relx = 0.69, rely = 0.45, anchor = 'center')
    global back_pic
    back_pic = PhotoImage (file = 'back_lvls.png')

    back = Button (root, command = show_first_screen, image = back_pic, bd = 0)
    back.place(relx = 0.31, rely = 0.78, anchor = 'center')


def change_widget_colour_on_enter(e):
    L = root.place_slaves()
    for i in L:
        if i is e:
            i['background'] = 'light blue'


def change_widget_colour_on_leave(e):
    L = root.place_slaves()
    for i in L:
        if i is e:
            i['background'] = 'SystemButtonFace'


def show_hard_lvls():
    clear()
    global provjera_tezine
    provjera_tezine = 'hard'
    global level1_button
    level1_button = Button(root, text = 'lvl 1', command = lambda:show_lvls_h(0), compound = 'center', font = number_font, bd = 0)
    level1_button.place(relx = 0.31, rely = 0.20, anchor = 'center')
    global level2_button
    level2_button = Button(root, text = 'lvl 2', command = lambda:show_lvls_h(1), compound = 'center', font = number_font, bd = 0)
    level2_button.place(relx = 0.5, rely = 0.20, anchor = 'center')
    global level3_button
    level3_button = Button(root, text = 'lvl 3', command = lambda:show_lvls_h(2), compound = 'center', font = number_font, bd = 0)
    level3_button.place(relx = 0.69, rely = 0.20, anchor = 'center')
    global level4_button
    level4_button = Button(root, text = 'lvl 4', command = lambda:show_lvls_h(3), compound = 'center', font = number_font, bd = 0)
    level4_button.place(relx = 0.31, rely = 0.535, anchor = 'center')
    global level5_button
    level5_button = Button(root, text = 'lvl 5', command = lambda:show_lvls_h(4), compound = 'center', font = number_font, bd = 0)
    level5_button.place(relx = 0.5, rely = 0.535, anchor = 'center')
    global level6_button
    level6_button = Button(root, text = 'lvl 6', command = lambda:show_lvls_h(5), compound = 'center', font = number_font, bd = 0)
    level6_button.place(relx = 0.69, rely = 0.535, anchor = 'center')
    lista_gumbova = [level1_button, level2_button, level3_button, level4_button, level5_button, level6_button]

    global back_b
    global back_lvls
    back_lvls = PhotoImage(file = 'back_lvls.png')
    back_b = Button(root, command = select_difficulty, image = back_lvls, bd = 0)
    back_b.place(relx = 0.31, rely = 0.78, anchor = 'center')


    for i in range (len (zvjezdice_hard)):
        if int(otkljucani_lvls_medium[0]) >= i:
            if zvjezdice_hard[i] == '0':
                lista_gumbova[i]['image'] = zvj_0
            elif zvjezdice_hard[i] == '1':
                lista_gumbova[i]['image'] = zvj_1
            elif zvjezdice_hard[i] == '2':
                lista_gumbova[i]['image'] = zvj_2
            elif zvjezdice_hard[i] == '3':
                lista_gumbova[i]['image'] = zvj_3
        else:
            lista_gumbova[i]['image'] = locked
            lista_gumbova[i]['text'] = ''
            lista_gumbova[i]['state'] = 'disabled'


def show_medium_lvls():
    clear()
    global provjera_tezine
    provjera_tezine = 'medium'
    global level1_button
    level1_button = Button(root, text = 'lvl 1', command = lambda: show_lvls_m(0), compound = 'center', font = number_font, bd = 0)
    level1_button.place(relx = 0.31, rely = 0.20, anchor = 'center')
    global level2_button
    level2_button = Button(root, text = 'lvl 2', command = lambda: show_lvls_m(1), compound = 'center', font = number_font, bd = 0)
    level2_button.place(relx = 0.5, rely = 0.20, anchor = 'center')
    global level3_button
    level3_button = Button(root, text = 'lvl 3', command = lambda: show_lvls_m(2), compound = 'center', font = number_font, bd = 0)
    level3_button.place(relx = 0.69, rely = 0.20, anchor = 'center')
    global level4_button
    level4_button = Button(root, text = 'lvl 4', command = lambda: show_lvls_m(3), compound = 'center', font = number_font, bd = 0)
    level4_button.place(relx = 0.31, rely = 0.535, anchor = 'center')
    global level5_button
    level5_button = Button(root, text = 'lvl 5', command = lambda: show_lvls_m(4), compound = 'center', font = number_font, bd = 0)
    level5_button.place(relx = 0.5, rely = 0.535, anchor = 'center')
    global level6_button
    level6_button = Button(root, text = 'lvl 6', command = lambda: show_lvls_m(5), compound = 'center', font = number_font, bd = 0)
    level6_button.place(relx = 0.69, rely = 0.535, anchor = 'center')

    lista_gumbova = [level1_button, level2_button, level3_button, level4_button, level5_button, level6_button]

    global back_b
    global back_lvls
    back_lvls = PhotoImage(file = 'back_lvls.png')
    back_b = Button(root, command = select_difficulty, image = back_lvls, bd = 0)
    back_b.place(relx = 0.31, rely = 0.78, anchor = 'center')

    for i in range(len(zvjezdice_medium)):
        if int(otkljucani_lvls_medium[0]) >= i:
            if zvjezdice_medium[i] == '0':
                lista_gumbova[i]['image'] = zvj_0
            elif zvjezdice_medium[i] == '1':
                lista_gumbova[i]['image'] = zvj_1
            elif zvjezdice_medium[i] == '2':
                lista_gumbova[i]['image'] = zvj_2
            elif zvjezdice_medium[i] == '3':
                lista_gumbova[i]['image'] = zvj_3
        else:
            lista_gumbova[i]['image'] = locked
            lista_gumbova[i]['text'] = ''
            lista_gumbova[i]['state'] = 'disabled'


def show_easy_lvls():
    clear()
    global provjera_tezine
    provjera_tezine = 'easy'
    global level1_button
    level1_button = Button(root, text = 'lvl 1', command = lambda : show_lvls_e(0), compound = 'center', font = number_font, bd = 0)
    level1_button.place(relx = 0.31, rely = 0.2, anchor = 'center')
    global level2_button
    level2_button = Button(root, text = 'lvl 2', command = lambda : show_lvls_e(1), compound = 'center', font = number_font, bd = 0)
    level2_button.place(relx = 0.5, rely = 0.2, anchor = 'center')
    global level3_button
    level3_button = Button(root, text = 'lvl 3', command = lambda : show_lvls_e(2), compound = 'center', font = number_font, bd = 0)
    level3_button.place(relx = 0.69, rely = 0.2, anchor = 'center')
    global level4_button
    level4_button = Button(root, text = 'lvl 4', command =  lambda : show_lvls_e(3), compound = 'center', font = number_font, bd = 0)
    level4_button.place(relx = 0.31, rely = 0.535, anchor = 'center')
    global level5_button
    level5_button = Button(root, text = 'lvl 5', command =  lambda : show_lvls_e(4), compound = 'center', font = number_font, bd = 0)
    level5_button.place(relx = 0.5, rely = 0.535, anchor = 'center')
    global level6_button
    level6_button = Button(root, text = 'lvl 6', command =  lambda : show_lvls_e(5), compound = 'center', font = number_font, bd = 0)
    level6_button.place(relx = 0.69, rely = 0.535, anchor = 'center')
    lista_gumbova = [level1_button, level2_button, level3_button, level4_button, level5_button, level6_button]

    global back_b
    global back_lvls
    back_lvls = PhotoImage(file = 'back_lvls.png')
    back_b = Button(root, command = select_difficulty, image = back_lvls, bd = 0)
    back_b.place(relx = 0.31, rely = 0.78, anchor = 'center')

    for i in range (len (zvjezdice_easy)):
        if int(otkljucani_lvls_easy[0]) >= i:
            if zvjezdice_easy[i] == '0':
                lista_gumbova[i]['image'] = zvj_0
            elif zvjezdice_easy[i] == '1':
                lista_gumbova[i]['image'] = zvj_1
            elif zvjezdice_easy[i] == '2':
                lista_gumbova[i]['image'] = zvj_2
            elif zvjezdice_easy[i] == '3':
                lista_gumbova[i]['image'] = zvj_3
        else:
            lista_gumbova[i]['image'] = locked
            lista_gumbova[i]['text'] = ''
            lista_gumbova[i]['state'] = 'disabled'


def make_timer():
    if provjera:
        global minute
        global sekunde
        global vrijeme_s
        vrijeme_s = int(sekunde) + int(minute)*60
        if timer_v == 1:
            if sekunde < 10:
                time_l['text'] = str(minute) + ':' + '0'  +str(sekunde)
            else:
                time_l['text'] =str( minute) + ':' + str(sekunde)
        sekunde += 1
        if sekunde == 60:
            minute += 1
            sekunde =  0
        root.after(1000, make_timer)


def promjena_provjere(e):
    global provjera
    provjera = False


def show_lvls_e(n):
    clear()
    show_4sudoku_grid()
    global back_pic
    back_pic = PhotoImage(file = 'back_lvls.png')
    back_b = Button(root, command = show_easy_lvls, image = back_pic, bd = 0)
    back_b.place(relx = 0.31, rely = 0.78, anchor = 'center')
    back_b.bind('<Button-1>', promjena_provjere)
    global check_p
    check_p = PhotoImage(file = 'check_b.png')
    check_b = Button (root, command = check_4sudoku , image= check_p, bd = 0)
    check_b.place (relx = 0.69, rely = 0.78, anchor = 'center')
    global oopsie
    oopsie = Label (root, bd = 0, bg = background_colour, font = 'Fixedsys 15')
    oopsie.place(relx = 0.5, rely = 0.2, anchor = 'center')
    global provjera
    provjera = True
    global time_l
    global time_i
    time_i = PhotoImage(file = 'timer.png')
    time_l = Label (root, image = time_i, font = text_font, compound = 'center', bd = 0)
    if timer_v == 1:
        time_l.place (relx = 0.5, rely = 0.78, anchor = 'center')
    global sekunde
    global minute
    sekunde = 0
    minute = 0
    make_timer()
    brx = 0.35
    bry = 0.348
    global m
    m = n
    global lista_labela
    lista_labela = []
    for i in range (16):
        if easy_lvls_unsolved[n][i] != 'x' and easy_lvls_unsolved[n][i] != 'X':
            label = Button(pozadina_label, text = easy_lvls_unsolved[n][i], bg = background_colour, bd = 0,fg = 'green', font = "Times 26 bold", relief = 'sunken', activebackground = background_colour, activeforeground = 'green')
            label.place(width = 46, height = 46, relx = brx, rely = bry, anchor = 'center')
            if i == 1 or i == 5 or i == 9 or i == 13:
                brx += 0.105
            else:
                brx += 0.095
            if i == 7:
                bry += 0.0995
                brx = 0.35
            elif i == 11:
                bry += 0.1
                brx = 0.35
            elif i == 3:
                brx = 0.35
                bry += 0.0965
        else:
            if i == 1 or i == 5 or i == 9 or i == 13:
                brx += 0.105
            else:
                brx += 0.095
            if i == 7:
                bry += 0.0995
                brx = 0.35
            elif i == 11:
                bry += 0.1
                brx = 0.35
            elif i == 3:
                brx = 0.35
                bry += 0.0965


def show_lvls_m(n):
    clear()
    show_9sudoku_grid()
    global back_pic
    back_pic = PhotoImage(file = 'back_lvls.png')
    back_b = Button(root, command = show_medium_lvls, image = back_pic, bd = 0)
    back_b.bind('<Button-1>', promjena_provjere)
    back_b.place (relx = 0.3, rely = 0.937, anchor = 'center')
    bry = 0.062
    brx = 0.062
    global check_b
    global check_p
    check_p = PhotoImage(file = 'check_b.png')
    check_b = Button (root, image = check_p ,command = lambda: check_9sudoku(1), bd = 0)
    check_b.place (relx = 0.7, rely = 0.937, anchor = 'center')
    global oopsie
    oopsie = Label(root, bd = 0, bg = background_colour, font = 'Fixedsys 15')
    oopsie.place(relx = 0.5, rely = 0.04, anchor = 'center')
    global provjera
    provjera = True
    global time_l
    global time_i
    time_i = PhotoImage(file = 'timer.png')
    time_l = Label(root, text = '', font = 'Times 15', image = time_i, compound = 'center', bd = 0)
    time_l.place(relx = 0.5, rely = 0.937, anchor = 'center')
    global sekunde
    global minute
    sekunde = 0
    minute = 0
    make_timer()

    global m
    m = n
    br = 0
    for y in range(9):
        for x in range(9):
            if medium_lvls_unsolved[n][br] != 'x' and medium_lvls_unsolved[n][br] != 'X':
                label = Label(pozadina_label, text = medium_lvls_unsolved[n][br], bg = background_colour, bd = 0,fg = 'green', font = "Times 26 bold")
                label.place(width = 50, height = 50, relx = brx, rely = bry, anchor = 'center')
                if x == 2:
                    brx += 0.11
                elif x == 5:
                    brx += 0.115
                else:
                    brx += 0.109
                br += 1
            else:
                if x == 2:
                    brx += 0.11
                elif x == 5:
                    brx += 0.115
                else:
                    brx += 0.109
                br += 1
        if y == 2:
            bry += 0.11
            brx = 0.062
        elif y == 5:
            bry += 0.115
            brx = 0.062
        else:
            bry += 0.109
            brx = 0.062


def show_lvls_h(n):
    clear()
    show_9sudoku_grid()
    global back_pic
    back_pic = PhotoImage(file = 'back_lvls.png')
    back_b = Button(root, command = show_hard_lvls, image = back_pic, bd = 0)
    back_b.bind('<Button-1>', promjena_provjere)
    back_b.place(relx = 0.3, rely = 0.937, anchor = 'center')
    bry = 0.062
    brx = 0.062
    global check_b
    global check_p
    check_p = PhotoImage(file = 'check_b.png')
    check_b = Button(root, image = check_p, command = lambda:check_9sudoku(2), bd = 0)
    check_b.place(relx = 0.7, rely = 0.937, anchor = 'center')
    global oopsie
    oopsie = Label(root, bd = 0, bg = background_colour, font = 'Fixedsys 15')
    oopsie.place(relx = 0.5, rely = 0.04, anchor = 'center')
    global provjera
    provjera = True
    global time_l
    global time_i
    time_i = PhotoImage(file = 'timer.png')
    time_l = Label(root, text = '', font = 'Times 15', image = time_i, compound = 'center', bd = 0)
    time_l.place(relx = 0.5, rely = 0.937, anchor = 'center')
    global sekunde
    global minute
    sekunde = 0
    minute = 0
    make_timer()
    global m
    m = n
    br = 0
    for y in range(9):
        for x in range(9):
            if hard_lvls_unsolved[n][br] != 'x' and hard_lvls_unsolved[n][br] != 'X':
                label = Label(pozadina_label, text = hard_lvls_unsolved[n][br], bg = background_colour, bd = 0,
                              fg = 'green', font = "Times 26 bold")
                label.place(width = 50, height = 50, relx = brx, rely = bry, anchor = 'center')
                if x == 2:
                    brx += 0.11
                elif x == 5:
                    brx += 0.115
                else:
                    brx += 0.109
                br += 1
            else:
                if x == 2:
                    brx += 0.11
                elif x == 5:
                    brx += 0.115
                else:
                    brx += 0.109
                br += 1
        if y == 2:
            bry += 0.11
            brx = 0.062
        elif y == 5:
            bry += 0.115
            brx = 0.062
        else:
            bry += 0.109
            brx = 0.062


def pokazi_1():
    zvjezdice['image'] = slikica_1

def pokazi_2_2():
    zvjezdice['image'] = slikica_2

def pokazi_2():
    zvjezdice['image'] = slikica_1
    root.after(500, pokazi_2_2)

def pokazi_3_2():
    zvjezdice['image'] = slikica_3

def pokazi_3():
    pokazi_2()
    root.after(1000, pokazi_3_2)


def show_zvjezdice(q):
    if q == 1:
        root.after(500, pokazi_1)
    elif q == 2:
        root.after(500, pokazi_2)
    elif q == 3:
        root.after(500, pokazi_3)


def show_congrats():
    clear()
    cograts = Label (root, text = 'Congrats!', bg = background_colour, bd = 0, fg = 'black', font = 'Fixedsys 35')
    cograts.place(relx = 0.5, rely = 0.15, anchor = 'center')
    global zvjezdice
    zvjezdice = Label (root, bd = 0, image = slikica_0)
    zvjezdice.place(relx = 0.5, rely = 0.43, anchor = 'center')

    vrijeme = Label (root, text = 'Your time:', bd = 0, bg = background_colour, font = 'Fixedsys 20')
    vrijeme.place(relx = 0.46, rely = 0.7, anchor = 'center')

    iznos = Label (root, bg = background_colour, bd = 0, text = 350, font = 'Fixedsys 20')
    iznos.place (relx = 0.58, rely = 0.7, anchor = 'center')
    global sekunde
    sekunde = sekunde - 1
    if sekunde < 0:
        sekunde = 0
    if sekunde < 10:
        iznos['text'] = str(minute) + ':' + '0' + str(sekunde)
    else:
        iznos['text'] = str(minute) + ':' + str(sekunde)

    global slika_next
    slika_next = PhotoImage (file = 'next_lvl.png')
    next_lvl = Button (root, bd = 0, text = 'next lvl',image = slika_next)
    next_lvl.place (rely = 0.8, relx = 0.62, anchor = 'center')
    global slika_choose
    slika_choose = PhotoImage(file = 'choose_lvls.png')
    izbor_lvl = Button (root, bd = 0, text = 'choose lvl', image = slika_choose)
    izbor_lvl.place(rely = 0.8, relx = 0.38, anchor = 'center')

    if provjera_tezine == 'easy':
        izbor_lvl['command'] = show_easy_lvls
        next_lvl['command'] = lambda: show_lvls_e(m + 1)
        if m == 5:
            next_lvl['command'] = show_easy_lvls
    elif provjera_tezine == 'medium':
        izbor_lvl['command'] = show_medium_lvls
        next_lvl['command'] = lambda:show_lvls_m(m + 1)
        if m == 5:
            next_lvl['command'] = show_medium_lvls
    elif provjera_tezine == 'hard':
        izbor_lvl['command'] = show_hard_lvls
        next_lvl['command'] = lambda:show_lvls_h(m + 1)
        if m == 5:
            next_lvl['command'] = show_hard_lvls
    show_zvjezdice(kratko)


def change():
    try:
        oopsie['text'] = ''
    except:
        DoNothing()

def check_4sudoku():
    global m
    global lista_sudoku
    lista_sudoku = []
    for i in range (len(lista_entrya)):
        if len(lista_entrya[i].get()) > 0:
            lista_sudoku.append(str(lista_entrya[i].get()))
        else:
            lista_sudoku.append(str(easy_lvls_unsolved[m][i]))
    if lista_sudoku == easy_lvls_solved[m]:
        global provjera
        global vrijeme_s
        global kratko
        provjera = False
        if vrijeme_s < 30:
            zvjezdice_easy[m] = '3'
            kratko = 3
        elif vrijeme_s < 60:
            if zvjezdice_easy[m] != '3':
                zvjezdice_easy[m] = '2'
            kratko = 2
        elif vrijeme_s < 90:
            if zvjezdice_easy[m] != '3' and zvjezdice_easy[m] != '2':
                zvjezdice_easy[m] = '1'
            kratko = 1
        else:
            if zvjezdice_easy[m] != '3' and zvjezdice_easy[m] != '2' and zvjezdice_easy[m] != '1':
                zvjezdice_easy[m] = '0'
            kratko = 0
        if m >= int(otkljucani_lvls_easy[0]):
            otkljucani_lvls_easy[0] = str(m + 1)
        show_congrats()

    else:
        oopsie['text'] = 'Something is wrong, try again.'

def check_9sudoku(z):
    global m
    global lista_sudoku
    global provjera
    global kratko
    lista_sudoku = []

    if z == 1:
        for i in range(len(lista_entrya)):
            if len(lista_entrya[i].get()) > 0:
                lista_sudoku.append(str(lista_entrya[i].get()))
            else:
                lista_sudoku.append(str(medium_lvls_unsolved[m][i]))
        if lista_sudoku == medium_lvls_solved[m]:
            provjera = False
            global kratko
            if vrijeme_s < 300:
                zvjezdice_medium[m] = '3'
                kratko = 3
            elif vrijeme_s < 480:
                if zvjezdice_medium[m] != '3':
                    zvjezdice_medium[m] = '2'
                kratko = 2
            elif vrijeme_s < 720:
                if zvjezdice_medium[m] != '3' and zvjezdice_medium[m] != '2':
                    zvjezdice_medium[m] = '1'
                kratko = 1
            else:
                if zvjezdice_medium[m] != '3' and zvjezdice_medium[m] != '2' and zvjezdice_medium[m] != '1':
                    zvjezdice_medium[m] = '0'
                kratko = 0
            if m >= int(otkljucani_lvls_medium[0]):
                otkljucani_lvls_medium[0] = str(m + 1)
            show_congrats()

        else:
            oopsie['text'] = 'Something is wrong, try again.'
    elif z == 2:
        for i in range(len(lista_entrya)):
            if len(lista_entrya[i].get()) > 0:
                lista_sudoku.append(str(lista_entrya[i].get()))
            else:
                lista_sudoku.append(str(hard_lvls_unsolved[m][i]))
        if lista_sudoku == hard_lvls_solved[m]:
            provjera = False
            if vrijeme_s < 600:
                zvjezdice_hard[m] = '3'
                kratko = 3
            elif vrijeme_s < 900:
                if zvjezdice_hard[m] != '3':
                    zvjezdice_hard[m] = '2'
                kratko = 2
            elif vrijeme_s < 1200:
                if zvjezdice_hard[m] != '3' and zvjezdice_hard[m] != '3':
                    zvjezdice_hard[m] = '1'
                kratko = 1
            else:
                if zvjezdice_hard[m] != '3' and zvjezdice_hard[m] != '2' and zvjezdice_hard[m] != '1':
                    zvjezdice_hard[m] = '0'
                kratko = 0
            if m >= int(otkljucani_lvls_hard[0]):
                otkljucani_lvls_hard[0] = str(m + 1)
            show_congrats()
        else:
            oopsie['text'] = 'Something is wrong, try again.'


def DoNothing():
    nothing = True


def save(e):
    global ime_datoteke
    dat = open(ime_datoteke, 'w')
    for i in range(len(zvjezdice_easy)):
        if i != 5:
            dat.write(zvjezdice_easy[i] + ' ')
        elif i == 5:
            dat.write(zvjezdice_easy[i] + '\n')
    for i in range(len(zvjezdice_medium)):
        if i != 5:
            dat.write(zvjezdice_medium[i] + ' ')
        elif i == 5:
            dat.write(zvjezdice_medium[i] + '\n')
    for i in range(len(zvjezdice_hard)):
        if i != 5:
            dat.write(zvjezdice_hard[i] + ' ')
        elif i == 5:
            dat.write(zvjezdice_hard[i] + '\n')
    dat.write(otkljucani_lvls_easy[0] + '\n')
    dat.write(otkljucani_lvls_medium[0] + '\n')
    dat.write(otkljucani_lvls_hard[0] + '\n')
    dat.write (str(timer_v) + '\n')

    dat.close()


select_profile()
root.mainloop()
try:
    save(100)
except:
    DoNothing()


dat = open('provjera.txt', 'w')
for i in range (len(lista_provjera)):
    if i == len(lista_provjera) - 1:
        dat.write (lista_provjera[i] + '\n')
    else:
        dat.write (lista_provjera[i] + ' ')
for i in range (len(lista_imena)):
    if i == len(lista_imena) - 1:
        dat.write (lista_imena[i] + '\n')
    else:
        dat.write (lista_imena[i] + ' ')
dat.close()
