"""By using descriptors and creating classes for similar variable types,
It creates clean code and doesn't repeat itself
"""


class Character:
    def __set_name__(self, owner, name):
        self.name = name

    def __init__(self, max_length: int = 128, invalid_values: list = None):
        self.max_length = max_length
        if invalid_values is None:
            invalid_values = []
        self.invalid_values = invalid_values.copy()

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be string.")
        if len(value) > self.max_length:
            raise ValueError(
                f"Max length for value is {self.max_length} characters.")
        if value in self.invalid_values:
            raise ValueError(f"Value can'nt be {value}.")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = None


class Person:
    invalid_names = ["admin", "superuser"]
    first_name = Character(256, invalid_names)
    last_name = Character(invalid_values=invalid_names)
    username = Character(invalid_values=invalid_names)
    car = Character(max_length=64)

    def __init__(self, first_name: str, last_name: str,
                 username: str, car: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.car = car

    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}, "
                f"Username: {self.username}, Car: {self.car}")


if __name__ == "__main__":
    p = Person("Mohammad", "Dori", "dori-dev", "BMW")
    p.first_name = "John"
    p.last_name = "Gates"
    p.username = "john-gates"
    p.car = "Benz"
    print(p)
    del p.first_name
    del p.last_name
    del p.username
    del p.car
    print(p)
