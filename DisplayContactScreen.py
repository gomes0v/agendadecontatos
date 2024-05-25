from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import mainScreen
from backend import Backend
from kivy.metrics import dp
class DisplayContact(Screen):
    Builder.load_file('.\DisplayContact.kv')
    db = Backend()
    
    def on_enter(self):
        try:
            ID = mainScreen.contactID[-1]
            self.display(ID)
        except Exception:
            pass
        
        
    def display(self, id):
        data = self.db.fetch(id)[0]
        self.ids.name.text = f"Nome:         {data['name']}"
        self.ids.email.text = f"Email:       {data['email']}"
        self.ids.address.text = f"Endereço:      {data['address']}"
        self.ids.phone.text = f"Telefone: {data['phone']}"
        
    