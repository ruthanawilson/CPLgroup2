import tree    #uses this for node structures
import scanner   #parser takes a single scanner object as an argument

class Parser:
    def __init__(self, scanner:scanner.Scanner):
        self.scanner = scanner
        self.ids = {}
    
    #the start of parsing
    #assigns the first node to root and begins recursively
    #adding nodes through prog()
    def parse(self):
        self.scanner.get_token()
        self.root = self.line()
    
    def lines(self):
        l = self.line()
        while self.scanner.next_token != 900:
            r = self.line()
            l = tree.multiNode((l,r), "lines")
    #call the different terminals and non-terminals found in a line
    #a line is a line number and a command list
    def line(self):
        if self.scanner.next_token == 160:
            self.scanner.get_token()
            cmd_list = self.cmd_list()
            return tree.multiNode((cmd_list,None), "line")
        else:
            print("expected line number at beginning of line!")
            return None




    #the second part of a line node
    #is multiple commands seperated by colons (300)
    def cmd_list(self):
        cmd_1 = self.command()
        if self.scanner.next_token == 300:
            self.scanner.get_token()
            lst = self.cmd_list()
            return tree.multiNode((cmd_1, lst), "statements")
        else:
            return tree.multiNode((cmd_1, None), "statements" )
    
    #each different type command in the basic language is parsed from here based 
    #mostly on the keyword used like PRINT or IF
    def command(self):
        if self.scanner.next_token == 800:
            self.scanner.get_token()
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
            return self.fun_stmnt()
        elif self.scanner.next_token == 40:
            return self.input_stmnt()

    #creates print statement node with an expression as a child
    def prnt_stmt(self):
        str_lit = self.str_lit()
        while True:
            if self.scanner.next_token == 290:
                self.scanner.get_token()
                lit_2 = self.str_lit()
                str_lit = tree.multiNode((str_lit, lit_2), "string")
        return tree.prntNode(str_lit)  #must be added to tree.py file
    
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
        if self.scanner.next_token != 100:
            print("expected THEN after IF condition")
            return None
        self.scanner.get_token()
        e = self.expr()
        return tree.ifNode(c,e) #TODO: add ifNode to tree.py
    
    def fun_stmnt(self):
        func_name = self.scanner.lexeme
        self.scanner.get_token()
        if self.scanner.next_token == 240:
            self.scanner.get_token()
            e = self.expr()
            if self.scanner.next_token == 250:
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
                l = tree.addNode(l,r)
            elif self.scanner.next_token == 210:
                self.scanner.get_token()
                r = self.term()
                l = tree.subNode(l,r)
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
                l = tree.multNode(l,r)
            elif self.scanner.next_token == 230:
                self.scanner.get_token()
                r = self.factor()
                l = tree.divNode(l,r)
            else:
                return l
    
    def factor(self):
        if self.scanner.next_token == 160:
            return self.num_literal()  
        if self.scanner.next_token == 150:
            return self.var()
        if self.scanner.next_token == 210:
            self.scanner.get_token()
            if self.scanner.next_token == 240:
                self.scanner.get_token()
                e = self.expr()
                
        if self.scanner.next_token == 240:
            self.scanner.get_token()
            a = self.expr()
            if self.scanner.next_token == 250:
                self.scanner.get_token()
                return a
            else:
                print("expected ) to close matching (")
                return None
        else:
            print("Expected a number next to operation")
            return None

    def num_literal(self):
        val = self.scanner.lexeme
        self.scanner.get_token()
        return tree.integer(int(val))
    
    def var(self):
        x = self.scanner.lexeme
        self.scanner.get_token()
        return tree.var(x)
    
    def str_lit(self):
        txt = self.scanner.lexeme
        return tree.multiNode((txt, None), "string_literal")

scan_obj = scanner.Scanner("BASIC_TEST_FILE.txt")
prse = Parser(scan_obj)
prse.parse()
prse.root.show_nodes()
        


