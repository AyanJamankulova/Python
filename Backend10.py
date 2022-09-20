# #Задача1
# name = input("Введите имя:")
# surname = input("Введите фамилию")
# print("Здраствуйте", name[0] +"."+surname)

######################################################################

# if True:
#    print('Условие ')

# num_1 = int(input("Ведите первое число:"))
# num_2 = int(input("Введите второе число:"))
# if num_1 > num_2:
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")
    
# number = int(input("Введите число:"))
# if number % 2 == 0:
#     print(number, "четное")
# else:
#     print(number, "нечетное")
    
# number = int(input("Введите число:"))
# if number == 10:
#     print("Десять")
# elif number == 20:
#     print("Двадцать")
# elif number ==100:
#     print("Сто")
# else:
#     print("Если условия не совпали срабатывает else")


# num_1 = 5
# num_2 = 40
# num_3 = 57
# #or - не строгий, and - строгий
# if num_1 > num_2 and num_1 > num_3:
#     print(num_1, "больше всех")
# elif num_2 > num_1 and num_2 > num_3:
#     print(num_2, "больше всех")
# else:
#     print(num_3, "больше всех")

# password = input("Введите пароль:")
# confirum_password = input("Потвердите пароль:")
# if password == "2020itrun" or confirum_password == "2020itrun":
#     print("Welcome")
# else:
#     print("Error")


#Задача1
# a = 10 
# b = 20
# if a < b:
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")
    
# #Задача2
# number = int(input("Введите число"))
# if number <0:
#     print('YES')
# else:
#     print('NO')

# #Задача3
# number = int(input("Введите число"))
# if number>100:
#     print('+')
# else:
#     print('-')

#Задача4
# mon = int(input())
# if mon >0 and mon <3 or mon ==12:
#     print("Зима")
# elif mon == 3 or mon == 4 or mon ==5:
#     print("весна")
# elif mon==6 or mon ==7 or mon ==8:
#     print("Лето")
# elif mon==9 or mon==10 or mon==11:
#     print("Осень")
# else:
#     print("Неправильный месяц")

# # #Задача5
# a = int(input())
# b = int(input())
# c = int(input())
# if a>10 and b>10 and c>10:
#     print("yes")
# else:
#     print("no")

# #Задача6
# a = int(input("Введите первое число:"))
# b = int(input("Введите втолрое число:"))
# c = int(input("Введите третье число:"))
# print((a > 0) +(b>0) +(c > 0))

#Задача7
# mon = int(input("Количество месяцев="))
# year = int(input("Количество лет="))
# print("Количество дней="+str(mon*29+year*348))

# #Задача8
# a = int(input('Введите число от 1 до 50'))
# if a<16:
#     print('Еще рано')
# elif a >=18 and a < 40:
#     print("Идем служить")
# else:
#     print("Уже не надо")

#######################################################################################

# lst = [1,2,3,]
# print(lst)

# my_list = ['один,' 'два,' 'три,']
# print(my_list)

# lst = [1, 2.0, True, [1,2,3,]]
# print(lst)

# numbers = ['один', 'два','три']
# numbers[1] = 'два'
# # print(numbers)
# print(numbers[2])

# cars = ["BMW","MERSEDES","LEXUS"]
# # print(cars[::-1])
# print(cars[1:3])
# cars.append("TESLA")
# cars.append("AUDI")
# cars.insert(0,"AUDI")
# cars.pop(0)
# cars.remove("LEXUS")
# print(cars)
# del cars[0:3]
# print(cars)

# contacts = ["Ayan","Diana"]
# find_name = input("Введите имя которую вы хотите найти:")
# if find_name.title() in contacts:
#     print("Контакт найден")
# else:
#     print("Не нашли")


# num_1 = int(input("Введите первое число:"))
# operation = input("+,-,*,/:")
# num_2 = int(input("Введите второе число:"))
# if operation == "+":
#     print(num_1 + num_2)
# elif operation == "-":
#     print(num_1 - num_2)
# elif operation == "*":
#     print(num_1 * num_2)
# elif operation == "/":
#     print(num_1 / num_2)
# else:
    # print("Неправильная операция")
    
    
    
    
# numbers = [0.1 , 10, 1, 3, 5, 100, 500, 30, 120000]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

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





