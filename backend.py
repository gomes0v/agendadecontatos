import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class Backend:
    """
    Backend for Contact Book
    Functions:
    add_contact() => Add Contact
    edit_contact() => Edit Contact
    del_contact() => Delete Contact
    get_all() => Get All Contacts from the db
    """
    def __init__(self):
        self.conn = sqlite3.connect('.\contacts.db')
        self.conn.row_factory = dict_factory
        self.cursor = self.conn.cursor()
        self.create_table()
        
        
    def create_table(self):
        self.cursor.execute(r"""CREATE TABLE IF NOT EXISTS contacts (
                                contact_id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL UNIQUE,
                                email VARCHAR(255) UNIQUE,
                                address TEXT,
                                phone TEXT NOT NULL UNIQUE
                                );""")
        self.conn.commit()
    
    def add_contact(self, **kwargs):
        query = (r"""INSERT INTO contacts (name, email, address, phone)
                            VALUES (:name, :email, :address, :phone);""")
        
        try:
             self.cursor.execute(query, kwargs)
        except sqlite3.Error as error:
            pass
        finally:        
            self.conn.commit()
    
    def edit_contact(self, **kwargs):
        query = "UPDATE contacts SET " + ", ".join(f + " = :" + f for f in kwargs if f != "contact_id") + " WHERE contact_id = :contact_id"
        self.cursor.execute(query, kwargs)
        self.conn.commit()
    
    def del_contact(self, contact_id):
        query = r"DELETE FROM contacts WHERE contact_id = :contact_id"
        self.cursor.execute(query, str(contact_id))
        self.conn.commit()
    
    def get_all(self):
        # all_records = self.cursor.fetchall()
        # return all_records
        self.cursor.execute(r"SELECT * FROM contacts ORDER BY name ASC")
        return self.cursor.fetchall()
        
    def fetch(self, id):
        self.cursor.execute(r"SELECT * FROM contacts WHERE contact_id = :id", {'id': id})
        return self.cursor.fetchall()
        