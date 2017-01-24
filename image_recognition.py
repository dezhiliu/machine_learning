from PIL import Image
import os
import numpy


# 遍历指定目录，返回目录下的所有文件名
def each_file(filepath):
	file_list = []
	path_dir =  os.listdir(filepath)
	file_count = len(path_dir)

	for count in range(0, file_count):
		child = os.path.join('%s%s' % (filepath, str(count) + ".png"))
		file_list.append(child)
	return file_list

train_dataset_path = "C:\\Users\\Administrator\\Desktop\\MNIST\\train\\"
train_label_path = "C:\\Users\\Administrator\\Desktop\\MNIST\\label.txt"

# 循环读取所有训练数据
file_list = each_file(train_dataset_path)
file_ary_list = []

for path in file_list:
	# 将图片文件转为灰度值数据
	img = Image.open(path)
	img_array = img.load()
	file_ary_list.append(img_array)

label_ary = []
f = open(train_label_path) # 返回一个文件对象
line = f.readline() # 调用文件的 readline()方法
label_ary = line.split(",")

def compute_cost(ary1, ary2):
	print(ary2[1, 2])
	cost_price = 0
	for x in range(0, 28):
		for y in range(0, 28):
			cost_price = cost_price + (ary1[x, y]-ary2[x, y])**2
	return cost_price	

def get_result(input_str, ):
	img = Image.open(input_str)
	img_array = img.load()
	result_count = -1
	result_cost = 0
	count = 0
	for file_ary in file_ary_list:
		img_temp = Image.open(input_str)
		img_array_temp = img.load()
		cost_price = compute_cost(img_array, file_ary)
		if (result_count < 0 or cost_price < result_cost):
			result_count = count
			result_cost = cost_price
		count = count + 1
	print("cost_count: " + str(result_count) + ", cost_price: " + str(result_cost) + ", result: " + label_ary[result_count])
	return label_ary[result_count]
	

def image_recognition(train_dataset_path, train_label_path, ):
	# 输入一个新的图片地址，进行识别
	while (True):
		# 接收要识别的图片
		input_str = input("if you want exit, type exit ,else input picture path: ")
		if input_str == "exit":
			print("exit")
			break
		else:
			get_result(input_str)

def vaildate_success_rate(train_dataset_path, train_label_path, ):
	f = open("C:\\Users\\Administrator\\Desktop\\MNIST\\label_test.txt") # 返回一个文件对象
	line = f.readline() # 调用文件的 readline()方法
	test_label_ary = line.split(",")

	correct_count = 0.0
	for x in range(0,100):
		temp_result = get_result("C:\\Users\\Administrator\\Desktop\\MNIST\\test\\" + str(x) + ".png")
		if int(temp_result) == int(test_label_ary[x]):
			correct_count = correct_count + 1
	print("correct rate is : " + str(correct_count/100))

if __name__ == "__main__":
	#vaildate_success_rate(train_dataset_path, train_label_path, )

	image_recognition(train_dataset_path, train_label_path, )
		




	

