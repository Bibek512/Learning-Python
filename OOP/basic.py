class Programmer:
    company_name='microsoft'

    def __init__(self,name,age,salary,address):
        self.name=name
        self.age=age
        self.salary=salary
        self.address=address

    @staticmethod
    def hello():
     print("hello hiiii byeee")

bibek=Programmer('bibek',21,"200000",'nepal')     
print(bibek.name,bibek.age,bibek.salary,bibek.address,bibek.company_name) 
bibek.hello()