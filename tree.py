class treeNode:
    def __init__(self):
        pass

    def eval(self):
        pass

class multiNode(treeNode):
    def __init__(self, chld_tuple : tuple, name, prnt_op):
        self.name = name
        self.children = chld_tuple
        self.prnt_op = prnt_op
    
    def prnt(self):
        return self.prnt_op(*self.children)

    def show_nodes(self):
        print(self.name + ":", end=" ")
        for node in self.children:
            if node != None and type(node) == multiNode:
                print(node.name, end=" ")
        print()
        for node in self.children:
            if node != None and type(node) == multiNode:
                node.show_nodes() 

def integer(x):
    return multiNode((x, None), "int", lambda x, *args: str(x))    

def string(x):
    return multiNode((x, None), "string", lambda x, *args: x)

def var(x):
    return multiNode((x, None), "variable", lambda x, *args: str(x))

def boolean(x):
    return multiNode((x,None), "bool", lambda x, *args: str(x))

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





