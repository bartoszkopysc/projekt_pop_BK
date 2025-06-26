from tkinter import *
import tkintermapview
import requests
from bs4 import BeautifulSoup

couriercompanys = []
workers = []
clients = []

class Couriercompany:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1], text=self.name)

    def get_coordinates(self):
        url = f"https://pl.wikipedia.org/wiki/{self.city}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        lon = float(soup.select(".longitude")[1].text.replace(",", "."))
        lat = float(soup.select(".latitude")[1].text.replace(",", "."))
        return [lat, lon]

class Worker:
    def __init__(self, name, surname, city, Couriercompany):
        self.name = name
        self.surname = surname
        self.city = city
        self.Couriercompany = Couriercompany
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1], text=f"{self.name} {self.surname}")

    def get_coordinates(self):
        url = f"https://pl.wikipedia.org/wiki/{self.city}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        lon = float(soup.select(".longitude")[1].text.replace(",", "."))
        lat = float(soup.select(".latitude")[1].text.replace(",", "."))
        return [lat, lon]

class Client:
    def __init__(self, name, surname, city, Couriercompany, class_name):
        self.name = name
        self.surname = surname
        self.city = city
        self.Couriercompany = Couriercompany
        self.coordinates = self.get_coordinates()
        self.marker = map_widget.set_marker(self.coordinates[0], self.coordinates[1], text=f"{self.name} {self.surname}")

    def get_coordinates(self):
        url = f"https://pl.wikipedia.org/wiki/{self.city}"
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        lon = float(soup.select(".longitude")[1].text.replace(",", "."))
        lat = float(soup.select(".latitude")[1].text.replace(",", "."))
        return [lat, lon]


def add_Couriercompany():
    name = entry_Couriercompany_name.get()
    city = entry_Couriercompany_city.get()
    s = Couriercompany(name, city)
    couriercompanys.append(s)
    entry_Couriercompany_name.delete(0, END)
    entry_Couriercompany_city.delete(0, END)
    entry_Couriercompany_name.focus()
    update_Worker_Couriercompany_menu()
    update_Client_Couriercompany_menu()
    show_couriercompanys()

def show_couriercompanys():
    listbox_couriercompanys.delete(0, END)
    for idx, s in enumerate(couriercompanys):
        listbox_couriercompanys.insert(idx, f"{idx+1}. {s.name} ({s.city})")

def show_Couriercompany_details():
    idx = listbox_couriercompanys.index(ACTIVE)
    s = couriercompanys[idx]
    listbox_workers_in_Couriercompany.delete(0, END)
    listbox_clients_in_Couriercompany.delete(0, END)
    label_Couriercompany_name_val.config(text=s.name)
    label_Couriercompany_city_val.config(text=s.city)
    map_widget.set_position(s.coordinates[0], s.coordinates[1])
    map_widget.set_zoom(16)

    listbox_workers_in_Couriercompany.delete(0, END)
    for t in workers:
        if t.Couriercompany == s.name:
            listbox_workers_in_Couriercompany.insert(END, f"{t.name} {t.surname}")
    for st in clients:
        if st.Couriercompany == s.name:
            listbox_clients_in_Couriercompany.insert(END, f"{st.name} {st.surname}")

def delete_Couriercompany():
    idx = listbox_couriercompanys.index(ACTIVE)
    couriercompanys[idx].marker.delete()
    couriercompanys.pop(idx)
    show_couriercompanys()
    update_Worker_Couriercompany_menu()
    update_Client_Couriercompany_menu()

def edit_Couriercompany():
    idx = listbox_couriercompanys.index(ACTIVE)
    entry_Couriercompany_name.insert(0, couriercompanys[idx].name)
    entry_Couriercompany_city.insert(0, couriercompanys[idx].city)
    button_add_Couriercompany.config(text="Zapisz", command=lambda: update_Couriercompany(idx))
    update_Worker_Couriercompany_menu()
    update_Client_Couriercompany_menu()

