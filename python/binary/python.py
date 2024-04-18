class Identity:
    def __init__(self, name, ethnicity, age):
        self.name = name
        self.ethnicity = ethnicity
        self.age = age

    def __str__(self):
        return f"{self.name} {self.ethnicity} {self.age}"

    def myFunc(self):
        print("Hello i am " + self.ethnicity)


firstIdentity = Identity('John', 'black', 22)

firstIdentity.myFunc()
