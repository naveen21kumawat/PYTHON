f = open("mytext.txt",'w')
text =input("ENTER TEXT :")
f.write(text)
f.close

with open("mytxt.txt",'w') as p: # dont need to close file opend with 'with' clouse
    wrt=input(" Write data\32")
    p.write(wrt)