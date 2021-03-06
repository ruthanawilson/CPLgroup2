#Class:       CS 4308 Section 01 
#Term:        Summer 2021
#Name:        Ruthana, Jorge, Seth
#Instructor:   Deepa Muralidhar 
#Project:  Deliverable 3 Interpreter - Python

import tree    #uses this for node structures

#for nodes that simply call each sub-node in order
def default_func(a,b):
    if a != None:
        a.eval()
    if b != None:
        b.eval()
    #I added this here because a lot of these types of nodes: lines, line, cmd_lst, cmd dont have a dedicated function in tree.py

class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.ids = {}
    
    #the start of parsing
    #assigns the first node to root and begins recursively
    #adding nodes through prog()

    def display_preorder(self):
        return self.root.show_nodes()

    def parse(self):
        self.scanner.get_token()
        self.root = self.lines()
    
    def lines(self):
        l = self.line()
        while self.scanner.next_token != 900:
            r = self.line()
            l = tree.multiNode((l,r), "lines", default_func)
        return l
    #call the different terminals and non-terminals found in a line
    #a line is a line number and a command list
    def line(self):
        if self.scanner.next_token == 160:
            self.scanner.get_token()
            cmd_list = self.cmd_list()
            if self.scanner.next_token == 800 or self.scanner.next_token == 900:
                self.scanner.get_token()
                return tree.multiNode((cmd_list,None), "line", default_func)
            else:
                print("expected end of line after no more commands were found")
                return None
        else:
            self.scanner.get_token()
            print("expected line number at beginning of line!")
            return None




    #the second part of a line node
    #is multiple commands seperated by colons (300)
    def cmd_list(self):
        cmd_1 = self.command()
        if self.scanner.next_token == 300:
            self.scanner.get_token()
            lst = self.cmd_list()
            return tree.multiNode((cmd_1, lst), "statements", default_func)
        else:
            return tree.multiNode((cmd_1, None), "statements", default_func)
    
    #each different type command in the basic language is parsed from here based 
    #mostly on the keyword used like PRINT or IF
    def command(self):
        if self.scanner.next_token == 800:
            return tree.multiNode((None,None), "Empty")
        elif self.scanner.next_token == 60:
            self.scanner.get_token()
            return self.if_stmt()
        elif self.scanner.next_token == 110:
            self.scanner.get_token()
            return self.prnt_stmt()
        elif self.scanner.next_token == 190:
            self.scanner.get_token()
            return self.assign()
        elif self.scanner.next_token == 500:
            return self.func_call()
        elif self.scanner.next_token == 40:
            self.scanner.get_token()
            return self.input_stmnt()
        elif self.scanner.next_token == 900:
            return tree.multiNode((None,None), "end_of_program")
        else:
            #print("command Keyword: " + self.scanner.lexeme + " not recognized")
            while self.scanner.next_token != 800:
                self.scanner.get_token()
            return None

    #creates print statement node with an expression as a child
    def prnt_stmt(self):
        expr_1 = self.expr()
        return tree.prntNode(expr_1)
    
    #creates variable node, checks for '=' symbol, calls expression method,
    #returns assign node with variable node and expression node as children
    def assign(self):
        if self.scanner.next_token == 150:
            x = tree.var(self.scanner.lexeme)
            self.scanner.get_token()
            if self.scanner.next_token == 280:
                self.scanner.get_token()
                e = self.expr()
                return tree.asgnNode(x,e)  #TODO: add asgnNode to tree.py
            else:
                print(" = sign expected after variable name")  
                return None
    
    #calls condition method, checks for 'THEN' keyword
    #calls expression method, returns ifNode
    def if_stmt(self):
        c = self.cond()
        if self.scanner.next_token == 100:
            self.scanner.get_token()
            e = self.expr()
            return tree.ifNode(c,e) #TODO: add ifNode to tree.py
        else:
            print("expected THEN after IF condition")
            return None

    
    def func_call(self):
        func_name = self.scanner.lexeme
        self.scanner.get_token()
        if self.scanner.next_token == 240:
            self.scanner.get_token()
            e = self.expr()
            if self.scanner.next_token == 250:
                self.scanner.get_token()
                return tree.multiNode((e,None), func_name )

    def input_stmnt(self):
        x = self.var()

        return tree.multiNode((x,None), "INPUT")


    #we don't need to handle logical ops, just relational '<,>,==,<=,>='
    #returns condition node
    #TODO: support recursive calling based on possible conditionals in BASIC
    def cond(self):
        l = self.expr()
        if self.scanner.next_token == 260:
            self.scanner.get_token()
            r = self.expr()
            return tree.multiNode((l,r), "<")
        elif self.scanner.next_token == 270:
            self.scanner.get_token()
            r = self.expr()
            return tree.multiNode((l,r), ">")
        elif self.scanner.next_token == 280:
            self.scanner.get_token()
            r = self.expr()
            return tree.multiNode((l,r), "=")

    def expr(self):
        l = self.term()
        while True:
            if self.scanner.next_token == 200:
                self.scanner.get_token()
                r = self.term()
                l = tree.add(l,r)
            elif self.scanner.next_token == 210:
                self.scanner.get_token()
                r = self.term()
                l = tree.sub(l,r)
            else:
                return l
            
    #calls factor method 
    #returns either a factors or a mult/div node with two factors as children 
    def term(self):
        l = self.factor()
        while True:
            if self.scanner.next_token == 220:
                self.scanner.get_token()
                r = self.factor()
                l = tree.muliply(l,r)
            elif self.scanner.next_token == 230:
                self.scanner.get_token()
                r = self.factor()
                l = tree.divide(l,r)
            elif self.scanner.next_token == 600: #unknown op
                op_name = self.scanner.lexeme
                self.scanner.get_token()
                r = self.factor()
                l = tree.multiNode((l,r), op_name)
            else:
                return l
    
    def factor(self):
        if self.scanner.next_token == 160:  #number literal
            return self.num_literal()  
        if self.scanner.next_token == 150:  #variable
            return self.var()
        if self.scanner.next_token == 210:  #-(expr)
            self.scanner.get_token()
            if self.scanner.next_token == 240:
                self.scanner.get_token()
                e = self.expr()
                if self.scanner.next_token == 250:
                    self.scanner.get_token()
                    return tree.multiNode((e,None), "negate")
                else:
                    print("Expected matching ')' to close '('")
                    return None
            else:
                print("Expected (expression) after '-' with no operand")
                return None
        if self.scanner.next_token == 240:  # (expr)
            self.scanner.get_token()
            a = self.expr()
            if self.scanner.next_token == 250:
                self.scanner.get_token()
                return a
            else:
                print("expected ) to close matching (")
                return None
        if self.scanner.next_token == 500:  #math function
            f = self.func_call()
            return f
        else:
            print("Expected a number next to operation")
            return None

    def num_literal(self):
        val = self.scanner.lexeme
        self.scanner.get_token()
        return tree.integer(int(val))
    
    def str_lit(self):
        txt = self.scanner.lexeme
        return tree.multiNode((txt, None), "string_literal")
        
    
    def var(self):
        x = self.scanner.lexeme
        self.scanner.get_token()
        return tree.var(x)
    
    def str_lit(self):
        txt = self.scanner.lexeme
        self.scanner.get_token()
        return tree.multiNode((txt, None), "string_literal")
