class Students:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} from {self.address}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Enter a value")
        self._name = name

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        if address not in ["Pune", "Mumbai", "Nasik", "Jalgoan", "Aurangabad"]:
            raise ValueError("Enter a valid address")
        self._address = address

    @classmethod
    def get(cls):
        name = input()
        address = input()
        return cls(name,address)

def main():
    student = Students.get()
    print(student)

if __name__ == "__main__":
    main()
