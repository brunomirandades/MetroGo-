from tkinter import *
from PIL import ImageTk,Image
from dbgetlist import *

main_window = Tk()
main_window.title("MetroGO!")
main_window.geometry("900x600")

# -----------Images-----------
# change the path to the resources!!
gear_icon = ImageTk.PhotoImage(Image.open("/Users/brunomiranda/Documents/metrogo/resources/gear_icon.png").resize((30, 30),Image.ANTIALIAS))
search_icon = ImageTk.PhotoImage(Image.open("/Users/brunomiranda/Documents/metrogo/resources/search_icon.png").resize((30, 31),Image.ANTIALIAS))
map_icon = ImageTk.PhotoImage(Image.open("/Users/brunomiranda/Documents/metrogo/resources/map_icon.png").resize((60, 61),Image.ANTIALIAS))
metro_image_map = ImageTk.PhotoImage(Image.open("/Users/brunomiranda/Documents/metrogo/resources/mapa_metro_sp.png").resize((540, 485),Image.ANTIALIAS))

# --------Global Variables--------

station_label_station = 'Jabaquara'
station_label_line = 'Azul'
station_label_color = "Blue"
bg_color = "#636363"
font_type = 'Helvetica'
word_color = "White"
station_counter = "--\nEstações"
connection_counter = "--\nConexões"
login_admin = 'admin'
password_admin = '12345678'
login_status = ' '
select_station_aux = 0
station_text_array_from = []
station_text_array_to = []

# ------Functions---------


# Center Window Function
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


def admin_login():
    # -------------Login Window-------------
    global admin_window
    admin_window = Tk()
    admin_window.title('Login')
    admin_window.geometry("250x190")
    center(admin_window)

    global login_entry
    global password_entry
    global login_enter_button
    global admin_widow_frame
    global admin_window_login_status

    admin_widow_frame = Frame(admin_window, bg=bg_color)
    admin_widow_frame.pack()

    admin_window_label = Label(admin_widow_frame, text="Admin", font=(font_type, 15, "bold"), fg=word_color, bg=bg_color, width=20)
    admin_window_label.pack(pady=(15, 8), padx=60)

    frame_login = Frame(admin_widow_frame, bg=bg_color)
    frame_login.pack(pady=(0, 5))
    login_label = Label(frame_login, text='Login: ', anchor=W, bg=bg_color, fg=word_color, font=(font_type))
    login_label.pack(side=LEFT, padx=(32, 0))
    login_entry = Entry(frame_login, width=16)
    login_entry.pack(side=LEFT, padx=(0, 5))

    frame_password = Frame(admin_widow_frame, bg=bg_color)
    frame_password.pack(pady=(0, 10))
    password_label = Label(frame_password, text='Password: ', anchor=W, bg=bg_color, fg=word_color, font=(font_type))
    password_label.pack(side=LEFT, padx=(5, 0))
    password_entry = Entry(frame_password, width=16, show="*")
    password_entry.pack(side=LEFT, padx=(0, 5))

    frame_buttons_login = Frame(admin_widow_frame, bg=bg_color)
    frame_buttons_login.pack(pady=5)
    login_enter_button = Button(frame_buttons_login, text="Entrar", width=10, bg=bg_color, command=lambda: select_station(1))
    login_enter_button.pack(side=LEFT, padx=(0, 5))
    login_cancel_button = Button(frame_buttons_login, text="Cancelar", width=10, bg=bg_color, command=admin_window.destroy)
    login_cancel_button.pack(side=LEFT)

    admin_window_login_status = Label(admin_widow_frame, text=login_status, bg=bg_color, fg=word_color, font=font_type)
    admin_window_login_status.pack(pady=(0, 18))


def select_station(option):
    global select_station_aux
    global admin_window
    global login_status
    global login_entry
    global password_entry
    global login_admin
    global password_admin
    global admin_window_login_status
    global admin_widow_frame

    if option == 1:
        if str(login_entry.get()) == login_admin and str(password_entry.get()) == password_admin:
            select_station_aux = 1
            select_station_function()
            admin_window.destroy()
        else:
            login_status = 'Login ou Senha incorreto(s)!'
            admin_window_login_status.pack_forget()
            admin_window_login_status = Label(admin_widow_frame, text=login_status, bg=bg_color, fg=word_color,
                                              font=font_type)
            admin_window_login_status.pack(pady=(0, 18))
            login_status = ' '

    if option == 2:
        select_station_aux = 2
        select_station_function()

    if option == 3:
        select_station_aux = 3
        select_station_function()


