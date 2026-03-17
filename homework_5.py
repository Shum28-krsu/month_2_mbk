class Distance:
    conversion_dict = {
        'cm': 0.01,
        'm': 1,
        'km': 1000
    }

    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return str(self.value) + " " + self.unit

    def __add__(self, other):
        total = self.convert() + other.convert()
        new_value = total / Distance.conversion_dict[self.unit]
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        total = self.convert() - other.convert()
        new_value = total / Distance.conversion_dict[self.unit]
        return Distance(new_value, self.unit)

    d1 = Distance(10, 'm')
    d2 = Distance(2, 'km')

    print(d1)
    print(d2)

    print(d1 + d2)
    print(d2 + d1)

    print(d2 - d1)