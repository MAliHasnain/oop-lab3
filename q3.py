class person:
    year_of_birth = int(input('Enter year of birth : '))

    @classmethod
    def calculate_age(cls):
        age = 2022 - cls.year_of_birth
        #print('Your age is ',age)
        return age

    @staticmethod
    def check_age(a):
        if a > 18:
            return True

p1 = person()
print('Your age is: ',p1.calculate_age())
print(p1.check_age(p1.calculate_age()))