def update_Couriercompany(idx):
    couriercompanys[idx].marker.delete()
    name = entry_Couriercompany_name.get()
    city = entry_Couriercompany_city.get()
    couriercompanys[idx].name = name
    couriercompanys[idx].city = city
    couriercompanys[idx].coordinates = couriercompanys[idx].get_coordinates()
    couriercompanys[idx].marker = map_widget.set_marker(couriercompanys[idx].coordinates[0], couriercompanys[idx].coordinates[1], text=name)
    button_add_Couriercompany.config(text="Dodaj firmę kurierską", command=add_Couriercompany)
    entry_Couriercompany_name.delete(0, END)
    entry_Couriercompany_city.delete(0, END)
    show_couriercompanys()
    update_Worker_Couriercompany_menu()
    update_Client_Couriercompany_menu()


def add_Worker():
    name = entry_Worker_name.get()
    surname = entry_Worker_surname.get()
    city = entry_Worker_city.get()
    Couriercompany = var_Worker_Couriercompany.get()
    t = Worker(name, surname, city, Couriercompany)
    workers.append(t)
    entry_Worker_name.delete(0, END)
    entry_Worker_surname.delete(0, END)
    entry_Worker_city.delete(0, END)
    show_workers()

def show_workers():
    listbox_workers.delete(0, END)
    for idx, t in enumerate(workers):
        listbox_workers.insert(idx, f"{idx+1}. {t.name} {t.surname} - {t.Couriercompany} ({t.city})")

def show_Worker_details():
    idx = listbox_workers.index(ACTIVE)
    t = workers[idx]
    label_Worker_name_val.config(text=t.name)
    label_Worker_surname_val.config(text=t.surname)
    label_Worker_city_val.config(text=t.city)
    label_Worker_Couriercompany_val.config(text=t.Couriercompany)
    map_widget.set_position(t.coordinates[0], t.coordinates[1])
    map_widget.set_zoom(16)

def delete_Worker():
    idx = listbox_workers.index(ACTIVE)
    workers[idx].marker.delete()
    workers.pop(idx)
    show_workers()

def edit_Worker():
    idx = listbox_workers.index(ACTIVE)
    t = workers[idx]
    entry_Worker_name.insert(0, t.name)
    entry_Worker_surname.insert(0, t.surname)
    entry_Worker_city.insert(0, t.city)
    var_Worker_Couriercompany.set(t.Couriercompany)
    button_add_Worker.config(text="Zapisz", command=lambda: update_Worker(idx))

def update_Worker(idx):
    workers[idx].marker.delete()
    name = entry_Worker_name.get()
    surname = entry_Worker_surname.get()
    city = entry_Worker_city.get()
    Couriercompany = var_Worker_Couriercompany.get()
    workers[idx].name = name
    workers[idx].surname = surname
    workers[idx].city = city
    workers[idx].Couriercompany = Couriercompany
    workers[idx].coordinates = workers[idx].get_coordinates()
    workers[idx].marker = map_widget.set_marker(workers[idx].coordinates[0], workers[idx].coordinates[1], text=f"{name} {surname}")
    button_add_Worker.config(text="Dodaj pracownika", command=add_Worker)
    entry_Worker_name.delete(0, END)
    entry_Worker_surname.delete(0, END)
    entry_Worker_city.delete(0, END)
    show_workers()

def update_Worker_Couriercompany_menu():
    menu = optionmenu_Worker_Couriercompany["Menu"]
    menu.delete(0, "end")
    for Couriercompany in couriercompanys:
        menu.add_command(label=Couriercompany.name, command=lambda value=Couriercompany.name: var_Worker_Couriercompany.set(value))
    if couriercompanys:
        var_Worker_Couriercompany.set(couriercompanys[0].name)

