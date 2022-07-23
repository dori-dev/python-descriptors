"""Using property(getter), setter, deleter for all variables,
It creates similar(it repeats itself) code and the code is not clean!
"""


class Person:
    def __init__(self, first_name: str, last_name: str,
                 username: str, car: str):
        self.invalid_names = ["admin", "superuser"]
        self._str_validation(first_name, 256, self.invalid_names)
        self._str_validation(last_name, invalid_values=self.invalid_names)
        self._str_validation(username, invalid_values=self.invalid_names)
        self._str_validation(car, max_length=64)
        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._car = car

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}, Car: {self.car}"

    def _str_validation(self, value: str,
                        max_length: int = 128, invalid_values: list = None):
        if invalid_values is None:
            invalid_values = []
        if not isinstance(value, str):
            raise ValueError("Value must be string.")
        if len(value) > max_length:
            raise ValueError(
                f"Max length for value is {max_length} characters.")
        if value in invalid_values:
            raise ValueError(f"Value can'nt be {value}.")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._str_validation(value, 256, self.invalid_names)
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        self._first_name = None

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._str_validation(value, invalid_values=self.invalid_names)
        self._last_name = value

    @last_name.deleter
    def last_name(self):
        self._last_name = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        self._str_validation(value, invalid_values=self.invalid_names)
        self._username = value

    @username.deleter
    def username(self):
        self._username = None

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value: str):
        self._str_validation(value, max_length=64)
        self._car = value

    @car.deleter
    def car(self):
        self._car = None


if __name__ == "__main__":
    p = Person("Mohammad", "Dori", "BMW")
    p.first_name = "John"
    p.last_name = "Gates"
    p.car = "Benz"
    print(p)
    del p.first_name
    del p.last_name
    del p.car
    print(p)