def select_station_function():

    global select_station_aux
    global select_station_window
    global station_listbox_list

    select_station_window = Tk()
    select_station_window.title("Selecionar Estação")
    select_station_window.geometry("500x424")
    center(select_station_window)

    select_station_window_mainframe = Frame(select_station_window, bg=bg_color)
    select_station_window_mainframe.pack()

    station_listbox_label = Label(select_station_window_mainframe, text="Estações", font=(font_type, 25, "bold"), fg=word_color, bg=bg_color, width=20)
    station_listbox_label.pack(pady=(20, 0))

    frame_listbox = Frame(select_station_window_mainframe, borderwidth=2, relief=RIDGE, bg=bg_color)
    frame_listbox.pack(pady=10, padx=50)
    select_station_scrollbar = Scrollbar(frame_listbox, orient=VERTICAL)
    station_listbox_list = Listbox(frame_listbox, yscrollcommand=select_station_scrollbar.set, selectmode=SINGLE, height=14, width=50, font=(font_type, 18))
    select_station_scrollbar.config(command=station_listbox_list.yview)
    select_station_scrollbar.pack(side=RIGHT, fill=Y)
    station_listbox_list.pack()

    # filling the listbox
    for item in stations_db_list:
        station_listbox_list.insert(END, item[0] + " \t " + item[1])

    frame_select_station_buttons = Frame(select_station_window_mainframe, bg=bg_color)
    frame_select_station_buttons.pack(pady=(0, 30))
    select_station_select_btn = Button(frame_select_station_buttons, text="Selecionar", font=(font_type, 16), width=12, bg=bg_color, command=station_selection)
    select_station_select_btn.pack(side=LEFT, padx=(0, 10))
    select_station_cancel_btn = Button(frame_select_station_buttons, text="Cancelar", font=(font_type, 16), width=12, bg=bg_color, command=select_station_window.destroy)
    select_station_cancel_btn.pack(side=LEFT)


def station_selection():
    global select_station_aux
    global station_listbox_list
    global station_name_label
    global station_line_label
    global station_color_label
    global station_label_color
    global station_selection_admin_button
    global line_text_only_from
    global station_text_only_from
    global line_text_only_to
    global station_text_only_to
    global station_text_array_from
    global station_text_array_to
    global station_departure_get
    global  station_arrival_get



    # Selecting the Station for the Top Frame
    if select_station_aux == 1:
        station_text_string = str(station_listbox_list.get(ANCHOR))
        # print(station_text_string)
        station_text_array = station_text_string.split(" \t ")
        line_text_only = station_text_array[0]
        # print(line_text_only)
        station_text_only = station_text_array[1]
        # print(station_text_only)

        # Changing the Top Frame
        station_name_label.pack_forget()
        station_line_label.pack_forget()
        station_color_label.pack_forget()
        station_selection_admin_button.pack_forget()

        station_name_label = Label(frame_top, text=station_text_only, font=(font_type, 30, "bold"), anchor=W,
                                   fg=word_color, height=1, width=20, bg=bg_color)
        station_line_label = Label(frame_top, text=line_text_only, font=(font_type, 30, "bold"), anchor=E,
                                   fg=word_color, height=1, width=18, bg=bg_color)
        # Changing the line color
        if line_text_only == 'Azul':
            station_label_color = "Blue"
        elif line_text_only == 'Rubi':
            station_label_color = "Purple"
        elif line_text_only == 'Amarela':
            station_label_color = "Yellow"

        station_color_label = Label(frame_top, padx=50, pady=7, background=station_label_color, fg=word_color)
        station_selection_admin_button = Button(frame_top, image=gear_icon, command=admin_login, bg=bg_color)

        station_name_label.pack(side=LEFT, padx=(10, 0))
        station_line_label.pack(side=LEFT, padx=(56, 0))
        station_color_label.pack(side=LEFT, padx=(10, 0))
        station_selection_admin_button.pack(side=LEFT, padx=(10, 10))

        # Destroying the selection window
        select_station_window.destroy()
        select_station_aux = 0

    # Selecting the station for the "From" entry
    if select_station_aux == 2:
        station_text_string = str(station_listbox_list.get(ANCHOR))
        station_text_array_from = station_text_string.split(" \t ")
        station_departure_get = list(station_text_array_from)
        # aux for route function
        # station_text_array_from = station_text_array
        # print(station_text_array_from)
        line_text_only_from = station_text_array_from[0]
        station_text_only_from = station_text_array_from[1]

        from_entry.delete(0, END)
        from_entry.insert(0, line_text_only_from + " " + station_text_only_from)
        # print(stations_from_array)

        select_station_window.destroy()
        select_station_aux = 0

    # Selecting the station for the "To" entry
    if select_station_aux == 3:
        station_text_string = str(station_listbox_list.get(ANCHOR))
        station_text_array_to = station_text_string.split(" \t ")
        station_arrival_get = list(station_text_array_to)
        # aux for route function
        # station_text_array_to = station_text_array_to
        #print(station_text_array_to)
        line_text_only_to = station_text_array_to[0]
        station_text_only_to = station_text_array_to[1]

        to_entry.delete(0, END)
        to_entry.insert(0, line_text_only_to + " " + station_text_only_to)
        # print(stations_to_array)

        select_station_window.destroy()
        select_station_aux = 0


