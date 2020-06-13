import pymysql
import settings

conn=pymysql.connect(host=settings.db["ip"],port=settings.db["port"],user=settings.db["user"],password=settings.db["password"],database=settings.db["database"],charset=settings.db["charset"])
cursor=conn.cursor();
cursor.execute("select version()")
data=cursor.fetchone();
print ("Database version : %s " % data)

#使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT * from student")
students=cursor.fetchall()
cursor.execute("SELECT * from student")
one=cursor.fetchone()
print(students)
print(one)

#增加数据
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   cursor.execute(sql)
   # 提交当前游标的全部操作
   conn.commit()
   print(22)
except:
   conn.rollback()

#关闭连接
cursor.close()
conn.close()
b=3.24j
print(b)
if(isinstance(b,complex)):
    print('complex')
else:
    print('others')
    print('else')
# print(hex(11))
# print(oct(10))
if 1<2 and 2>3:
    print(22)