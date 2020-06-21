
class Vector:
    __secretCount = 0  # private 私有变量
    _protectedParm=100 #protected类型变量，允许本类和及其子类访问
    publicCount = 1  # public 公开变量

    def __init__(self,a,b):
        """
        构造方法
        :param a:
        :param b:
        """
        self.a=a
        self.b=b

    def __str__(self):
        return 'Vector(%d, %d)'% (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
print(v1.publicCount)
#不能直接访问私有变量，需要特殊处理
print (v1._Vector__secretCount)