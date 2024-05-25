from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from backend import Backend
import mainScreen


class EditContactScreen(Screen):
    Builder.load_file('.\EditContact.kv')
    db = Backend()
    
    def on_enter(self):
        self.getData()
    
    def check_requirements(self):
        if len(self.ids.name_field.text) > 1 and len(self.ids.phone_field.text) > 1:
            self.ids.save.disabled= False
    
    def getData(self):
        self.ID = mainScreen.contactID[-1]
        details = self.db.fetch(self.ID)[0]
        self.ids.name_field.text = f"{details['name']}"
        self.ids.email_field.text = f"{details['email']}"
        self.ids.phone_field.text = f"{details['phone']}"
        self.ids.address_field.text = f"{details['address']}"
        
    
    def edit_contact_backend(self):
        details = {}
        details['name'] = self.ids.name_field.text
        details['email'] = self.ids.email_field.text
        details['phone'] = self.ids.phone_field.text
        details['address'] = self.ids.address_field.text
        details['contact_id'] = self.ID
        self.db.edit_contact(**details)
        
        self.ids.name_field.text = ""
        self.ids.email_field.text = ""
        self.ids.phone_field.text = ""
        self.ids.address_field.text = ""