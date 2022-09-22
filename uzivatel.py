class uzivatel:
    def _init_(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        pass

    def print_info(self) -> str:
        return print(f"Meno: {self.first_name} Priezvisko: {self.last_name} Vek: {self.age}")