def add_Client():
    name = entry_Client_name.get()
    surname = entry_Client_surname.get()
    city = entry_Client_city.get()
    Couriercompany = var_Client_Couriercompany.get()
    s = Client(name, surname, city, Couriercompany,add_Client)
    clients.append(s)
    entry_Client_name.delete(0, END)
    entry_Client_surname.delete(0, END)
    entry_Client_city.delete(0, END)
    show_clients()

def show_clients():
    listbox_clients.delete(0, END)
    for idx, s in enumerate(clients):
        listbox_clients.insert(idx, f"{idx+1}. {s.name} {s.surname} - {s.Couriercompany}, ({s.city})")

def show_Client_details():
    idx = listbox_clients.index(ACTIVE)
    s = clients[idx]
    label_Client_name_val.config(text=s.name)
    label_Client_surname_val.config(text=s.surname)
    label_Client_city_val.config(text=s.city)
    label_Client_Couriercompany_val.config(text=s.Couriercompany)
    map_widget.set_position(s.coordinates[0], s.coordinates[1])
    map_widget.set_zoom(16)

def delete_Client():
    idx = listbox_clients.index(ACTIVE)
    clients[idx].marker.delete()
    clients.pop(idx)
    show_clients()

def edit_Client():
    idx = listbox_clients.index(ACTIVE)
    s = clients[idx]
    entry_Client_name.insert(0, s.name)
    entry_Client_surname.insert(0, s.surname)
    entry_Client_city.insert(0, s.city)
    var_Client_Couriercompany.set(s.Couriercompany)
    button_add_Client.config(text="Zapisz", command=lambda: update_Client(idx))

def update_Client(idx):
    clients[idx].marker.delete()
    name = entry_Client_name.get()
    surname = entry_Client_surname.get()
    city = entry_Client_city.get()
    Couriercompany = var_Client_Couriercompany.get()
    clients[idx].name = name
    clients[idx].surname = surname
    clients[idx].city = city
    clients[idx].Couriercompany = Couriercompany
    clients[idx].coordinates = clients[idx].get_coordinates()
    clients[idx].marker = map_widget.set_marker(
        clients[idx].coordinates[0], clients[idx].coordinates[1],
        text=f"{name} {surname}"
    )
    button_add_Client.config(text="Dodaj klienta", command=add_Client)
    entry_Client_name.delete(0, END)
    entry_Client_surname.delete(0, END)
    entry_Client_city.delete(0, END)
    show_clients()

def update_Client_Couriercompany_menu():
    menu = optionmenu_Client_Couriercompany["menu"]
    menu.delete(0, "end")
    for Couriercompany in couriercompanys:
        menu.add_command(label=Couriercompany.name, command=lambda value=Couriercompany.name: var_Client_Couriercompany.set(value))
    if couriercompanys:
        var_Client_Couriercompany.set(couriercompanys[0].name)

def clear_all_markers():
    for s in couriercompanys:
        if s.marker:
            s.marker.delete()
            s.marker = None
    for t in workers:
        if t.marker:
            t.marker.delete()
            t.marker = None
    for st in clients:
        if st.marker:
            st.marker.delete()
            st.marker = None

def show_Worker_markers_for_Couriercompany(Couriercompany_name):
    clear_all_markers()
    for t in workers:
        if t.Couriercompany == Couriercompany_name:
            t.marker = map_widget.set_marker(t.coordinates[0], t.coordinates[1], text=f"{t.name} {t.surname}")

def show_Client_markers_for_Couriercompany(Couriercompany_name):
    clear_all_markers()
    for st in clients:
        if st.Couriercompany == Couriercompany_name:
            st.marker = map_widget.set_marker(st.coordinates[0], st.coordinates[1], text=f"{st.name} {st.surname}")

def get_selected_Couriercompany_name():
    idx = listbox_couriercompanys.index(ACTIVE)
    return couriercompanys[idx].name