# #Задача9
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215,
# 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 110]
# print(numbers.count(110))
###################################################################
# date = ()
# print(type(date))

# date = ("IT RUN",)
# print(type(date))

# lst = ['Лето','Зима','Осень']
# date = tuple(lst)
# print(date)

# tup = (1, 2.0, False, "Hello",[1,10,2],(10,30,50))
# print(tup)

# tup_cars = ("BMW","Lexus","Lotus")
# tup_cars[2] = "Tesla"
# tup_cars.append("Hello")
# print(tup_cars)
# tup_cars.remove("BMW")
# print(tup_cars)
#########################################

# lst_cars = ["BMW","Lexus","LOtus"]
# lst_cars[2] = "Tesla"
# print(lst_cars)

# lst_cars.append("Mersedes")
# print(lst_cars)

# lst_cars.remove("BMW")
# print(lst_cars)
#########################################33


# it_company = ("Google","Amazon","facebook","telegram","instagram")
# print(it_company[1:4:2])
# print(it_company[::-1])
# print(it_company)

# lst_it_company = list(it_company)
# print(lst_it_company)
# lst_it_company.append("Space X")
# print(lst_it_company)
# it_company = tuple(lst_it_company)
# print(it_company)

# a,b,c,d = ('Лето','Зима','Осень','Весна')
# print(c)

# name = 'Egor'
# age = '30'
# (name,age) = (age,name)
# print(name)
# # print(age)
######################################
# num1,num2,num3 = 10,20,30
# print(num1)

# num1 = "First"
# num2 = "second"
# num1,num2 = num2,num1
# print(num2)
# print(num1)

# # number = 88823234
# # name = "Dima"
# # print("Name" + name + str(number))
# # print(f"Name {name} {number}")


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
# password = input("ВВедите пароль:")
# password2 = input("Введите пароль:")
# if len (password)<8:
#     print("Короткий пароль!")
# elif "123" in password:
#     print("Простой пароль!")
# elif password2 != password:
#     print("Различаются.")
# else:
#     print("OK")
    
##############################################################################################################################

# num1 = 10
# num2 = 20
# if num1==10 or num2==10:
#     print("First")
# elif num1 ==20 or num2==20:
#     print("Second")
# else:
#     print("Error")


# ######################################
# number = int(input("Введите число:"))
# # if number %2 == 0:
# #     print("Четное")
# # else:
# #     print("Нечетное")
    
# #Тернарныц оператор
# number = int(input("Введите число:"))
# res = "Четное" if number %2 == 0 else "Нечетное"
# print(res)

# #Сокращение тернарного оператора1
# number = int(input("Введите число:"))
# print("Четное") if number%2 ==0 else print("нечетное")

# #Пример2
# num1 = int(input("Введите первое число:"))
# num2 = int(input("Введите второе число:"))
# if num1>num2:
#     print("Первое число больше")
# else:
#     print("Второе число больше")
    
# #Тернарный оператор 2
# num1 = int(input("Введите первое число:"))
# num2 = int(input("Введите второе число:"))
# res = "Первое число больше" if num1>num2 else "Второе число больше"
# print(res)

# num= int(input("Введите число:"))
# res = ("Нечетное","Четное")[num%2 ==0]
# print(res)

# num1 = 20000
# num2 = 4000
# num3 = 1000
# result = "Первое число" if num1>num2 and num1>num3 else "Второе число" if num2>num1 and num2>num3 else "Третье"
# print(result)

# #Задача1
# age = int(input("Возраст:"))
# res = ("Доступ разрешен") if age>=18 and age<=50 else  ("Вы уже старый")  if age>50 else("Иди домой")
# print(res)

#Задача2
# my_password = ["qwerty","12345"]
# user_input = input("Введите пароль:")
# res = ("Парольный верный") if user_input in my_password else ("Неверный пароль") 
# print(res)

# #Задача3
# number = int(input("Пожалуйста введите цифру:"))
# res = ("Четным") if number%2 ==0 else ("Нечетным")
# print(res)

# #Задача4
# boolean = True
# res=(f'{boolean} является истиной') if boolean else (f'{boolean} является ложью')
# print(res)

# #Задача5
# name = input("Ваше имя:")
# names = ["Mark", "Kate", "Anna", "Smit"]
# res = (f"{name} в нашем классе") if name in names else (f"{name} не в нашем классе")
# print(res)

