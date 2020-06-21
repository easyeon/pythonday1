import  smtplib
from email.mime.text import MIMEText
from email.header import Header

sender="2452369568@qq.com"
host_qq = 'smtp.qq.com'
password_qq="bwjqdpghpzqbdjbe"
port_qq=25
receivers=["finbarr45@163.com"]

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message=MIMEText('python test send email.......','plain','utf-8')
message['From'] =Header('冯大师','utf-8')
message['To'] =Header('张天师')

subject='python send email'
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP(host=host_qq,port=port_qq)
    smtpObj.login(user=sender,password=password_qq)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print('发送邮件成功!')
except smtplib.SMTPException as e:
    print('error:发送邮件失败!')
    print(e)

