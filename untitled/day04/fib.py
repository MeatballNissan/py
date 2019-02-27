
#迭代器原理
def fib(max):
    n,a,b = 0,0,1
    while n < max:
#        print(b)
        yield b  #保存了函数的中断状态
        a, b = b, a + b  # t = (b, a+b) ; a = t[0]  ; b = t[1]
        n += 1
    return


f = fib(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())

for i in f:
    print(i)

try:
    print(f.__next__())
except StopIteration as e:
    print('error:',e.value)


