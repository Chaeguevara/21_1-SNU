class Member:
    def __init__(self, name: str, address: str, email: str, DoB: str, affiliation: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.DoB = DoB
        self.affiliation = affiliation
        self.infoList = [self.name, self.address,
                         self.email, self.DoB, self.affiliation]

    def printInfo(self):
        print(self.infoList)

    def switch_affiliation(self, new_affiliation:str):
        print("Memeber",self.name,"Changes affiliation",self.affiliation,"to",new_affiliation)
        self.infoList[4] = new_affiliation


class Student(Member):
    def __init__(self, name: str, address: str, email: str, DoB: str, affiliation: str, student_num: str) -> None:
        super().__init__(name, address, email, DoB, affiliation)
        self.student_num = student_num
        self.advisor = ""
        self.courses_taken = []
        self.courses_taking = []
        self.GPA = 0
        self.infoList += [self.student_num, self.advisor,
                          self.courses_taken, self.courses_taking, self.GPA]

    # def switch_affiliation(self, new_affiliation:str):
    #     print("Student",self.name,"Changes affiliation",self.affiliation,"to",new_affiliation)
    #     self.infoList[4] = new_affiliation

class Faculty(Member):
    def __init__ (self, name: str, address: str, email: str, DoB: str, affiliation: str, faculty_num: str) -> None:
        super().__init__(name, address, email, DoB, affiliation)
        self.faculty_num = faculty_num
        self.advisees = []
        self.courses_teaching = []
        self.infoList += [self.faculty_num, self.advisees, self.courses_teaching]
    
    # def switch_affiliation(self, new_affiliation:str):
    #     print("Faculty",self.name,"Changes affiliation",self.affiliation,"to",new_affiliation)
    #     self.infoList[4] = new_affiliation
        

a = Member("Heejin", "Seoul", "Dfso2", "1990", "Engineering")

print(type(a))
a.printInfo()

b = Student("Heejin", "Seoul", "Dfso2", "1990", "Engineering","2021-60777")
print(type(b))
b.printInfo()


c = Faculty("Heejin", "Seoul", "Dfso2", "1990", "Engineering","abcdd")
print(type(c))
c.printInfo()

a.switch_affiliation("Korean")
b.switch_affiliation("English")
c.switch_affiliation("Manage")

a.printInfo()
b.printInfo()
c.printInfo()