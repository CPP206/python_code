ticket = 1 #1表示有车票  0表示没有车票

knifeLenght = 48 #cm

#先判断是否有车票
if ticket == 1:
	print("通过了车票的检测，进入到了车站，接下来要安检了")

	#判断刀的长度是否合格：
	if knifeLenght <=10:
		print("通过了安检，进入到了候车厅")
		print("马上就要见到他了，很开心..")
	else:
		print("安检没有通过，等待公安处理..")
else:
	print("兄弟 你还没有车票，去个屁呀...")