#####################################################################################################################################

# for i in range(1001):
#     print(i)
    
# numbers = [2,3,4,5,9,11,12,103,105,283]
# for num in numbers:
#     if num%2 == 0:
#         print(num,"Четный")
#     else:
#         print(num,"Нечетный")

# numbers = (2,3,4,5,9,11,12,103,105,283)
# for b in numbers:
#     print(b)
    
# it = "ITRUN"
# for a in it:
#     print(a)

# for b in range(0,10,3):
#     print(b)

# for i in range(1,101)


    
    
# numbers = [2,3,4,5,9,11,12,100,105,283]
# for i in numbers:
#     print(i)
#     if i == 100:
#         print("STOP ITERATION")
#         break


# numbers = [2,3,4,5,9,11,12,100,105,283]
# for i in numbers:
#     print(i)
#     if i == 100:
#         print("STOP ITERATION")
#         continue

# num1 = 10
# num2 = 30
# while num1<num2: 
#     print(num1)
    # num1 += 1
    
# num = 0
# while True:
#     num+=1
#     print(num)
#     if num == 10000:
#         break
    
        
# import time

# n =0
# while True:
#     n +=10
#     print(f"Hack {n}%")
#     time.sleep(0.5)
#     if n == 100:
#         print("Hacked")
        # break
        
# import random

# random_num = random.randint(1,10)
# n = 0
# while True:
#     user_num = int(input("Введите число с 1 до 10:"))
#     if user_num >0 and user_num <=10:
#         n +=1
#         if n == 3:
#             print("У вас закончились попытки")
#             break
#         elif random_num == user_num:
#             print("Вы выиграли!")
#             break
#         else:
#             print(f"Неправильно у вас {3-n} попыток")
#     else:
#         print("Написано же ввести цифру от 1 до 10")

#######################################################################################################3

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
        
# #Задача7
# n = 0
# while True:
#     a = int(input("ВВЕДИТЕ ЧИСЛО С 1 ДО 18:"))
#     if a==18:        
#         n +=1
#         print("Доступ разрешен!") 
#     while a<18:
#         print("Извините, пользование данным ресурсом только  с 18 лет")
#         break


###########################################################################################
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Деление на ноль")
  
    
# try:
#     print(10 +"10")
# except TypeError:
#     print("Ошибка типа: неподдерживаемые типы операндов для +:'int' и 'str'")

# # try:
# #     number1 = int(input("Введите первое число:"))
# #     number2 = int(input("Введите второе число:"))
# # except ValueError:
# #     print("Введите число!")

# # try:
# #     print(100/0)
# # except ZeroDivisionError:
# #     raise OSError("У вас ошибка в коде!")

# # try:
# #      print(100/1)  
# # except ZeroDivisionError:
# #     print("Деление на ноль") 
# # finally:
# #     print("Я все равно сработаю")

# # while True:
# #     try:
# #         num1 = int(input("Введите первое число:"))
# #         operation = input("*, /, +, -,:")
# #         num2 = int(input("Введите второе число:"))
# #         if operation == "+":
# #             print(num1 +num2)
# #         elif operation == "-":
# #             print(num1 - num2)
# #         elif operation == "/":
# #             print(num1 / num2)
# #         elif operation == "*":
# #             try:
# #                 print(num1*num2)
# #             except ZeroDivisionError:
# #                     print("Деление на ноль")
# #         else:
# #             print("Неправильная операция")
# #     except ValueError:
# #         print("Введите целое число")

# student = {'name': 'Adilet','age':17}
# print(student['age'])
# student['age'] = 18
# del student['age']
# print(student)
# print(student.get('age'))
# student.setdefault('key','value')
# student['hello'] = 'world'
# print(student)
# student.pop['name']
# print(student)

# student_dct = dict(name = 'Ayana', age = 15)
# print(student_dct)

# car = {'name':'Lexus', 'year':'2022','color':'red'}
# print(car.keys())
# print(car.values())
# print(car.items)
# for key, value in car.items():
#     print(key,value)

###############################################################################################33
#Задача1
#(try,except) используется для обработки исключений.
#исключения необходимы для того,чтобы сообщать программисту об ощибках.
#try - определяет блок кода в котором может произойти исключение,а блок except перехватывает их.

# #Задача2
# try:
#     print(328/0)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя!")

