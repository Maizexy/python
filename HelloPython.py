# Learn how to use Python
# Yuxi Wang
# 2020/5/20

import sys

# Print
'''
    ‘,’可以用于分开不同的数据类型，并且会print一个空格
    ‘+’只能用于相同数据类型
    “end = ''”可以使下一个print的内容不另起一行
'''
print("Hello World.")
name = "Python"
print("My name is", name, end="")
print(".")
print("%c is my %s letter and No.%d number is %.5f"  # %.5f即显示小数点后五位
      % ('x', 'favorite', 1, 1.14))

# 计算
'''
    +， -， *， /， **， //
    a**b （a的b次方）
    a//b （a/b,结果取整）
'''

# Variables
'''
    Numbers: （数字）
        为不可改变的数据类型
        int， long， float， complex（复数）
    Strings:（字符串）
        是由数字、字母、下划线组成的一串字符
        Python的字串列表有2种取值顺序:
            从左到右索引默认0开始的，最大范围是字符串长度减1
            从右到左索引默认-1开始的，最大范围是字符串开头
        从字符串中获取一段子字符串的话，可以使用变量 [头下标:尾下标]
            范围是:（顾头不顾尾，或左闭右开）
    Lists:（列表）
        可以存放不同数据类型
        支持字符，数字，字符串甚至可以包含列表（所谓嵌套）
        用[ ]标识，内部元素用逗号隔开
    Tuples:（元组）
        和列表类似，但不可二次赋值，相当于只读列表
        用( )标识
    Dictionaries:（字典）
        字典(dictionary)是除列表以外Python之中最灵活的内置数据结构类型。
        列表是有序的对象结合，字典是无序的对象集合。
        两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
        用"{ }"标识
        字典由索引(key)和它对应的值value组成。
'''

# String
string = "0123456789"
print(string)                 # 输出完整字符串
print(string[0])              # 输出字符串中的第一个字符
print(string[2:5])            # 输出字符串中第三个至第五个之间的字符
print(string[2:])             # 输出从第三个开始到最后的字符串
print(string*2)               # 输出字符串两次
print('say: ' + string)       # 输出连接的字符串

# List
List = ["One", "Two", "Three", "Two"]
print(List)

List.sort()
print(List)

List.remove("Two")
print(List)

del List[1]
print(List)
print(List[1])

List.insert(2, "Three")
print(List)

List.reverse()
print(List)

# Dictionary
Dict = {}
Dict['one'] = 'This is one'
Dict[2] = 'This is two'
tinyDict = {'name': 'john', 'code': 5762, 'dept': 'sales'}

print(Dict['one'])  # 输出键为'one'的值
print(Dict[2])  # 输出键为2的值
print(tinyDict)  # 输出完整的字典
print(tinyDict.keys())  # 输出所有键
print(tinyDict.values())  # 输出所有值

# if, elif, else, and, or
age = 21
if age >= 21:
    print('you can drink')
else:
    print('you cannot drink')

grade = 91
if (grade >= 80) and (grade < 90):
    print('you got a B')
elif (grade >= 90) and (grade <= 100):
    print('you got an A')

# for loop
for x in range(0, 10):  # 从0号开始，到10号的前一个为止
    print(x, ' ', end='')
print('\n')

'''
    for 遍历序列，若无 break 结束当前循环，则循环结束后执行 else 语句块
'''
nameList = ['woodman', 'Alan', 'Bobo']
for name in nameList:
    print(name)
else:
    print('循环完整结束后执行')

'''
    若有break 结束循环，则for 下的 else 不会执行
'''
for name in nameList:
    print(name)
    if name == 'Alan':
        break  # break 结束循环，for 下的 else 也不会执行
else:
    print('循环完整结束后执行')

'''
    若有continue 跳过本次循环，则进入下一次循环
    continue 只跳过本次循环，循环结束后 else 语句块最后被执行
'''
for name in nameList:
    if name == 'Alan':
        continue  # continue 跳过本次循环，进入下一次循环
    print(name)  # 如果被 continue 本条语句不会执行
else:
    print('循环完整结束后执行')

# Functions
def addNum(first, last):
    sum = first + last
    return sum
print(addNum(1, 5))

# Get input from user
print('what is your name?')
name = sys.stdin.readline()
print('Hello,', name)

# class
class Software:
    __name = ""
    __users = ""
    __score = 0 # from 0 to 10, 10 is the best

    def __init__(self, name, users, score):
        self.__name = name
        self.__users = users
        self.__score = score

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setUsers(self, users):
        self.__users = users

    def getUsers(self):
        return self.__users

    def setScore(self, score):
        self.__score = score

    def getScore(self):
        return self.__score

    def getType(self):
        print("Software")

    def toString(self):
        return "Most of the users of {} are {}.\nIts score is {}".format(self.__name,
                                                                        self.__users,
                                                                        self.__score)

Browser = Software('Google', 'the people who use Internet', 9.5)

print(Browser.toString())

class Game(Software):
    __gameType = ""

    def __init__(self, name, users, score, gameType):
        self.__gameType = gameType
        super(Game, self).__init__(name, users, score)

    def setGameType(self, gameType):
        self.__gameType = gameType

    def getGameType(self):
        return self.__gameType

    def getType(self):
        print("Game")

    def toString(self):
        return "{} is a {} game; most of the users of it are {}.\nIts score is {}".format(self.getName(),
                                                                                         self.__gameType,
                                                                                         self.getUsers(),
                                                                                         self.getScore())

CSGO = Game("CSGO", "students", 8.5, "FPS")

print(CSGO.toString())

Browser.getType()
CSGO.getType()