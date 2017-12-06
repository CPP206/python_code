#1. 获取用户要复制的文件名
olf_file_name = input("请输入要复制的文件名: ")

#2.打开要复制的文件
old_file = open(old_file_name, "r")

#3.test.py ---->test[附件].py

position = old_file_name.rfind(".")
new_file_name = old_file_name[:position]+"[附件]"+old_file_name[position:]

#新建一个文件
new_file = open(new_file_name, "w")


#5.从旧文件中读取数据，并且写入到新文件中去
while True：
	content = old_file.read(1024)

	if len(content) == 0:
		break
	else:
		new_file.write(content)

#6. 关闭2个文件
old_file.close()
new_file.close()