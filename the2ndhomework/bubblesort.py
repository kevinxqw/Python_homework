#冒泡排序
#定义 循环所用到的i和j
i=0;
j=0;
#定义一个数组list1
list1 = [6,5,4,3,2,1]
#控制循环的次数，循环的次数为list1的长度-1，
for i in range(len(list1)-1):
    #打印循环次数
    print("这是第{}次循环".format(i))
    #控制排序的次数，排序次数为list1的长度-1再减去i（已冒泡的次数）
    for j in range(len(list1)-i-1):
        #打印排序的次数
        print("这是第{}次排序".format(j))
        #进入排序循环，如果前面冒出来的数字小于后面的数字，则跳出此次排序
        if list1[j]<=list1[j+1]:
            continue
        #如果前面数字大于后面的数字，交换顺序
        else:
            list1[j],list1[j+1]=list1[j+1],list1[j]
        #打印排序后的结果
        print(list1)
#打印最终冒泡的结果
print("最终冒泡的结果为{}".format(list1))