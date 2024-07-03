class Person():
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.__phone_number = phone_number
    def __welcome(self):
        print("Hello", self.name)
        print("Welcome To My World")

    def welcome(self):
        self.__welcome()
    def get_phone_number(self):
        print(self.__phone_number)

per1 = Person("Sishir Siam", 20, "01317129349")

print(per1.name, per1.age)
per1.welcome()
per1.get_phone_number()

