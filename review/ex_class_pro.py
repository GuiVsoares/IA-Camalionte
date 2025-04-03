class People:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age: int):
        self._age = new_age


ana = People("Ana", 13)
print(f"Eu sou {ana.name} e tenho {ana.age} anos!")

ana.name = "Ana Maria"
ana.age = 18
print(f"Eu sou {ana.name} e tenho {ana.age} anos!!")
