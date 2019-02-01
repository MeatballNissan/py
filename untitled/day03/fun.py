"""

def func1():
    return "hello";

print(func1())

def func2():
    print("hello")

x = func1()
y = func2()

print(x)
print(y)


import time
def test1():
    print("test1")
    logger("test1")
def test2():
    print("test2")
    logger("test2")

def logger(x):
    time_format = '%Y-%m-%d %X '
    logger_time = time.strftime(time_format)
    with open("bxd.txt", 'a') as file:
        file.write("\n")
        file.write(logger_time)
        file.write(x)

test1()
test2()
def test3():
    return 1,"2",[],()

def test4():
    return test1
print(test3())
print(test4())
print(test4()())

"""

def test1(x = 1,y = 2):
    print(x,y)
test1(y = 3,x=2)
