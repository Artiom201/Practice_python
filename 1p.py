#1
first_num =9
second_num = 7.8
my_str = "start"
print(first_num, second_num,my_str)
first_num = 5.2
print(first_num, type(first_num))
third_num = first_num + second_num
print(third_num, type(third_num))
first_num += 5
second_num += first_num
second_num = int(second_num)
print(first_num, second_num)
my_str += "&stop"
print(my_str)
print(my_str * 5)

#2
path = "c:\\Users\\MainAdmin\\Desktop\\programs"
print(path)
path += "\\game.exe"
print(path)
path = "c:\\Users\\MainAdmin\\Desktop\\files"
path += "\\picture.png"
print(path)
path = "C:\\Games\\city simulator"
print(path)
print("ERROR:", path * 2)

#3

num_1 =7
num_2 = 10
num_3 =4
summ =num_1 + num_2 + num_3
print("Сумма всех чисел",summ )
num_1 =7.9
num_2 = 21.3
num_3 = float(num_3)
summ = num_1 + num_2 + num_3
print("Сумма всех не целых чисел:", summ)
num_1 =130
num_2 = 4
num_3 = 2
m = num_1 * num_2 * num_3
print("Произведение все что то там:", m)
devision = (num_1 / num_2) / num_3
print("деление чето там", devision)
num_1 = 2
num_2 = 3
num_3 = 4
print(num_1 ** num_2 ** num_3)
num_1 = 2
num_2 =8
num_3 = 5
print(((43 + num_1) + (num_2 + 67) - (num_3 * 2)) // 2)