# #Задача3
# try:
#     print(283+"328")
# except TypeError:
#     print("Ошибка типов данных! Иди читай notion")

#Задача4
# h1,m1,s1 = (10,15,45)
# h2,m2,s2 = (15,25,30)
# print((h2-h1)*3600+(m2-m1)*60+(s2-s1))

#Задача5
# num =[]
# for i in range(1,401):
#     if i %2 ==0:
#         print([i,'Четный'])

# #Задача6
# dictionary_1 = {'a':300, 'b':400}
# dictionary_2 = {'c':500,'d':600}
# dictionary_3 = dictionary_1.copy()
# dictionary_3.update(dictionary_2)
# print(dictionary_3)

# # #Задача7
# numbers = {'num_1':1, 'num_2':2, 'num_3':3, 'num_100':100}
# for key in numbers:
#     numbers[key]*=5
# print(numbers)

# # #Задача8 
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# adilet['age']*=2
# print(adilet)

# #Задача9
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# del adilet['color']
# print(adilet)

# #Задача10
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# adilet['age']=18
# print(adilet)

# #Задача11
# adilet = {'name': 'Adilet','age':17, 'color': 'White'}
# adilet['address'] = 'Западный Анар'
# print(adilet)

#############################################################################################################

# a = [1,2,3,4,5]
# b = [2,3,4,5,6]
# c = a +b
# print(set(c))

# names = {"Adilet","Kurmanbek","Sardor","Adilet"}
# print(names)

# numbers= {1,2,3,4,5,6,7,8,9,10}
# print(numbers)

# logic = {1, 1.0, True}
# print(logic)

# strange_app = set('TikTok')
# print(strange_app)

# pangram = {'съешь же еще этих мягких фрвнцузких булок, да выпей чаю'}
# print(pangram)

# cars = ("BMW","TESLA","AUDI","TESLA","MERSEDES")
# set_cars = set(cars)
# print(set_cars)

# types = {1,2.0, False, "1",(10,20,30)}
# print(types)

# some_dict = {'key_one': 'val_one','key_two':'val_two'}
# some_set = set(some_dict)
# print(some_set) 

# card_suit = ['heart','diamond','club','spade','spade']
# suit_set = set(card_suit)
# print(suit_set)

# unbreakable_diamond = ['Jotaro','Josuke','Koichi',]
# golden_wind =['Jotaro','Giorno','Koichi',] 
# overlap = set(unbreakable_diamond) & set(golden_wind)
# print(overlap)

# it_company = {"Google","Tesla","Amazon"}
# it_company.add("Microsoft")
# print(it_company)

# # it_company.remove("Google")
# # print(it_company)

# # it_company.pop()
# # print(it_company)

# for i in it_company:
#     print(i)

# it_company = ["Google","Tesla","Amazon"]
# it_company.append("Microsoft")
# frzn_it = frozenset(it_company)
# print(frzn_it)

# nums = []
# for num in range(1,101):
#     nums.append(num)
# print(nums)

# nums = [num for num in range(1,101)]
# print(nums)

# nums = []
# for i in range(101):
#     if i%2 ==0:
#         nums.append(i)
# print(nums)

# nums=[ i for i in range(101)if i %2 ==0]
# print(nums)

# petrol = {
#     'Ai 100' : 60,
#     'Ai 95':55,
#     'Ai 92':50,
#     'Ai 80':40,
#     'DT' : 35
# }

# new_petrol = {}
# for name, price in petrol.items():
#     new_petrol.setdefault(name, price + 15)
# print(new_petrol)

# new_petrol = {name:price + 15 for name, price in petrol.items()}
# print(new_petrol)

#####################################################################################################
#Задача1
# numbers = {1,1,2,3,5,8,13,21,34,55,89}
# for elem in numbers:
#     if elem<5:
#         print(elem)
        
#Задача2
# numbers1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
# overlap = set(numbers1)& set(numbers2)
# print(overlap)

#Задача3
# names = {"anna","adilet","sardor","kurmanbek","alla"}
# for b in names:
#     if b [::-1] == b:
#         print(b)

#Задача4
# numbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
# 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, ]
# for b in numbers:
#     if b == 418:
#         break
#     elif b %2 == 0:
#         print(b)

# #########################################################################################################
# def hello():
#     print("Hello World")
    
