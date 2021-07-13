class treeNode:
    def __init__(self):
        pass

    def eval(self):
        pass

class multiNode(treeNode):
    def __init__(self, chld_tuple : tuple, name):
        self.name = name
        self.children = chld_tuple
   

    def show_nodes(self):
        name_string = self.name + " "
        for node in self.children:
            if type(node) != None:
                name_string += node.name + " " 
        return name_string

def integer(x):
    return multiNode((x, None), "int")    

def string(x):
    return multiNode((x, None), "string")

def var(x):
    return multiNode((x, None), "variable")

def boolean(x):
    return multiNode((x,None), "bool")

def asgnNode(c,e):
    return multiNode((c,e), "=")

def ifState(c,e):
    return multiNode((c,e), "if")

def muliply(x,y):
    return multiNode((x,y), "*")

def divide(x,y):
    return multiNode((x,y), "/")

def add(x,y):
    return multiNode((x,y), "+")

def sub(x,y):
    return multiNode((x,y), "-")