'''
def search_route():
    for i in range(50):
        Label(route_canvas_scrollable_frame, text="Sample scrolling label",
              bd=5, relief=SUNKEN, bg="Purple", fg="White",
              font=("Helvetica", 15, "bold"), width=39).pack()
'''


def search_route(stations_from_array, stations_to_array):
    global station_route_label
    global connection_route_label
    global map_button
    global station_counter
    global connection_counter

    stations_1 = []
    stations_2 = []
    stations_3 = []

    for i in range(len(stations_db_list)):
        for j in range(2):
            if 'Azul' == stations_db_list[i][j]:
                stations_1.append(stations_db_list[i])
            if 'Rubi' == stations_db_list[i][j]:
                stations_2.append(stations_db_list[i])
            if 'Amarela' == stations_db_list[i][j]:
                stations_3.append(stations_db_list[i])

    station_cnt_label = 0
    connection_cnt_label = 0

    # print(stations_from_array)
    # print(stations_to_array)
    # print(stations_1)

    if stations_from_array in stations_1 and stations_to_array in stations_1:
        if stations_1.index(stations_from_array) < stations_1.index(stations_to_array):
            aux_array_to_print = stations_1[stations_1.index(stations_from_array):
                                            stations_1.index(stations_to_array) + 1]
        if stations_1.index(stations_from_array) > stations_1.index(stations_to_array):
            aux_array_to_print = stations_1[stations_1.index(stations_to_array):
                                            stations_1.index(stations_from_array) + 1]
            aux_array_to_print.reverse()
        array_to_print = aux_array_to_print
    elif stations_from_array in stations_2 and stations_to_array in stations_2:
        if stations_2.index(stations_from_array) < stations_2.index(stations_to_array):
            aux_array_to_print = stations_2[stations_2.index(stations_from_array):
                                            stations_2.index(stations_to_array) + 1]
        if stations_2.index(stations_from_array) > stations_2.index(stations_to_array):
            aux_array_to_print = stations_2[stations_2.index(stations_to_array):
                                            stations_2.index(stations_from_array) + 1]
            aux_array_to_print.reverse()
        array_to_print = aux_array_to_print
    elif stations_from_array in stations_3 and stations_to_array in stations_3:
        if stations_3.index(stations_from_array) < stations_3.index(stations_to_array):
            aux_array_to_print = stations_3[stations_3.index(stations_from_array):
                                            stations_3.index(stations_to_array) + 1]
        if stations_3.index(stations_from_array) > stations_3.index(stations_to_array):
            aux_array_to_print = stations_3[stations_3.index(stations_to_array):
                                            stations_3.index(stations_from_array) + 1]
            aux_array_to_print.reverse()
        array_to_print = aux_array_to_print
    else:
        connection_cnt_label = 1
        # departure
        if stations_from_array in stations_1:
            if stations_1.index(stations_from_array) > stations_1.index(['Azul', 'Luz']):
                add_array_to_print_from = stations_1[
                                          stations_1.index(['Azul', 'Luz']):stations_1.index(
                                              stations_from_array) + 1]
                add_array_to_print_from.reverse()
                array_to_print_from = add_array_to_print_from

            if stations_1.index(stations_from_array) < stations_1.index(['Azul', 'Luz']):
                array_to_print_from = stations_1[stations_1.index(stations_from_array):
                                                 stations_1.index(['Azul', 'Luz']) + 1]

            if stations_1.index(stations_from_array) == stations_1.index(['Azul', 'Luz']):
                array_to_print_from = [stations_from_array]

        if stations_from_array in stations_2:
            if stations_2.index(stations_from_array) > stations_2.index(['Rubi', 'Luz']):
                add_array_to_print_from = stations_2[
                                          stations_2.index(['Rubi', 'Luz']):stations_2.index(
                                              stations_from_array) + 1]
                add_array_to_print_from.reverse()
                array_to_print_from = add_array_to_print_from

            if stations_2.index(stations_from_array) < stations_2.index(['Rubi', 'Luz']):
                array_to_print_from = stations_2[stations_2.index(stations_from_array):
                                                 stations_2.index(['Rubi', 'Luz']) + 1]

            if stations_2.index(stations_from_array) == stations_2.index(['Rubi', 'Luz']):
                array_to_print_from = [stations_from_array]

        if stations_from_array in stations_3:
            if stations_3.index(stations_from_array) > stations_3.index(['Amarela', 'Luz']):
                add_array_to_print_from = stations_3[
                                          stations_3.index(['Amarela', 'Luz']):stations_3.index(
                                              stations_from_array) + 1]
                add_array_to_print_from.reverse()
                array_to_print_from = add_array_to_print_from

            if stations_3.index(stations_from_array) < stations_3.index(['Amarela', 'Luz']):
                array_to_print_from = stations_3[stations_3.index(stations_from_array):
                                                 stations_3.index(['Amarela', 'Luz']) + 1]

            if stations_3.index(stations_from_array) == stations_3.index(['Amarela', 'Luz']):
                array_to_print_from = [stations_from_array]

            # arrival
        if stations_to_array in stations_1:
            if stations_1.index(stations_to_array) > stations_1.index(['Azul', 'Luz']):
                array_arrival_print = stations_1[
                                      stations_1.index(['Azul', 'Luz']):stations_1.index(stations_to_array) + 1]

            if stations_1.index(stations_to_array) < stations_1.index(['Azul', 'Luz']):
                add_array_arrival_print = stations_1[
                                          stations_1.index(stations_to_array):stations_1.index(
                                              ['Azul', 'Luz']) + 1]
                add_array_arrival_print.reverse()
                array_arrival_print = add_array_arrival_print

            if stations_1.index(stations_to_array) == stations_1.index(['Azul', 'Luz']):
                array_arrival_print = [stations_to_array]

        if stations_to_array in stations_2:
            if stations_2.index(stations_to_array) > stations_2.index(['Rubi', 'Luz']):
                array_arrival_print = stations_2[
                                      stations_2.index(['Rubi', 'Luz']):stations_2.index(stations_to_array) + 1]

            if stations_2.index(stations_to_array) < stations_2.index(['Rubi', 'Luz']):
                add_array_arrival_print = stations_2[
                                          stations_2.index(stations_to_array):stations_2.index(
                                              ['Rubi', 'Luz']) + 1]
                add_array_arrival_print.reverse()
                array_arrival_print = add_array_arrival_print

            if stations_2.index(stations_to_array) == stations_2.index(['Rubi', 'Luz']):
                array_arrival_print = [stations_to_array]

        if stations_to_array in stations_3:
            if stations_3.index(stations_to_array) > stations_3.index(['Amarela', 'Luz']):
                array_arrival_print = stations_3[
                                      stations_3.index(['Amarela', 'Luz']):stations_3.index(stations_to_array) + 1]

            if stations_3.index(stations_to_array) < stations_3.index(['Amarela', 'Luz']):
                add_array_arrival_print = stations_3[
                                          stations_3.index(stations_to_array):stations_3.index(
                                              ['Amarela', 'Luz']) + 1]
                add_array_arrival_print.reverse()
                array_arrival_print = add_array_arrival_print

            if stations_3.index(stations_to_array) == stations_3.index(['Amarela', 'Luz']):
                array_arrival_print = [stations_to_array]

        array_to_print = list(array_to_print_from + array_arrival_print)


    #print()
    #print(array_to_print_from)
    #print()
    #print(array_arrival_print)
    #print()

    # print(array_to_print)
    # print()

    # cleaning canvas
    for widget in route_canvas_scrollable_frame.winfo_children():
        widget.destroy()

    # removing repeated stations
    for i in range(len(array_to_print)-1):
        if array_to_print[i] == array_to_print[i-1]:
            array_to_print.pop(array_to_print.index(array_to_print[i]))

    '''
    for i in array_to_print:
        print(i)
    '''

    for i in range(len(array_to_print)):
        station_cnt_label += 1
        if array_to_print[i][0] == 'Azul':
            canvas_label_station_color = "Blue"
            canvas_label_station_word_color = "White"
        elif array_to_print[i][0] == 'Rubi':
            canvas_label_station_color = "Purple"
            canvas_label_station_word_color = "White"
        elif array_to_print[i][0] == 'Amarela':
            canvas_label_station_color = "Yellow"
            canvas_label_station_word_color = "Black"

        Label(route_canvas_scrollable_frame, text=array_to_print[i][1],
              bd=2, relief=GROOVE, bg=canvas_label_station_color, fg=canvas_label_station_word_color,
              font=("Helvetica", 17, "bold"), width=36).pack()

    station_counter = str(station_cnt_label) + "\nEstações"
    connection_counter = str(connection_cnt_label) + "\nConexão"

    station_route_label.pack_forget()
    connection_route_label.pack_forget()
    map_button.pack_forget()
    station_route_label = Label(frame_bottom_right_2, text=station_counter, bg=bg_color, fg=word_color,
                                font=(font_type, 25, "bold"), width=10)
    station_route_label.pack(pady=(0, 80))
    connection_route_label = Label(frame_bottom_right_2, text=connection_counter, bg=bg_color, fg=word_color,
                                   font=(font_type, 25, "bold"), width=10)
    connection_route_label.pack(pady=(0, 80))
    map_button = Button(frame_bottom_right_2, image=map_icon, bg=bg_color, command=show_map)
    map_button.pack(pady=(0, 20))


