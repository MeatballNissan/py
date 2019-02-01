# enumerate 取下标遍历
#

money = input("请输入你的金额：")
#money.isdigit() 判断是否数字
name = input("请输入你的姓名：")

car = [name,int(money),[]]
goods = [(1,"iphone",4000),(2,"mac",14000),(3,"bike",800),(4,"book",80)]

while True:
    for i in goods:
        a = ""
        for j in i:
            a += str(j) + " ";
        print(a);

    id = input("请输入你想购买的商品id：")
    if id == "q":
        print(car)
        break
    elif int(id)<1 or int(id)>len(goods):
        print("商品不存在")
    else:
        goodsMoney = goods[int(id) - 1][2]
        if car[1] >= goodsMoney:
            car[1] = car[1] - goodsMoney;
            car[2].append(goods[int(id) - 1])
            print("你购买了 %s,还剩钱\033[31;1m%s1\033[0m"%(str(goods[int(id) - 1][1]), str(car[1])))
        else:
            print("钱不够了，退出")
            print(car)
            break
