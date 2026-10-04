class User:
    def __init__(self,name):
        self.name=name
    def get_prmissions(self):
        return []
class Admin(User):
    def get_prmissions(self):
        return ["view","edit","delete"]
class Editor(User):
    def get_prmissions(self):
        return ["view","edit"]
class Viewer(User):
    def get_prmissions(self):
        return ["view"]
admin=Admin("Alice")
editor=Editor("Bob")
viewer=Viewer("Charlie")
print(admin.get_prmissions())
print(editor.get_prmissions())
print(viewer.get_prmissions())