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