class Student:
    
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    def __str__(self):
        return f"Student 1: {self._name}, Age: {self._age}, Grade: {self._grade}"

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if type(new_name) == str and len(new_name) >= 3:
            for char in new_name.lower():
                if ord(char) >= 97 and ord(char) <= 122:
                    self._name = new_name.title()

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int):
            if new_age < 18 and new_age > 11:
                self._age = new_age 
    
    @property
    def get_grade(self):
         return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        if int(new_grade[:-2]) > 9 and int(new_grade[:-2]) < 12:
            if str(new_grade.endswith("th")):
                self._grade = new_grade

joseph = Student('joseph', 32, "12th")
Gary = Student("Gary", 33, "12th")

print(joseph)