def reset_Couriercompany_map_view():
    clear_all_markers()
    idx = listbox_couriercompanys.index(ACTIVE)
    s = couriercompanys[idx]
    if s.marker is None:
        s.marker = map_widget.set_marker(s.coordinates[0], s.coordinates[1], text=s.name)
    show_Couriercompany_details()


root = Tk()
root.title("System zarządzania firmami kurierskimi i pracownikami")
root.geometry("1024x800")

button_frame = Frame(root)
button_frame.grid(row=0, column=0)

def show_couriercompanys_frame():
    frame_couriercompanys.tkraise()

def show_workers_frame():
    frame_workers.tkraise()

Button(button_frame, text="Pokaż firmy kurierskie", command=show_couriercompanys_frame).grid(row=0, column=0, padx=5, pady=5)
Button(button_frame, text="Pokaż pracowników", command=show_workers_frame).grid(row=0, column=1, padx=5, pady=5)
Button(button_frame, text="Pokaż klientów", command=lambda: frame_clients.tkraise()).grid(row=0, column=2, padx=5, pady=5)


frame_couriercompanys = Frame(root)
frame_couriercompanys.grid(row=1, column=0, sticky="nsew")
frame_workers = Frame(root)
frame_workers.grid(row=1, column=0, sticky="nsew")


frame_Couriercompany_list = Frame(frame_couriercompanys)
frame_Couriercompany_form = Frame(frame_couriercompanys)
frame_Couriercompany_details = Frame(frame_couriercompanys)

Label(frame_Couriercompany_details, text="Pracownicy w tej firmie:").grid(row=1, column=0, sticky="w", padx=5)
listbox_workers_in_Couriercompany = Listbox(frame_Couriercompany_details, width=50, height=5)
listbox_workers_in_Couriercompany.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

Label(frame_Couriercompany_details, text="Klienci w tej firmie:").grid(row=1, column=1, sticky="w", padx=5)
listbox_clients_in_Couriercompany = Listbox(frame_Couriercompany_details, width=50, height=5)
listbox_clients_in_Couriercompany.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

Label(frame_Couriercompany_details, text="Nazwa:").grid(row=0, column=0, sticky="w", padx=5)
label_Couriercompany_name_val = Label(frame_Couriercompany_details, text="...")
label_Couriercompany_name_val.grid(row=0, column=1, sticky="w", padx=5)

Label(frame_Couriercompany_details, text="Miejscowość:").grid(row=0, column=2, sticky="w", padx=5)
label_Couriercompany_city_val = Label(frame_Couriercompany_details, text="...")
label_Couriercompany_city_val.grid(row=0, column=3, sticky="w", padx=5)

frame_Couriercompany_details.grid_columnconfigure(0, weight=1)
frame_Couriercompany_details.grid_columnconfigure(1, weight=1)
frame_Couriercompany_details.grid_columnconfigure(2, weight=0)
frame_Couriercompany_details.grid_columnconfigure(3, weight=0)
frame_Couriercompany_details.grid_rowconfigure(2, weight=1)

frame_Couriercompany_list.grid(row=0, column=0, sticky="nsew")
frame_Couriercompany_form.grid(row=0, column=1, sticky="nsew")
frame_Couriercompany_details.grid(row=0, column=2, sticky="nsew")

Label(frame_Couriercompany_list, text="Lista firm kurierskich:").grid(row=0, column=0, columnspan=3)
listbox_couriercompanys = Listbox(frame_Couriercompany_list, width=50)
listbox_couriercompanys.grid(row=1, column=0, columnspan=3)
Button(frame_Couriercompany_list, text="Pokaż szczegóły", command=show_Couriercompany_details).grid(row=2, column=0)
Button(frame_Couriercompany_list, text="Edytuj", command=edit_Couriercompany).grid(row=2, column=1)
Button(frame_Couriercompany_list, text="Usuń", command=delete_Couriercompany).grid(row=2, column=2)