def clean_route():
    global station_counter
    global connection_counter
    global station_route_label
    global connection_route_label
    global map_button

    # cleaning the fields
    from_entry.delete(0, END)
    to_entry.delete(0, END)
    # cleaning the route canvas
    for widget in route_canvas_scrollable_frame.winfo_children():
        widget.destroy()

    station_counter = "--\nEstações"
    connection_counter = "--\nConexões"

    station_route_label.pack_forget()
    connection_route_label.pack_forget()
    map_button.pack_forget()
    station_route_label = Label(frame_bottom_right_2, text=station_counter, bg=bg_color, fg=word_color,
                                font=(font_type, 25, "bold"), width=10)
    station_route_label.pack(pady=(0, 80))
    connection_route_label = Label(frame_bottom_right_2, text=connection_counter, bg=bg_color, fg=word_color,
                                   font=(font_type, 25, "bold"), width=10)
    connection_route_label.pack(pady=(0, 80))
    map_button = Button(frame_bottom_right_2, image=map_icon, bg=bg_color, command=show_map)
    map_button.pack(pady=(0, 20))


def show_map():
    global map_window
    global metro_image_map

    # Must use Toplevel or else the image will not show
    map_window = Toplevel()
    map_window.title('Mapa do Metrô')
    map_window.geometry("560x560")
    center(map_window)

    map_window_frame = Frame(map_window, borderwidth=2, relief=RIDGE, bg=bg_color)
    map_window_frame.pack()

    map_label = Label(map_window_frame, image=metro_image_map)
    # declare the image to avoid garbage collection
    map_label.image = metro_image_map
    map_label.pack(pady=(5, 0), padx=5)

    map_window_quit_button = Button(map_window_frame, text="Sair", width=10, bg=bg_color, font=(font_type, 20), command=map_window.destroy)
    map_window_quit_button.pack(pady=(10, 20))


