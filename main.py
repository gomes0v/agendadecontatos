from kivymd.app import MDApp
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from backend import Backend
from mainScreen import MainScreen
from AddContactsScreen import AddContact
from EditContact import EditContactScreen
from DisplayContactScreen import DisplayContact
from kivy.metrics import dp

Config.set('graphics', 'resizable', False)
Window.size = (300, 600)

class ContactBookApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MainScreen(name='mainScreen'))
        sm.add_widget(AddContact(name='contact'))
        sm.add_widget(DisplayContact(name='display_contact'))
        sm.add_widget(EditContactScreen(name='edit_contact'))
        return sm
        
    
    def on_start(self):
        self.backend = Backend()

ContactBookApp().run()
