# when we use self the instance attribute is called

class value():
    a=6
    def show(self):
        print(f'the value of a is {self.a}')


x=value()
x.a=45
x.show()


# when we use class method the class attributeis called::::

class value():
    a=6
    @classmethod
    def show(cls):
        print(f'the value of a is {cls.a}')


x=value()
x.a=45
x.show()