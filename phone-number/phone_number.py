class PhoneNumber:
    def __init__(self, number):
        for char in "-. +()":
            number = number.replace(char, "")
        if number[0] == '1':
            number = number[1:]
        if len(number) != 10:
            raise ValueError("Phone number must be 10 digits")
        if not set([int(num) for num in number]).issubset(set(range(10))):
            raise ValueError("Phone number must contan digits only")
        if int(number[0]) < 2 or int(number[3]) < 2:
            raise ValueError("Invalid format")

        self.number = number
        self.area_code = self.number[:3]
        self.first_3 = self.number[3:6]
        self.last_4 = self.number[6:]

    def pretty(self):
        return f"({self.area_code})-{self.first_3}-{self.last_4}"
