#!/usr/bin/python3
class Node:
    """ """
def __init__(self, data, next_node=None):
    """ """
    if type(data) is not int:
        raise TypeError("data must be an integer")
    else:
        self.__data = data
    if next_node is not None and next_node is not Node:
        raise TypeError("next_node must be a Node object")
    else:
        self.__next_node = next_node

@property
def data(self):
    """ """
    return self.__data

@data.setter
def data(self, value):
    """ """
    if type(value) is not int:
        raise TypeError("data must be an integer")
    else:
        self.__data = value

@property
def next_node(self):
    """ """
    return self.__next_node

@next_node.setter
def next_node(self, value):
    """ """
    if value is not None and value is not Node:
        raise TypeError("next_node must be a Node object")
    else:
        self.__next_node = value


class SinglyLinkedList:
    """ """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node
        new_node.next_node = None
        new_node.data = value
        if self.__head == None:
            new_node.next_node = self.__head
            self.__head = new_node
        elif self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            cur_node = self.__head
            while cur_node.next_node.data < new_node.data:
                cur_node = cur_node.__next_node
            new_node.next_node = cur_node.next_node
            cur_node.next_node = new_node
    
    def __str__(self):
        while self.__head != None:
            self.__head == self.__head.next_node
            return str(self.__head.data)
            

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)