# ------Main window-------
center(main_window)
frame_top = Frame(main_window, borderwidth=2, relief=RIDGE, height=50, width=800, bg=bg_color)
frame_bottom_left = Frame(main_window, borderwidth=2, relief=RIDGE, height=600, width=350, bg=bg_color)
frame_bottom_right = Frame(main_window, borderwidth=2, relief=RIDGE, height=600, width=550, bg=bg_color)

frame_top.pack()
frame_bottom_left.pack(side=LEFT)
frame_bottom_right.pack(side=LEFT)

# --------Top Frame

station_name_label = Label(frame_top, text=station_label_station, font=(font_type, 30, "bold"), anchor=W, fg=word_color, height=1, width=20, bg=bg_color)
station_line_label = Label(frame_top, text=station_label_line, font=(font_type, 30, "bold"), anchor=E, fg=word_color, height=1, width=18, bg=bg_color)
station_color_label = Label(frame_top, padx=50, pady=7, background=station_label_color, fg=word_color)
station_selection_admin_button = Button(frame_top, image=gear_icon, command=admin_login, bg=bg_color)

station_name_label.pack(side=LEFT, padx=(10,0))
station_line_label.pack(side=LEFT, padx=(56, 0))
station_color_label.pack(side=LEFT, padx=(10, 0))
station_selection_admin_button.pack(side=LEFT, padx=(10, 10))

