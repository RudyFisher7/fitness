
# OOP's 4 fundamental principles
# 1. Encapsulation - bundle data and the methods that act on them together, protect/hide internal state
# 2. Polymorphism - derived-class objects can be used like super-class objects, methods can be overloaded for specialization
# 3. Inheritance - inherite behavior and/or data from super class, one mechanism that allows polymorphism to work
# 4. Abstraction - hide complexities and expose only what interfacing code needs to know to use, interfaces or abstract classes are 2 mechanisms for this

class Person:
    instance_count: int = 0

    @classmethod # Decorators start with @.
    def get_instance_count(cls) -> int:
        return cls.instance_count

    # A static method. Called on the class but doesn't have access to
    # any class variables or other info.
    @staticmethod
    def only_local_data_here() -> str:
        return "this static method didn't access any class info for returning this string"

    def __init__(self, in_name: str) -> None:
        self.name = in_name
        self._protected_name = "my protected name" # not enforced by interpretor, just a convention
        Person.instance_count += 1
    
    def __del__(self) -> None:
        Person.instance_count -= 1

    def __str__(self) -> str:
        return f"{{{self.name}}}"
    
    def __repr__(self):
        return self.__str__()

    # A method.
    # Has access to the object instance it is called on via the self argument.
    def get_protected_name(self) -> str:
        return self._protected_name

    def say_hi(self) -> str:
        return "hi"


class Captain(Person):
    instance_count: int = 0

    @classmethod
    def get_instance_count(cls) -> int:
        return cls.instance_count

    def __init__(self, in_name: str, in_ship_name: str) -> None:
        super().__init__(in_name)

        self.ship_name = in_ship_name
        Captain.instance_count += 1
    
    def __del__(self) -> None:
        super().__del__()
        Captain.instance_count -= 1

    def __str__(self) -> str:
        return f"{{{self.name}, {self.ship_name}}}"
    
    def __repr__(self):
        return self.__str__()
    
    def say_hi(self):
        return "ahoy"


# A function (not defined in a class).
def filter_by_name(name: str, obj: Person) -> bool:
    return obj.name == name


person = Person("Jane Smith")
person_2 = Person("John Smith")
person_2 = Person("Jeff Smith")
captain = Captain("Jack", "Interceptor")

print(f"people: {Person.instance_count}")
print(f"captains: {Captain.get_instance_count()}")
print(Person.only_local_data_here())

people: list[Person] = []
for i in range(100):
    if i % 3 == 0:
        people.append(Captain("Jane", "Pinto"))
    else:
        people.append(Person(f"person_name_{i}"))

janes = list(filter(lambda x: filter_by_name("Jane", x), people))

print(janes)