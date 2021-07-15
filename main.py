#Class:       CS 4308 Section 01 
#Term:        Summer 2021
#Name:        Ruthana, Jorge, Seth
#Instructor:   Deepa Muralidhar 
#Project:  Deliverable 2 Parser - Python

import scanner
import descent_parser

# TODO: 1. Open and Read file
def main():
  #scanner now handles file input directly through get_char function
  basic_code = "BASIC_Input_File_1.txt"
  scan_obj = scanner.Scanner(basic_code)
  prse = descent_parser.Parser(scan_obj)
  prse.parse()
  parse_tree_preorder = prse.display_preorder()
  # Big part after this print statement where we will validate tokens and count.
  
  # TODO: 2. Write to existing output file

  # After counting we then overwrite the empty output file with a 'count' or whatever we decide to use.
  
  fileOut = open("output.txt", "w")
  # Will need a format for the information we will write to the file.
  fileOut.write(parse_tree_preorder)
        #print("wrote " + str(token) + " to file")
  fileOut.close()

if __name__ == "__main__":
    main()
