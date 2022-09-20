#Задача1
# name = input("Введите имя:")
# surname = input("Введите фамилию:")
# print("Здраствуйте", name[0] +"."+surname)

#Задача2
# num1 = int(input("Введите первое число:"))
# num2 = int(input("Введите второе число:"))
# print(num1 + num2)

#Задача3
# stroka = input("Как дела?")
# print(stroka. upper())

#Задача4
# D = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
# tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
# nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
# irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
# Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
# anim id est laborum."""
# print(len(D))
# print(D.count("e"))

# #Задача5
# sideA = int(input("Длина:"))
# sideB = int(input("Длина:"))
# perimeter = (sideA + sideB)*2
# print("Периметр квадрата:",perimeter)

# sideA = int(input("Длина:"))
# sideB = int(input("Длина:"))
# area = sideA * sideB;
# print("Площадь квадрата",area)

# sideA = int(input("Длина:"))
# sideB = int(input("Ширина:"))
# perimeter = (sideA + sideB)*2;
# print("Периметр прямоугольника:",perimeter)

# sideA = int(input("Длина:"))
# sideB = int(input("ширина:"))
# area = sideA * sideB;
# print("Площадь прямоугольника:",area)

#Задача6

# product = int(input("Ввод:"))
# print(((product/100)*12)+product)


#################################################################

#Задача1
# a = 10
# b = 20
# if a>b:
#     print(a)
# else:
#     print(b)

# #Задача2
# a = int(input("Введите первое число"))
# b = int(input("Введите второе число"))
# if (a-b)==0:
#     print('YES')
# else:
#     print('NO')

# #Задача3
# num = int(input("Введите число"))
# if num>100:
#     print('+')
# else:
#     print('-')

#Задача4
# mon = int(input())
# if mon==1 and mon==12 or mon==2:
#     print("Зима")
# elif mon ==3 and mon ==4 or mon==5:
#     print("Весна")
# elif mon==9 or mon==10 and mon==11:
#     print("Осень")
# elif mon==6 and mon==7 and mon==8:
#     print("Лето")
# else:
#     print("Неправильный месяц")


#Задача5
# a = int(input())
# b = int(input())
# c = int(input())
# if a>10 and b>10 and c>10:
#     print("yes")
# else:
#     print("no")


#Задача6
# a = int(input("Введите первое число:"))
# b = int(input("Введите второе число:"))
# c = int(input("Введите третье число:"))
# print((a>0)+(b>0)+(c>0))


#Задача7
# mon = int(input("Количество месяцев="))
# year = int(input("Количество лет="))
# print("Количество дней="+str(mon*29+year*348))


#Задача8
# a = int(input('Введите число от 1 до 50'))
# if a<16:
#     print('Еще рано')
# elif a>=18 and a<40:
#     print("Идем служить")
# else:
#     print("Уже не надо");

#######################################################################

#Задача1
# city = ["Baghdad", " Bangkok", "Barcelona","Berlin", "Athens", "Amsterdam", "Beijing","Cairo","Chicago","Dubai", "Hanoi","Dublin","Kabul","Lima","Madrid"]
# print(city[2::7])

# #Задача2
# num = ["1","2","3","4","5"]
# print(num[::-1])

# #Задача3
# a = [1,3,4,5]
# b = [4,5,6,7]
# b.remove(4)
# b.remove(5)
# print(b)


# #Задача4
# num = [1,2,3,4,5]
# print(min(num))

# #Задача5
# num = [1,2,3,4,5]
# del num[:]
# print(num)


# #Задача6
# num = [1,2,3,4,5]
# print(sum(num))

# # #Задача7
# listnum = [1,2,3,4,5];
# print("The mean is =", sum(listnum)/len(listnum));

# #Задача8
# playlist = [1,2,3,4,5,6,7,8,9,10]
# # playlist[4],playlist[8]=playlist[8],playlist[4]
# print(playlist)




# #Задача9
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
# 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110]
# print(numbers.count(110))