Label(frame_Couriercompany_form, text="Nazwa firmy kurierskiej").grid(row=0, column=0)
entry_Couriercompany_name = Entry(frame_Couriercompany_form)
entry_Couriercompany_name.grid(row=0, column=1)

Label(frame_Couriercompany_form, text="Miejscowość:").grid(row=1, column=0)
entry_Couriercompany_city = Entry(frame_Couriercompany_form)
entry_Couriercompany_city.grid(row=1, column=1)

button_add_Couriercompany = Button(frame_Couriercompany_form, text="Dodaj firmę kurierską", command=add_Couriercompany)
button_add_Couriercompany.grid(row=2, column=0, columnspan=2)

frame_couriercompanys.grid_columnconfigure(0, weight=1)
frame_couriercompanys.grid_columnconfigure(1, weight=0)
frame_couriercompanys.grid_columnconfigure(2, weight=1)


frame_Worker_list = Frame(frame_workers)
frame_Worker_form = Frame(frame_workers)
frame_Worker_details = Frame(frame_workers)

frame_Worker_list.grid(row=0, column=0)
frame_Worker_form.grid(row=0, column=1)
frame_Worker_details.grid(row=0, column=2, sticky="nsew")

Label(frame_Worker_list, text="Lista pracowników:").grid(row=0, column=0, columnspan=3)
listbox_workers = Listbox(frame_Worker_list, width=50)
listbox_workers.grid(row=1, column=0, columnspan=3)
Button(frame_Worker_list, text="Pokaż szczegóły", command=show_Worker_details).grid(row=2, column=0)
Button(frame_Worker_list, text="Edytuj", command=edit_Worker).grid(row=2, column=1)
Button(frame_Worker_list, text="Usuń", command=delete_Worker).grid(row=2, column=2)

Label(frame_Worker_form, text="Imię:").grid(row=0, column=0)
entry_Worker_name = Entry(frame_Worker_form)
entry_Worker_name.grid(row=0, column=1)

Label(frame_Worker_form, text="Nazwisko:").grid(row=1, column=0)
entry_Worker_surname = Entry(frame_Worker_form)
entry_Worker_surname.grid(row=1, column=1)

Label(frame_Worker_form, text="Miejscowość:").grid(row=2, column=0)
entry_Worker_city = Entry(frame_Worker_form)
entry_Worker_city.grid(row=2, column=1)

Label(frame_Worker_form, text="Firma kurierska:").grid(row=3, column=0)
var_Worker_Couriercompany = StringVar()
var_Worker_Couriercompany.set("Brak firm kurierskich")
optionmenu_Worker_Couriercompany = OptionMenu(frame_Worker_form, var_Worker_Couriercompany, "Brak firm kurierskich")
optionmenu_Worker_Couriercompany.grid(row=3, column=1)

button_add_Worker = Button(frame_Worker_form, text="Dodaj pracownika", command=add_Worker)
button_add_Worker.grid(row=4, column=0, columnspan=2)

Label(frame_Worker_details, text="Imię:").grid(row=0, column=0)
label_Worker_name_val = Label(frame_Worker_details, text="...")
label_Worker_name_val.grid(row=0, column=1)

Label(frame_Worker_details, text="Nazwisko:").grid(row=0, column=2)
label_Worker_surname_val = Label(frame_Worker_details, text="...")
label_Worker_surname_val.grid(row=0, column=3)

Label(frame_Worker_details, text="Miejscowość:").grid(row=0, column=4)
label_Worker_city_val = Label(frame_Worker_details, text="...")
label_Worker_city_val.grid(row=0, column=5)

Label(frame_Worker_details, text="Firma kurierska:").grid(row=0, column=6)
label_Worker_Couriercompany_val = Label(frame_Worker_details, text="...")
label_Worker_Couriercompany_val.grid(row=0, column=7)


frame_clients = Frame(root)
frame_clients.grid(row=1, column=0, sticky="nsew")

