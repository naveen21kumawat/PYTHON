with open("data.txt",'a') as a:
    a.write("Hello World\n")
    a.write("This is a test\n")
    with open("data.txt", 'r') as b:
        print(b.read())
