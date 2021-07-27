#Class:       CS 4308 Section 01 
#Term:        Summer 2021
#Name:        Ruthana, Jorge, Seth
#Instructor:   Deepa Muralidhar 
#Project:  Deliverable 3 Interpreter - Python

class treeNode:
    def __init__(self):
        pass



class multiNode:
    def __init__(self, chld_tuple : tuple, name, func):
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
    
    def eval():
        l = chld_tuple[0]
        r = chld_tuple[1]
        return func(l,r)

def integer(x):
    return multiNode((x, None), "int", integerEval)    

def string(x):
    return multiNode((x, None), "string", lambda x: None)

def var(x):
    return multiNode((x, None), x, varEval)

def boolean(x):
    return multiNode((x,None), "bool", lambda x: None)

def prntNode(l):
    return multiNode((l,None), "print_statement", printEval)

def asgnNode(c,e):
    return multiNode((c,e), "=", assignEval)

def ifNode(c,e):
    return multiNode((c,e), "if", lambda x: None)

def muliply(x,y):
    return multiNode((x,y), "*", multiplyEval)

def divide(x,y):
    return multiNode((x,y), "/", divideEval)

def add(x,y):
    return multiNode((x,y), "+", addEval)

def sub(x,y):
    return multiNode((x,y), "-", subEval)

def lookup(var_name, y):
    if var_name not in var_table.keys():
        print("missing var assignment, returning null")
        return None
    else:
        return var_table[var_name]



var_table = {}

#assigns value to the lookup table
def assignEval(var, exp):
    var_table[var.name] = exp.eval()

#stores printed declaration into lookup table
def printEval(strng, y):
    print(strng)
   
#basic operations (add, subtract, multiply and divide)
def addEval(l,r):
       return l.eval() + r.eval()

def subEval(l,r):
       return l.eval() - r.eval()

def multiplyEval(l,r):
       return l.eval() * r.eval()

def divideEval(l,r):
       return l.eval() / r.eval()

def integerEval(x, y):
    return int(x)    

def stringEval(x,y):
    return int(x)

def varEval(x,y):
   return lookup(x)

def booleanEval(x):
    return  "bool"

def numericEval(x):
    return int(x)

def floatingEval(x):
    return  float(x)

