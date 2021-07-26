#Class:       CS 4308 Section 01 
#Term:        Summer 2021
#Name:        Ruthana, Jorge, Seth
#Instructor:   Deepa Muralidhar 
#Project:  Deliverable 2 Parser - Python

class treeNode:
    def __init__(self):
        pass



class multiNode:
    def __init__(self, chld_tuple : tuple, name):
        self.name = name
        self.children = chld_tuple

    def show_nodes(self):
        name_string = self.name + " "
        for node in self.children:
            if type(node) == int or type(node) == str:
                name_string += str(node)
            elif type(node) == multiNode:
                name_string += node.show_nodes() + " " 
            else:
                name_string += "" 
        return name_string

def integer(x):
    return multiNode((x, None), "int")    

def string(x):
    return multiNode((x, None), "string")

def var(x):
    return multiNode((x, None), "variable")

def boolean(x):
    return multiNode((x,None), "bool")

def prntNode(l):
    return multiNode((l,None), "print_statement" )

def asgnNode(c,e):
    return multiNode((c,e), "=")

def ifNode(c,e):
    return multiNode((c,e), "if")

def muliply(x,y):
    return multiNode((x,y), "*")

def divide(x,y):
    return multiNode((x,y), "/")

def add(x,y):
    return multiNode((x,y), "+")

def sub(x,y):
    return multiNode((x,y), "-")

def lookup(var_name):
    if var_name not in var_table.keys():
        print("missing var assignment, returning null")
        return None
    else:
        return var_table[var_name]

def assign(var_name, val):
    var_table[var_name] = val

var_table = {}




