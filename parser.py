import tree    #uses this for node structures
import scanner   #parser takes a single scanner object as an argument


def prnt_lines(*args):
    for arg in args:
        print(arg.prnt())    

def prnt_cmd(*args):
    for arg in args:
        arg.prnt()

class Parser:
    def __init__(self, scanner:scanner.Scanner):
        self.scanner = scanner
        self.ids = {}
    
    #the start of parsing
    #assigns the first node to root and begins recursively
    #adding nodes through prog()
    def parse(self):
        self.scanner.get_token()
        self.root = self.prog()
    
    #calls line method to parse new line nodes until it hits end of file (900)
    def prog(self):
        lines = ()
        while self.scanner.next_token != 900:
            l = self.line()
            lines = lines + (l,)
        return tree.multiNode(lines, "program", prnt_lines)

    
    #call the different terminals and non-terminals found in a line
    #a line is a line number and a command list
    def line(self):
        pass

    #the second part of a line node
    #is multiple commands seperated by colons (300)
    def cmd_list(self):
        pass
    
    #each different type command in the basic language is parsed from here based 
    #mostly on the keyword used like PRINT or IF
    def command(self):
        if self.scanner.next_token == 60:
            self.scanner.get_token()
            return self.if_stmt()
        elif self.scanner.next_token == 110:
            self.scanner.get_token()
            return self.prnt_stmt()
        else:
            return self.assign()

    #creates print statement node with an expression as a child
    def prnt_stmt(self):
        e = self.expr()
        return tree.prntNode(e)  #must be added to tree.py file
    
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
            return None
        self.scanner.get_token()
        e = self.expr()
        return tree.ifNode(c,e) #TODO: add ifNode to tree.py
    
    #we don't need to handle logical ops, just relational '<,>,==,<=,>='
    #returns condition node
    #TODO: support recursive calling based on possible conditionals in BASIC
    def cond(self):
        self.scanner.get_token()
        return tree.boolean(True)

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
            self.integers()   
            
        if self.scanner.next_token == 150:
            x = self.scanner.lexeme
            self.scanner.get_token()
            return tree.var(x)    
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

    def integers(self):
        val = self.scanner.lexeme
        self.scanner.get_token()
        return tree.integer(int(val))


scan_obj = scanner.Scanner("BASIC_Input_File_1.txt")
prse = Parser(scan_obj)
prse.parse()
prse.root
        