# ---------Bottom Left Frame

frame_bottom_left_1 = Frame(frame_bottom_left, bg=bg_color)
frame_bottom_left_1.pack(pady=(90, 30))
from_label = Label(frame_bottom_left_1, text="Origem", bg=bg_color, fg=word_color, font=(font_type, 30, "bold"))
from_label.pack()

frame_bottom_left_2 = Frame(frame_bottom_left, bg=bg_color)
frame_bottom_left_2.pack()
from_button = Button(frame_bottom_left_2, image=search_icon, bg=bg_color, command=lambda: select_station(2))
from_button.pack(side=LEFT)
from_entry = Entry(frame_bottom_left_2, width=20, font=(font_type, 20))
from_entry.pack(side=LEFT)

frame_bottom_left_3 = Frame(frame_bottom_left, bg=bg_color)
frame_bottom_left_3.pack(pady=(50, 30))
to_label = Label(frame_bottom_left_3, text="Destino", bg=bg_color, fg=word_color, font=(font_type, 30, "bold"))
to_label.pack()

frame_bottom_left_4 = Frame(frame_bottom_left, bg=bg_color)
frame_bottom_left_4.pack(padx=30)
to_button = Button(frame_bottom_left_4, image=search_icon, bg=bg_color, command=lambda: select_station(3))
to_button.pack(side=LEFT)
to_entry = Entry(frame_bottom_left_4, width=20, font=(font_type, 20))
to_entry.pack(side=LEFT)

frame_bottom_left_5 = Frame(frame_bottom_left, bg=bg_color)
frame_bottom_left_5.pack(pady=(60, 110))
search_search_button = Button(frame_bottom_left_5, text="Pesquisar", width=10, command=lambda: search_route(station_departure_get, station_arrival_get), bg=bg_color, font=(font_type, 20))
search_search_button.pack(side=LEFT)
clean_search_button = Button(frame_bottom_left_5, text="Limpar", width=10, command=clean_route, bg=bg_color, font=(font_type, 20))
clean_search_button.pack(side=LEFT, padx=(35, 0))

# -----Bottom Right Frame

frame_bottom_right_1 = Frame(frame_bottom_right, bg=bg_color)
frame_bottom_right_1.pack(side=LEFT)
route_label = Label(frame_bottom_right_1, text="Trajeto", bg=bg_color, fg=word_color, anchor=W, font=(font_type, 30, "bold"))
route_label.pack(pady=(15,0))
frame_route = Frame(frame_bottom_right_1, bd=2, relief=RIDGE, height=550, width=390, background=bg_color)
frame_route.pack(pady=(10, 10), padx=10)

# Canvas
route_canvas = Canvas(frame_route, bg="#969696", bd=0, height=540, width=362)
route_canvas_scrollbar = Scrollbar(frame_route, orient="vertical", command=route_canvas.yview)

route_canvas_scrollable_frame = Frame(route_canvas, bg="#969696", bd=0)
route_canvas_scrollable_frame.bind("<Configure>", lambda e: route_canvas.configure(scrollregion=route_canvas.bbox("all")))
route_canvas.create_window((0, 0), window=route_canvas_scrollable_frame, anchor="nw")
route_canvas.configure(yscrollcommand=route_canvas_scrollbar.set)

route_canvas.pack(side="left", fill="both", expand=True)
route_canvas_scrollbar.pack(side="right", fill="y")

frame_bottom_right_2 = Frame(frame_bottom_right, bg=bg_color)
frame_bottom_right_2.pack(side=LEFT, padx=(0, 10))
station_route_label = Label(frame_bottom_right_2, text=station_counter, bg=bg_color, fg=word_color, font=(font_type, 25, "bold"), width=10)
station_route_label.pack(pady=(0, 80))
connection_route_label = Label(frame_bottom_right_2, text=connection_counter, bg=bg_color, fg=word_color, font=(font_type, 25, "bold"), width=10)
connection_route_label.pack(pady=(0, 80))
map_button = Button(frame_bottom_right_2, image=map_icon, bg=bg_color, command=show_map)
map_button.pack(pady=(0, 20))

main_window.mainloop()