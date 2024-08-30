# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def config(self,):
#         print(f'the config is {self.cpu} , {self.ram}')

# c1=computer('i5',16)
# c2=computer('i9',32)
# c1.config()
# c2.config()

'''***********else*********'''

# class computer:
#     def config(self):
#         print('i5',16)

# c1=computer()
# c2=computer()
# c1.config()
# c2.config()

'''*********constructor******'''

# class computer:
#     def __init__(self):
#         self.name='navin'
#         self.age=20

#     def update(self):
#         self.age=30

# c1=computer()
# c2=computer()
# c1.name='rashid'
# c1.age=20
# c1.update()
# print(c1.name)
# print(c2.name)
'''******over*****'''

# class employe:
#     def __init__(self,sal,ag):
#         self.salary=sal
#         self.age=ag
#     def show(self):
#         print(f'salary is {self.salary} and age is {self.age}')

# e1=employe(2500,25)
# e2=employe(35000,30)

# print(e1.age)
# print(e2.salary)
# e1.salary=2000
# print(e1.salary)

# e1.show()
# e2.show()

'''*******oveer******'''
# # coplit
# class bike:
#     name=""
#     gaer=0
# bike1=bike()
# bike1.name='kbz'
# bike1.gaer=5
# print(bike1.name)
# print(bike1.gaer)

# class bike:
#     def __init__(self,name,gear):
#         self.name=name
#         self.gear=gear
# class mountainbike(bike):
#     def __init__(self,name,gear,suspension):
#         super().__init__(name,gear)
#         self.suspension=suspension
#     def show(self):
#         print(f"name:{self.name} gear:{self.gear} sespensation:{self.suspension}")


# bk1=mountainbike('bmx',6,'high')
# bk2=mountainbike('bmw',3,'modernate')
# bk3=bike('atles','chain')
# print(bk1.name)
# print(bk1.gear)
# print(bk1.suspension)
# print(bk2.suspension)
# print(bk2.suspension)
# bk2.gear=4
# print(bk2.gear)

# bk1.show()
# bk2.show()

# class Animal:
#     def speak(self):
#         pass  

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog_instance = Dog()
# cat_instance = Cat()

# print(dog_instance.speak())  
# print(cat_instance.speak())  

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def getname(self):
#         return self.name

#     def getage(self):
#         return self.age
    
#     def setage(self,new_age):
#         if new_age >=0:
#             self.age=new_age

# person1=person('alex',25)
# person2=person('syed',20)
# print(f'name:{person1.getname()} age:{person1.getage()} ')
# print(f'name:{person2.getname()} age:{person2.getage()} ')

# person1.setage(35)
# print(f'name:{person1.getname()} age:{person1.getage()} ')

# person2.setage(40)
# print(f'name:{person2.getname()} age:{person2.getage()}') 

# class Person:
#     def __init__(self, name, age):
#         self._name = name  
#         self._age = age    

#     def get_name(self):
#         return self._name

#     def get_age(self):
#         return self._age

#     def set_age(self, new_age):
#         if new_age >= 0:
#             self._age = new_age

# person1 = Person(name="Alice", age=30)

# print(f"Name: {person1.get_name()}, Age: {person1.get_age()}")

# person1.set_age(35)
# print(f"Updated Age: {person1.get_age()}")


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number  # Private attribute
#         self._balance = balance  # Protected attribute

#     def deposit(self, amount):
#         self._balance += amount

#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#         else:
#             print("Insufficient funds!")

#     def get_balance(self):
#         return self._balance

# # Usage
# account = BankAccount(account_number="123456", balance=1000)
# account.deposit(500)
# account.withdraw(200)
# print(f"Account Balance: ${account.get_balance()}")

# f=open('C:/Users/Syed Ibrahim/Desktop/ibrahim.txt','r')
# print(f.read())

# z=open('C:/Users/Syed Ibrahim/Desktop/syed.txt','w')
# print(z.write('hyderabad,tealangana' ))

# h=open('C:/Users/Syed Ibrahim/Desktop/ansar.txt','w')
# print(h.write('shabir is a'))

# f=open('python2.py','w')
# print(f.write('hey how are u!is every thing is fine.'))
# text=f.write('hey how are u!is every thing is fine.')
# print(text)
# f.close()

# with open('python1.py', 'r') as f:
#     file_content = f.read()
#     print(file_content)

# f=open('python2.py','a')
# f.write('hi,world'  'how are u')
# f.close

# with open('myfile.txt','a') as z:
#     z.write('ar rahman')

# f=open('demo.txt','w')
# f.write('i want to go to trip 123')
# f.close()

f=open('C:/Users/Syed Ibrahim/Desktop/.txt','w')
print(f.write('ansar is serious'))