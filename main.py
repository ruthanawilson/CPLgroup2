#Class:       CS 4308 Section 01 
#Term:        Summer 2021
#Name:        Ruthana, Jorge, Seth
#Instructor:   Deepa Muralidhar 
#Project:  Deliverable 2 Parser - Python

import scanner

# TODO: 1. Open and Read file
def main():
  #scanner now handles file input directly through get_char function
  basic_code = "BASICcode.txt"
  scan_obj = scanner.Scanner(basic_code)
    
  # Big part after this print statement where we will validate tokens and count.

  # TODO: 2. Write to existing output file

  # After counting we then overwrite the empty output file with a 'count' or whatever we decide to use.
  
  fileOut = open("output.txt", "w")
  # Will need a format for the information we will write to the file.
  
  while scan_obj.next_token != 900:
    scan_obj.get_token()
    token = scan_obj.next_token
    fileOut.write(str(token))
    fileOut.write(" " + scan_obj.lexeme)
    fileOut.write("\n")        #print("wrote " + str(token) + " to file")
  fileOut.close()

if __name__ == "__main__":
    main()
