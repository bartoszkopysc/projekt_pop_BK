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
    menu = optionmenu_Worker_Couriercompany["menu"]
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