# TODO: 1. Open and Read file

fileIn = open("BASICcode.txt", "r")
print(fileIn.read())

# Big part after this print statement where we will validate tokens and count.

# TODO: 2. Write to existing output file

# After counting we then overwrite the empty output file with a 'count' or whatever we decide to use.

fileOut = open("output.txt", "w")
# Will need a format for the information we will write to the file.
fileOut.write("PLACEHOLDER FOR SOME SHIT WE WILL ADD LATER")


print(fileOut.read())