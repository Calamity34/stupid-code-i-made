import os

theword = input("What letter word would you like to say? ")
print("...")

joe = "joe.txt"
file = open(joe,'r')
text = file.read()
print(text)
file.close()
file = open(joe,'w')
file.write(text + theword + " word")
file.close()
file = open(joe,'r')
text = file.read()
print(text)
file.close()
file = open(joe,'w')
file.write("i am going to say the ")
file.close()

h = input("Do you need help with OS module? Type '1' if yes: ")
if h == "1":
    help(os)
else:
    print("Ok!")
