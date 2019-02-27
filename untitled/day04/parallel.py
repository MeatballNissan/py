
import time
#nginx 单线程模型 -------最简单的协程
def consumer(name):
    print(" %s 准备吃包子了" %name)

    while True:
        baozi = yield
        print("包子 %s 来了 被 %s 吃了" %(baozi, name))


c = consumer("bxd")
c.__next__()
b1 = "牛肉馅"
c.send(b1)
c.send("猪肉馅")
# __next__会调用yield（唤醒）   send不止调用yield，还会给其传值（唤醒并传值）
def producer(name):
    c = consumer('bxd')
    c2 = consumer('BXD')
    c.__next__()
    c2.__next__()
    print('老子开始做包子了')
    for i in range(10):
        time.sleep(1)
        print('做了两个包子')
        c.send(i)
        c2.send(i)

producer('b')
