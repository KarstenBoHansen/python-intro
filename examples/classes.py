class Hello():
    def __init__(self, string):
        self.variable = string

    def say_hello(self):
        print(self.variable)

    def greet(self, name):
        return f"{self.variable} {name}"