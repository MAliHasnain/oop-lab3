class Student:
    def std_info(self):
        self.name=input("Enter the name of student: ")
        self.roll_no=input("Enter roll no. of student: ")
        self.email_address=input("Enter the email address: ")

    def courses(self):
        self.no_of_courses=int(input("Enter the no. of courses: "))
        self.course_credithr_dict={}
        for i in range(self.no_of_courses):
            self.courses_name=input("Enter the name of your course: ")
            self.credithr=int(input("Enter the credit hours of this course: "))
            self.course_credithr_dict[self.courses_name]=self.credithr
    @classmethod
    def calculate_gpa(cls):
        self.courses_gpa_dict = {}
        self.sum_of_credit_hrs = 0
        for j in self.course_credithr_dict:
            self.sum_of_credit_hrs += self.course_credithr_dict[j]
            course_marks = int(input(f'Enter marks of {j} : '))
            if 85 <= course_marks <= 100:
                self.courses_gpa_dict[j] = 4.0

            if 80 <= course_marks <= 84:
                self.courses_gpa_dict[j] = 3.7

            if 75 <= course_marks <= 79:
                self.courses_gpa_dict[j] = 3.4

            if 70 <= course_marks <= 74:
                self.courses_gpa_dict[j] = 3.0
            if 67 <= course_marks <= 69:
                self.courses_gpa_dict[j] = 2.7
            if 64 <= course_marks <= 66:
                self.courses_gpa_dict[j] = 2.4
            if 60 <= course_marks <= 63:
                self.courses_gpa_dict[j] = 2.0
        print("The GPA of the courses are as follows: ")
        for k in self.courses_gpa_dict:
            print(f'The GPA in {k} is: ',self.courses_gpa_dict[k])
    @classmethod
    def calculate_cgpa(cls):
        numerator_term=[]
        for l in self.courses_gpa_dict:
            prod=self.courses_gpa_dict[l]*self.course_credithr_dict[l]
            numerator_term.append(prod)

        numerator=sum(numerator_term)
        CGPA=numerator/self.sum_of_credit_hrs
        print(f'The CGPA of {self.name}is :',CGPA)

    @staticmethod
    def no_of_students(Batch):
        if Batch == 'First Year':
            no_of_students = 50
        elif Batch == 'Second Year':
            no_of_students = 75
        elif Batch == 'Third Year':
            no_of_students = 110
        elif Batch == 'Fourth Year':
            no_of_students = 120
        return no_of_students

Hasnain=Student()
Hasnain.std_info()
Hasnain.courses()
Hasnain.calculate_gpa()
Hasnain.calculate_cgpa()