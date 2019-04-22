# object = Object in java
class School(object):
    members = 0

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self, stu_obj):
        print("学员%s注册" % stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,teacher):
        print("老师%s招聘成功"%teacher.name)
        self.teachers.append(teacher)

class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    pass

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---info of Teacher :%s---
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        ''' % (self.name, self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching" % self.name)


class Student(SchoolMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
                ---info of Student :%s---
                Name:%s
                Age:%s
                Sex:%s
                StuId:%s
                Grade:%s
                ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self,amount):
        print('%s has paid tution for $%s' %(self.name,amount))


school = School('b school' ,'西丽')
t1 = Teacher("b1 teacher", 26, 'M',2000,"java")
t2 = Teacher("b2 teacher", 23, 'M',3000,"devOps")
s1 = Student("b1 student", 18,'M','000001','一年级')
s2 = Student("b2 student", 15,'M','000004','一年级')
t1.tell()
t2.tell()
school.enroll(s1)
school.enroll(s2)
school.hire(t1)
school.hire(t2)

# school.teachers[0].teach()
for teacher in school.teachers:
    teacher.teach()
for stu in school.students:
    stu.pay_tuition(200)