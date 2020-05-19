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

"""
class SinglyLinkedList:
    """ """
    def __init__(self):
        self.__head = Node
    def sorted_insert(self, value):
        while self.__head != None:
            self.__head == self.__head.next_node
            if value > self.__head.data and value < self.__head.next_node.data:
                break
        self.__head.data = value
        self.__head
        """
        