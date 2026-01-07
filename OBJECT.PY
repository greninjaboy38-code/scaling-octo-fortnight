class myclass:
    __privateVar = 27

    def __prevMeth(self):
        print("I am inside Myclass")

    def hello(self):
        print("The private variable value is:",myclass.__privateVar)

foo=myclass()
foo.hello()
foo.__privMeth()