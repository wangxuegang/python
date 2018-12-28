#打印字符串
print("hello word")

#声明maxTo方法
def maxTo(a,b):
	if a > b:
		print(a)
	else:
		print(b)

#调用maxTo方法		
maxTo(3,2)		

#变量赋值
str = "你好，Python"

#打印str
print(str)

#变量赋值
x = 6;

#声明printFuc方法
def printFuc():
    y = 8
    z = 9
    print(y + z)
	
	#函数内部可以调用全局部变量,反之报错
    print(x)  

#调用printFuc方法	
printFuc()

#内容写入文件
text = "wangxuegang"

#内置open方法（打开或创建）w：表示write
wFile = open("demo_1.txt","w")
#写入内容
wFile.write(text)
#关闭资源
wFile.close()

#在文件里追加内容,a：表示append
aFile = open("demo_1.txt","a")
#写入内容
aFile.write(text)
#关闭资源
aFile.close()

#读取文件内容
rFile = open("demo_1.txt","r").read()
#打印内容
print(rFile)
