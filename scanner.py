class Scanner:
    def __init__(self):
        self.count = 0
        self.tokens = {
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
            "END"  : 170,
            ";"  : 180,
            "$"  : 190,
            "="  : 200,
            ">"  : 210,
            "<"  : 220,
            ":"  : 230,   }

    #this expexts to be given each word after the input is divided by whitespace
    def lookup(self, lexeme):  
        vals = self.check_keywords(lexeme)
        if vals[0]:
            self.count += 1
            return vals[1]
        elif len(lexeme) == 1 and lexeme.isalpha():
            self.count += 1
            return 150
        elif lexeme.isdigit():
            self.count += 1
            return 160
        else:
            #if we dont have an identifier by now then somethings wrong
            return

    def check_keywords(self, lexeme):
        if lexeme not in self.tokens.keys():
            return [False, None]
        else:
            token = self.tokens[lexeme]
            return [True, token]
