from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from backend import Backend
from kivy.metrics import dp
class AddContact(Screen):
    Builder.load_file('.\Addcontact.kv')

    def check_requirements(self):
        if len(self.ids.name_field.text) > 1 and len(self.ids.phone_field.text) > 1:
            self.ids.save.disabled= False
    
    def add_contact_backend(self):
        db = Backend()
        details = {}
        details['name'] = self.ids.name_field.text
        details['email'] = self.ids.email_field.text
        details['phone'] = self.ids.phone_field.text
        details['address'] = self.ids.address_field.text
        db.add_contact(**details)
        
        self.ids.name_field.text = ""
        self.ids.email_field.text = ""
        self.ids.phone_field.text = ""
        self.ids.address_field.text = ""
    
    