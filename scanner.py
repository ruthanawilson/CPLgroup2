#Class:       CS 4308 Section 01 
#Term:        Summer 2021
#Name:        Ruthana, Jorge, Seth
#Instructor:   Deepa Muralidhar 
#Project:  Deliverable 2 Parser - Python
import string


class Scanner:
    def __init__(self, filename):
        self.fileIn = open(filename, "r")
        self.count = 0
        self.char_type = 89
        self.lexeme = ""
        self.next_char = ''
        self.next_token = 1
        self.keywords = {
            "TEXT"  : 10,
            "HOME"  : 20,
            "REM"  : 30,
            "INPUT"  : 40,
            "LEN(S$)"  : 50,
            "IF"  : 60,
            "OR"  : 70,
            "GOTO"  : 80,
            "WIDTH"  : 90,
            "THEN"  : 100,
            "PRINT"  : 110,
            "FOR"  : 120,
            "TO"  : 130,
            "STEP"  : 140,
        #"single letter (variable)"  : "150",  special case so handled seperately
        #  "number"  : 160,                    special case handled seperately
        #  string literal : 170                special case 
            "END"  : 900,
            "LET"  : 190, 
            "PR"   : 330,
            "DIM"  : 340,
            "NEXT" : 350,
        }
        self.ops = {
            "+"  : 200,
            "-"  : 210,
            "*"  : 220,
            "/"  : 230,
            "("  : 240,
            ")"  : 250,  
            "<"  : 260,
            ">"  : 270,
            "="  : 280,
            ";"  : 290,
            ":"  : 300,
            "$"  : 310, 
            "#"  : 320,
            }

        self.func_names = {
            "ATN" : 360,
            "COS" : 370,
            "EXP" : 380,
            "INT" : 390,
            "LOG" : 400,
            "RND" : 410,
            "SIN" : 420,
            "SQR" : 430,
            "TAN" : 440, # currently we wont use these token numbers
            #instead all function names will have token number 500
        }

    #gets the next character from the file, sets the character type 
    def get_char(self):
        self.next_char = self.fileIn.read(1)
        if self.next_char == '\n':
            self.char_type = 800  #end of line
        elif self.next_char.isalpha():
            self.char_type = 0
        elif self.next_char.isdigit():
            self.char_type = 1
        elif self.next_char == "":
            self.char_type = 900   #end of file, 900 is also returned by END
        else:
            self.char_type = 99

    #adds the current character in next_char into the current lexeme being built
    def add_char(self):
        self.lexeme = self.lexeme + self.next_char

    def get_token(self):
        self.lexeme = ""
        self.skip_whitespace()
        if self.char_type == 0:
            self.handle_names()          #names and keywords are treated the same, 
        elif self.char_type == 1:        #except a check is made to see if the name is in keyword dict
            self.handle_ints()
        elif self.char_type == 99:
            self.check_op(self.next_char)
        elif self.char_type == 900:
            self.next_token = 900
        elif self.char_type == 800:
            self.next_token = 800
            self.add_char()
            self.get_char()

    def handle_names(self):
        self.add_char()
        self.get_char()
        self.get_lexeme([0,1])
        if self.lexeme =="REM":
                self.skip_line()
                self.get_token()
        elif self.lexeme in self.keywords.keys():
            self.next_token = self.keywords[self.lexeme]
        elif self.lexeme in self.func_names.keys():
            self.next_token = 500
        else:
            self.next_token = 150

    def handle_ints(self):
        self.add_char()
        self.get_char()
        self.get_lexeme([1])
        self.next_token = 160

    def skip_whitespace(self):
        if self.char_type == 900:
            return
        while self.next_char in string.whitespace and self.char_type != 800:
            if self.next_char == '\n':
                self.char_type = 800
                return
            self.get_char()

    #currently only used for comments, continues 
    #to grab characters until one after a \n
    def skip_line(self):
        while self.next_char != '\n':
            self.get_char()

    def check_op(self, c):
        if c in self.ops.keys():
                self.add_char()
                self.next_token = self.ops[self.next_char]
                self.get_char()
        elif c == '"':
            self.add_char()
            self.get_char()
            while self.next_char != '"':
                self.add_char()
                self.get_char()
            self.add_char()
            self.get_char()
            self.next_token = 170
        else:
            self.add_char()
            self.next_token = 600
            self.get_char()
        
            

    #continues to get characters if they are in condition list 
    def get_lexeme(self, conds):
        while self.char_type in conds or self.next_token == '.':
            self.add_char()
            self.get_char()
