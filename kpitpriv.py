class myClass:
    #private var
    __privateVar = 27;
    #private method
    def __privateMeth(self):
        print("I am inside class myClass")
    def hello(self):
        print("Private Variable value: ", myClass.__privateVar)
foo = myClass()
foo.hello()
foo.__privateMeth