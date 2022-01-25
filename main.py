from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
CORS(app)
version = "v1"


class Home(Resource):
    def get(self):
        home = open("home.json", "r")
        jsonHome = json.load(home)
        return {"home": jsonHome}

class Menu(Resource):
    def get(self):
        menu = open("menu.json", "r")
        jsonMenu = json.load(menu)
        return {"menu": jsonMenu}

class Elements(Resource):
    def get(self):
        elements = open("elements.json", "r")
        jsonElements = json.load(elements)
        return {"menu": jsonElements}

class Events(Resource):
    def get(self):
        events = open("events.json", "r")
        jsonEvents = json.load(events)
        return {"events": jsonEvents}

class Gallery(Resource):
    def get(self):
        gallery = open("gallery.json", "r")
        jsonGallery = json.load(gallery)
        return {"gallery": jsonGallery}

class About(Resource):
    def get(self):
        about = open("about.json", "r")
        jsonAbout = json.load(about)
        return {"about": jsonAbout}

class Contact(Resource):
    def get(self):
        contact = open("contact.json", "r")
        jsonContact = json.load(contact)
        return {"contact": jsonContact}

class Book(Resource):
    def get(self):
        booking = open("bookATable.json", "r")
        jsonBook = json.load(booking)
        return {"booking": jsonBook}


api.add_resource(Home, f'/{version}/home/')
api.add_resource(Menu, f'/{version}/menu/')
api.add_resource(Elements, f'/{version}/elements/')
api.add_resource(Events, f'/{version}/events/')
api.add_resource(Gallery, f'/{version}/gallery/')
api.add_resource(About, f'/{version}/about/')
api.add_resource(Contact, f'/{version}/contact/')
api.add_resource(Book, f'/{version}/booking/')


if __name__ == '__main__':
    app.run()