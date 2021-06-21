import scanner

# TODO: 1. Open and Read file
scan_obj = scanner.Scanner()

fileIn = open("BASICcode.txt", "r")
basic_code = fileIn.read()
words = basic_code.split()
  
# Big part after this print statement where we will validate tokens and count.

# TODO: 2. Write to existing output file

# After counting we then overwrite the empty output file with a 'count' or whatever we decide to use.

fileOut = open("output.txt", "w")
# Will need a format for the information we will write to the file.
for word in words:
  token = scan_obj.lookup(word)
  if bool(token):
    fileOut.write(token)


print(fileOut.read())