frame_Client_list = Frame(frame_clients)
frame_Client_form = Frame(frame_clients)
frame_Client_details = Frame(frame_clients)

frame_Client_list.grid(row=0, column=0)
frame_Client_form.grid(row=0, column=1)
frame_Client_details.grid(row=1, column=0, columnspan=2)

Label(frame_Client_list, text="Lista klientów:").grid(row=0, column=0, columnspan=3)
listbox_clients = Listbox(frame_Client_list, width=50)
listbox_clients.grid(row=1, column=0, columnspan=3)
Button(frame_Client_list, text="Pokaż szczegóły", command=show_Client_details).grid(row=2, column=0)
Button(frame_Client_list, text="Edytuj", command=edit_Client).grid(row=2, column=1)
Button(frame_Client_list, text="Usuń", command=delete_Client).grid(row=2, column=2)

Label(frame_Client_form, text="Imię:").grid(row=0, column=0)
entry_Client_name = Entry(frame_Client_form)
entry_Client_name.grid(row=0, column=1)

Label(frame_Client_form, text="Nazwisko:").grid(row=1, column=0)
entry_Client_surname = Entry(frame_Client_form)
entry_Client_surname.grid(row=1, column=1)

Label(frame_Client_form, text="Miejscowość:").grid(row=2, column=0)
entry_Client_city = Entry(frame_Client_form)
entry_Client_city.grid(row=2, column=1)

Label(frame_Client_form, text="Firma kurierska:").grid(row=3, column=0)
var_Client_Couriercompany = StringVar()
var_Client_Couriercompany.set("Brak firm kurierskich")
optionmenu_Client_Couriercompany = OptionMenu(frame_Client_form, var_Client_Couriercompany, "Brak firm kurierskich")
optionmenu_Client_Couriercompany.grid(row=3, column=1)



button_add_Client = Button(frame_Client_form, text="Dodaj klienta", command=add_Client)
button_add_Client.grid(row=5, column=0, columnspan=2)

Label(frame_Client_details, text="Imię:").grid(row=0, column=0)
label_Client_name_val = Label(frame_Client_details, text="...")
label_Client_name_val.grid(row=0, column=1)

Label(frame_Client_details, text="Nazwisko:").grid(row=0, column=2)
label_Client_surname_val = Label(frame_Client_details, text="...")
label_Client_surname_val.grid(row=0, column=3)

Label(frame_Client_details, text="Miejscowość:").grid(row=0, column=4)
label_Client_city_val = Label(frame_Client_details, text="...")
label_Client_city_val.grid(row=0, column=5)

Label(frame_Client_details, text="Firma kurierska:").grid(row=0, column=6)
label_Client_Couriercompany_val = Label(frame_Client_details, text="...")
label_Client_Couriercompany_val.grid(row=0, column=7)




Button(frame_Couriercompany_list, text="Pokaż pracowników na mapie",
       command=lambda: show_Worker_markers_for_Couriercompany(get_selected_Couriercompany_name())
      ).grid(row=3, column=0, columnspan=3, sticky="ew", pady=(5,0))

Button(frame_Couriercompany_list, text="Pokaż klientów na mapie",
       command=lambda: show_Client_markers_for_Couriercompany(get_selected_Couriercompany_name())
      ).grid(row=4, column=0, columnspan=3, sticky="ew", pady=(5,10))

Button(frame_Couriercompany_list, text="Resetuj widok ,,firmy kurierskie''",
       command=reset_Couriercompany_map_view
      ).grid(row=5, column=0, columnspan=3, sticky="ew", pady=(0,10))



map_widget = tkintermapview.TkinterMapView(root, width=1024, height=400)
map_widget.set_position(52.2297, 21.0122)
map_widget.set_zoom(6)
map_widget.grid(row=2, column=0)


show_couriercompanys_frame()
root.mainloop()