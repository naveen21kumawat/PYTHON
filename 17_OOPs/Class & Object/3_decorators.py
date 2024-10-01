def greet(fx):
    print("good night?")
    fx()
    print("Good morning!")

    # def mfx():
    # mfx()
    #     fx()
    # return mfx

try:
    @greet 
    def hello():
        print("Hello")
        def hi():
            print("hi")
        hi()
except NameError:
    print("ERROR DETECT")