# ########################################################################
# #Задача1
# it_company = ('Google','Amazon','Microsoft')
# lst_it_company = list(it_company)
# print(lst_it_company)
# lst_it_company.append("Tesla")
# print(lst_it_company)
# it_company = tuple(lst_it_company)
# print(it_company)

# #Задача2
# it_company = ('Google','Amazon','Microsoft')
# print(it_company[1])

# #Задача3
# lst_it_company = list(it_company)
# lst_it_company[0]="Apple"
# it_company = tuple(lst_it_company)
# print(it_company)

# #Задача4
# it_company = ('Apple','Amazon','Microsoft')
# print(it_company[0:3])

# #Задача5
# text_tuple = ('Experienced','programmers','in','any','other','language','can','pick','up','Python','very','quicly','and','beginners',
# 'find','the','clean','syntax','and','indentation','structure','easy','to','learn','What','your','appetite','with','our','Python','3','overiew')
# print(text_tuple.count("Python"))


# #Задача6
# password = input("Введите пароль:")
# password2 = input("Введите пароль:")
# if len (password)<8:
#     print("Короткий пароль!")
# elif "123" in password:
#     print("Простой пароль!")
# elif password2 != password:
#     print("Различаются.")
# else:
#     print("OK")
 ######   ######################################################################

# #Задача1
# age = int(input("Возраст:"))
# res = ("Доступ разрешен") if age>=18 and age<=50 else  ("Вы уже старый")  if age>50 else("Иди домой")
# print(res)

#Задача2
# my_password = ["qwerty","12345"]
# user_input = input("Введите пароль:")
# res = ("Парольный верный") if user_input in my_password else ("Неверный пароль") 
# print(res)

# # #Задача3
# number = int(input("Пожалуйста введите цифру:"))
# types = ("Четным") if number%2 ==0 else ("Нечетным")
# print(types)

# #Задача4
# boolean = True
# res=(f'{boolean} является истиной') if boolean else (f'{boolean} является ложью')
# print(res)

# #Задача5
# name = input("Ваше имя:")
# names = ["Mark", "Kate", "Anna", "Smit"]
# res = (f"{name} в нашем классе") if name in names else (f"{name} не в нашем классе")
# print(res)

# ################################################################################################

# #Задача1
# for i in range(5):
#     print("00000", i+1)

# #Задача2
# num = []
# for i in range(1,101):
#     num.append(i)
# print(num)

# #Задача3
# for i in range(1,497):
#     if i %2 == 0:
#         print(i, "Четный")
# #Задача4
# nums = []
# for num in range(1,1001):
#     nums.append(num)
# print(min(nums))
# print(max(nums))
# print(sum(nums))

# #Задача5    
# for i in range(100):
#     print(0)

# #Задача6
# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# a,b = b,a
# print(a)
# print(b)
        
#Задача7
# n = 0
# while True:
#     a = int(input("ВВЕДИТЕ ЧИСЛО С 1 ДО 18:"))
#     if a==18:        
#         n +=1
#         print("Доступ разрешен!") 
#     while a<18:
#         print("Извините, пользование данным ресурсом только  с 18 лет")
#         break

#############################################################################################

#Задача1
#(try,except) используется для обработки исключений.
#исключения необходимы для того,чтобы сообщать программисту об ощибках.
#try - определяет блок кода в котором может произойти исключение,а блок except перехватывает их.

# #Задача2
# try:
#     print(328/0)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя!")

#Задача3
# try:
#     print(283+"328")
# except TypeError:
#     print("Ошибка типов данных! Иди читай notion")

# #Задача4
# h1,m1,s1 = (10,15,45)
# h2,m2,s2 = (15,25,30)
# print((h2-h1)*3600+(m2-m1)*60+(s2-s1))

#Задача5
# num =[]
# for i in range(1,401):
#     if i %2 ==0:
#         print([i,'Четный'])

