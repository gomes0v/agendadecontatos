from kivy.uix.screenmanager import Screen
from kivymd.uix.list import IRightBody, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.lang import Builder

from backend import Backend

dataObj = dict()
global edit_btn 
global del_btn
global view_btn
global contactID
contactID = []

KV = '''
<ListItemWithCheckbox>:
    checkbox: checkbox
    RightCheckbox:
        id: checkbox
        on_active:
            root.on_checkbox_active(*args)
'''

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    Builder.load_string(KV)
    
    def on_checkbox_active(self, checkbox, value):
        global edit_btn
        global del_btn
        global view_btn
        global contactID
        global dataObj
        #print(type(self))
        if value:
            edit_btn.disabled = False
            del_btn.disabled = False
            view_btn.disabled = False
            contactID.append(dataObj[self])
            # print(dataObj[self])
        else:
            view_btn.disabled = True
            edit_btn.disabled = True
            del_btn.disabled = True
            contactID.remove(dataObj[self])

class RightCheckbox(IRightBody, MDCheckbox):
    pass

class MainScreen(Screen):
    Builder.load_file('.\MainScreen.kv')
    db = Backend()
    displayed = False
    
    
    def on_enter(self):
        global edit_btn
        global view_btn
        global del_btn
        global dataObj
        view_btn = self.ids.view_contact
        edit_btn = self.ids.edit_contact
        del_btn = self.ids.del_contact
        
        edit_btn.disabled = True
        del_btn.disabled = True
        view_btn.disabled = True
        
        self.display()
        
        
    def display(self):
        self.ids.container.clear_widgets()
        records = self.db.get_all()
        if not records:
            if not self.displayed:
                self.ids.container.add_widget(MDLabel(text="Sem contatos", halign="center", valign="center"))
                self.displayed = True
            return
        
        for data in records:
            contact_id = data['contact_id']
            
            item = ListItemWithCheckbox(text=f"{data['name']}")
            dataObj[item] = contact_id
            self.ids.container.add_widget(item)
            
    def deleteContact(self):
        for ID in contactID:
            self.db.del_contact(ID)
        edit_btn.disabled = True
        del_btn.disabled = True
        view_btn.disabled = True
        self.displayed = False
        contactID.clear()
        self.display()
        

        