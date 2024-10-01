a= open("mytxt.txt",'r')    
txt = a.read()
print(txt)
a.close()

with open("mytext.txt",'r') as p:
    text = p.read()
    print(text)