# def it():
#     print("IT RUN")

# hello()
# it()

# def calc():
#     num1 =  int(input("Введите первое число:"))
#     num2 =  int(input("Введите второе число:"))
#     print(num1 + num2)
    
# calc()


# def calc (num1, num2):
#     print(num1 + num2)
    
# calc(10,10)

# def chet_nechet(number):
#     if number %2 == 0:
#         print(number,"четный")
#     else:
#         print(number,"нечетный")
# chet_nechet(2)
# chet_nechet(9)

# def ayan(number):
#     for b in range(1, number):
#         print(b)
        
# ayan(2007)

# def mult(num1 = 2, num2 = 3):
#     print(num1 * num2)
# mult()
# mult(100)
# mult(20,100)

#################################################################################################3
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

# #Задача2
# word = "Кыргызская Республика, Ruby On Rails, For You Interest"
# word_split = word.split()
# print(word_split[0][0] + word_split[1][0])
# print(word_split[2][0] + word_split[3][0]+word_split[4][0])
# print (word_split[5][0] + word_split[6][0]+word_split[7][0])

# #Задача3
# import re
# from collections import Counter
# t = "Money, Money, Money, its always sunny, in the richmens world"
# words = re.findall(r'\w+',t)
# words = [b. title() for b in words]

# for word, b in Counter (words).most_common():
#     print(word, b)

# #Задача4
# def main(word):
#     word_dict = list(word)
#     chat_bot = set(word)
#     if len(word_dict) == len(chat_bot):
#         return True
#     return False

# print(main('привет'))
# print(main('как ты'))

# #Задача5
# n1 = input("Введите число")
# n2 = n1[::-1]
# print('"перевернутое" ему число:', n2)

#########################################################################################################3
#Задача1
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

#Задача2
# def count_word(word):
#     word_split = word.split(",")
#     str_split = "".join(word_split).lower()
#     word_split = str_split.split()
#     for i in set(word_split):
#         print(word_split.count(i),i)
# count_word( "Money, money, money, it’s always sunny, in the richmen’s world")
#############################################################################################################
# def welcome(*names):
#     for name in names:
#         print(name, "welcome")

# welcome("Ayan","Diana","Hello")
# welcome(1,2,3,4,5)

# nums1 = [1,2,3,4,5]
# nums2 = [6,7,*nums1,8,9,10]
# print(nums2)

# def translate(**words):
#     for key, value in words.items():
#         print(key,value)

# translate(USA = "США", Russia = "Россия")

#####################################################################################################

#Задача1
# def word (name, *points):
#     print(name,points)
# word("Ayan", 5,4,6,7)

#Задача2
# def nums(*numbers):
#     for b in numbers:
#         print(b*2)
# nums(33,23,28,56,30)

#Задача3
# def func(*args):
#     for i in args:
#         print(i)
# func('Hello','Welcome','to','GeeksforGeeks')
        
#Задача4
# def ayan(owner,**kwargs):
#     print(f"Owner name: {owner}")
#     for cars,name in kwargs.items():
#         print(f"{cars}: {name}")
# ayan("Ayana", cars = "Lexus_UX")
    
#Задача5
# def ayan(**kwargs):
#     for key,value in kwargs.items():
#        print(key,value)
# ayan(firsname ="Muntasir", lastname = "IT",age=30, country = "USA",email = "mun@gmail.com",phone = "0987654")

#Задача6
# def trans(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# trans(Kyrgyzstan = "Кыргызстан" , China = "Китай", Korea = "Корея",France = "Франция", New_York = "Нью-Йорк")

#Задача7
# def lexus_UX(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# lexus_UX(Двигатель = "бензиновый(1987 см3)", Мощность = "150 л.с", Крутящий_момент_двигателя ="202 Н.м", Коробка_передач = "вариатор(0 ступеней)", Максимальная_скорость = "190км/ч", Расход_топлива = "0/0/5.8")

###########################################################################################################

# from index import students
# import index #импортировать сам модуль
# index.add(20,45)
# index.sub(45,20)
# print(index.it)

# from index import add, sub, it #импортировать отдельные определения из модуля
# add(10,100)
# sub(10,1)
# print(it)

# from index import* #импортировать все содержимое модуля сразу
# add(10,40)
# print(it)
# sub(10,20)
# students("Ayana","Diana")


    



















