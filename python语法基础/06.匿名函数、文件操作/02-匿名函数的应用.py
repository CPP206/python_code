# nums = [11, 34,34,23,34,123,1,23,34,54,323,234,154,45]

#nums.sort()
#print(nums)

infos = [{"name": "laowang","age":10}, {"name":"xiaoming", "age":20}, {"name":"banzhang", "age":23}]


infos.sort(key = lambda x:x['age'])
infos.sort(lambda x:)
# sort方法有两个可选参数：key和reverse
#1、kry在使用时必须提供一个排序过程总调用的函数
#2、reverse实现降序排序，需要一个布尔值

print(infos)