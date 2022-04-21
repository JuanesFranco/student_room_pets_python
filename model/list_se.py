from .pet import Pet
from .node import Node

class ListSE:
    def __init__(self):
        self.head=None

    def add(self,pet:Pet):
        if self.head==None:
            self.head=Node(pet)
        else:
            temp=self.head
            while temp.next!=None:
                temp =temp.next
            #UBICADO EN EL ULTIMO
            temp.next=Node(pet)
    def add_to_start(self,pet:Pet):
        if self.head==None:
            self.head=Node(pet)
        else:
            temp=Node(pet)
            temp.next=self.head
            self.head=temp

    def invert(self):
        if self.head!=None:
            list_cp=ListSE()
            temp=self.head
            while temp!=None:
                list_cp.add_to_start(temp.data)
                temp=temp.next
            self.head=list_cp.head






