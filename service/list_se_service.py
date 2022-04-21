from model.list_se import ListSE
from model.node import Node
from model.pet import Pet

class ListService:

    def __init__(self):
        self.list=ListSE()


    def get_all_linked(self):
        return self.list.head

    def invert(self):
        if self.list.head:
            return{"mesage":"la lista esta vacia"}
        else:
            return self.invert()
            return {"mesage":"se ha invertido la lista"}

    def add(self,dict):
        self.list.add_to_start(Pet(dict))
        return {"mesagge":"Adicionado con exito"}






