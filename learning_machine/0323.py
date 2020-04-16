class Student:
    def __init__(self,new_gender,new_major, new_id):
        self.gender=new_gender
        self.__major =new_major
        self.id = new_id
    def get_gender(self):
        return self.gender
    def set_gender(self,new_gender):
        if new_gender == 'M' or new_gender =='F':
           self.gender = new_gender
        else:
            print('====請傳入F OR M=====')
    def join_class(self):
        pass
    def quit_class(self):
        pass

class Member:
    def __init__(self,new_gender,new_major,new_id):
            self.gender = new_gender
            self.__major = new_major
            self.id = new_id
    def get_gender(self):
            return self.gender

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
                self.gender = new_gender
        else:
                print('====請傳入F OR M=====')
    def borrow_resources(self):
        pass
    def check_auth(self):
        pass
class Student(Member):
    def __init__(self,new_gender,new_major,new_id):
        super().__init__(new_gender,new_major,new_id)
    def borrow_resources(self):
            print('student borrow')
    def join_class(self):
            pass
    def quit_class(self):
class Professor(Member):
    def __init__(self,new_gender,new_major,new_id):
        super().__init__(new_gender,new_major,new_id)
    def borrow_resources(self):
        print('professor borrow')

student1 = Student('M','工管系','D123456')
student2 = Student('F','數媒系','D555555')
professor1 =Professor('M','經濟系','D66666')
professor2 =Professor('F','經濟系','J66666')

studentA = Student('F','工管系','D0239567')
print(studentA.gender)
studentA.set_gender('g')
print(studentA.gender)


ls = [student1,student2,professor1,professor2]
for item in ls:
    item.borrow_resources()
