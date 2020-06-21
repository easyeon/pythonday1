
class student:
    """
    学生类
    """
    stuCount=0;

    def __init__(self,name,age):
        """
        构造方法
        :param name:
        :param age:
        """
        self.name=name
        self.age=age
        self.stuCount+=1

    def disCount(self):
        """
        显示一共有多少学生
        :return:
        """
        print("现在学生人数："+self.stuCount)

    def displayStudent(self):
        """
        显示学生详细信息
        :return:
        """
        print("学生姓名："+self.name+" 年龄："+str(self.age))

stu=student("fengbin",24)
stu.displayStudent()
stu1=student("2334",3)
stu1.displayStudent()
print(getattr(stu,"age"))
setattr(stu,"age",0)
print(hasattr(stu,"sex"))
print(getattr(stu,"age"))
delattr(stu,"age")
print(hasattr(stu,"age"))
print("-----------------")
print ("Employee.__doc__:", stu.__doc__)
print ("Employee.__name__:", stu.__name__)
print ("Employee.__module__:", stu.__module__)
print ("Employee.__bases__:", stu.__bases__)
print ("Employee.__dict__:", stu.__dict__)


