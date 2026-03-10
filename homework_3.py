class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    def introduce(self):
        education = "I have master's degree" if self.__higher_education else "I haven't master's degree"
        print(f"HI, my name is {self.name}, I was born on {self.birth_date}, my occupation is {self.__occupation}. {education}")

    @property
    def occupation(self):
        return self.__occupation
    @occupation.setter
    def occupation(self, occupation):
        self.__occupation = occupation

    @property
    def higher_education(self):
        return self.__higher_education
    @higher_education.setter
    def higher_education(self, higher_education):
        self.__higher_education = higher_education

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        education = "I have master's degree" if self.higher_education else "I haven't master's degree"
        print(f"Hi, my name is {self.name}. I am a classmate from group {self.group_name}. I was born on {self.birth_date} and my occupation is {self.occupation}.{education}")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        education = "I have master's degree" if self.higher_education else "I haven't master's degree"
        print(f"Hi, my name is {self.name}. I am a friend. I was born on {self.birth_date}, I work as {self.occupation}. My hobby is {self.hobby}.{education}")


class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Our shared memory: {self.shared_memory}")

person1 = Person("Baibol", "17.11.2006", "software engineer", True)
person2 = Person("Azema", "08.05.2002", "theology", False)
person3 = Person("Aruuke", "20.04.2005", "international relations", True)

classmate1 = Classmate("Umar", "12.03.2007", "student", False, "GEEKS-64-1")
classmate2 = Classmate("Aktan", "04.07.2007", "student", False, "EPI-5-24")


friend1 = Friend("Bekmyrza", "27.12.2004", "programmer", True, "reading")
friend2 = Friend("Ayana", "23.06.2007", "designer", False, "scetching")

best_friend = BestFriend("Erzhan", "12.03.2007", "computer sciencer", True, "music", "Our school days")

people = [person1, person2, person3, classmate1, classmate2, friend1, friend2, best_friend]
for person in people:
    person.introduce()