#Задача6
# dictionary_1 = {'a':300, 'b':400}
# dictionary_2 = {'c':500,'d':600}
# dictionary_3 = dictionary_1.copy()
# dictionary_3.update(dictionary_2)
# print(dictionary_3)

#Задача7
# numbers = {'num_1':1, 'num_2':2, 'num_3':3, 'num_100':100}
# for key in numbers:
#     numbers[key]*=5
# print(numbers)

#Задача8 
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# adilet['age']*=2
# print(adilet)

#Задача9
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# del adilet['color']
# print(adilet)

#Задача10
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# adilet['age']=18
# print(adilet)

#Задача11
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# adilet['address'] = 'Западный Анар'
# print(adilet)

####################################################################################################
#Задача1
# numbers = {1,1,2,3,5,8,13,21,34,55,89}
# for elem in numbers:
#     if elem<5:
#         print(elem)
        
# Задача2
# numbers1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
# overlap = set(numbers1)& set(numbers2)
# print(overlap)

# Задача3
# names = {"anna","adilet","sardor","kurmanbek","alla"}
# for b in names:
#     if b [::-1] == b:
#         print(b)

# Задача4
# numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
# 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, ]
# for b in numbers:
#     if b == 237:
#         break
#     elif b %2 == 0:
#         print(b)

######################################################################################################
#Задача1
# def chat_bot():
#     while True:
#         word = input("Напишите слово:")
#         if word == "":
#             print("Как классно когда ты молчишь. Продолжай в том же духе!")
#         elif word == "ВОТ ТАК!":
#             print("Успокойся")
#         elif "?" in word:
#             print("Конечно")
#         else:
#             print("ну и что")
# chat_bot()

#Задача2
# def short_split(word):
#     word_split = word.split()
#     new_lst = []
#     for b in word_split:
#         new_lst.append(b.title()[0])
#     res = "".join(new_lst)
#     print(res)

# short_split("Кыргызская Республика")
# short_split("Жаманкулова Аяна")
# short_split("Ruby on Rails")

#Задача3
# def count_word(word):
#     word_split = word.split(",")
#     str_split = "". join(word_split). lower()
#     word_split = str_split.split()
#     for i in set(word_split):
#         print(word_split.count(i),i)
# count_word ("Money, Money, Money, its always sunny, in the richmens world")
    
#Задача4
# def main(word):
#     word_dict = list(word)
#     chat_bot = set(word)
#     if len(word_dict) == len(chat_bot):
#         return True
#     return False

# print(main('привет'))
# print(main('как ты'))

#Задача5
# n1 = input("Введите число")
# n2 = n1[::-1]
# print('"перевернутое" число:', n2)
#################################################################################################
# Задача1
# def word (name, *points):
#     print(name,points)
# word("Ayan", 5,4,6,7)

# Задача2
# def nums(*numbers):
#     for b in numbers:
#         print(b*2)
# nums(245,456,789,967,283)

# Задача3
# def func(*args):
#     for i in args:
#         print(i)
# func('Hello','Welcome','to','GeeksforGeeks')
        
# Задача4
# def ayan(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# ayan(Owner = "Ayana", cars = "Lexus_UX")
    
# Задача5
# def ayan(**kwargs):
#     for key,value in kwargs.items():
#        print(key,value)
# ayan(firsname ="Muntasir", lastname = "IT",age=30, country = "USA",email = "mun@gmail.com",phone = "0987654")

# Задача6
# def trans(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# trans(Kyrgyzstan = "Кыргызстан" , China = "Китай", Korea = "Корея",France = "Франция", New_York = "Нью-Йорк")

# Задача7
# def lexus_UX(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# lexus_UX(Двигатель = "бензиновый(1987 см3)", Мощность = "150 л.с", Крутящий_момент_двигателя ="202 Н.м", Коробка_передач = "вариатор(0 ступеней)", Максимальная_скорость = "190км/ч", Расход_топлива = "0/0/5.8")


    








    


    

























