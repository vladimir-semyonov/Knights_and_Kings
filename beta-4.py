#beta-4
#Добавление роли короля
#Пока что отдельно от рыцаря
# *прописанна только роль короля

import random
import time
#
#
#Король
def role():
    print("Добро пожаловать в королевство")
    time.sleep(3)
    print("Выберите роль:")
    time.sleep(1)
    print("3.Рыцарь\n2.Король")
def Kpred():
    time.sleep(3)    
    print("Hello world!")
    time.sleep(3)
    print("Ладно это не всё")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("Вам очень повезло")
    time.sleep(3)
    print("Вы родились наследником короля")
    time.sleep(3)
    print("Ну очень большого королевства")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("Шли годы")
    time.sleep(3)
    print("Вы выросли")
    time.sleep(3)
    print("Пора становиться королём")
    time.sleep(1.5)
    print("...")

    time.sleep(1.5)    
    print("Вы стали королём")
    time.sleep(3)
    print("К сожалению ваш отец скончался")
    time.sleep(3)
    print("Он был великим королём")
    time.sleep(3)
    print("Надеюсь он оставил хорошего наследника")
    time.sleep(3)
    print("Это мы сейчас и проверим")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("Вам надо решить несколько вопросов")
    time.sleep(3)
    print("Помошники предложили принять несколько законов")
    time.sleep(3)
    print("Чтож начнём")
def Kz1():
    time.sleep(3)
    print("Первый закон предусматревает поддержку купцов вашего королевства")
    time.sleep(3)
    print("Для этого надо увеличить таможенные сборы")
    time.sleep(3)
    print("Выбирайте:")
    time.sleep(3)
    print("1.Принять закон\n2.Отказаться от принятия")
def Kz2():
    time.sleep(3)
    print("Следующий закон")
    time.sleep(3)
    print("Надо понизить уровень бедности")
    time.sleep(3)
    print("Для этого построим несколько государственных ферм")
    time.sleep(3)
    print("Бедняки будут на них работать")
    time.sleep(3)
    print("Приносить 50% урожая вам, остальное забирать себе")
    time.sleep(3)
    print("Выдадим также каждому по участку земли")
    time.sleep(3)
    print("Выбирайте:")
    time.sleep(3)
    print("1.Принять закон\n2.Отказаться от принятия")
def Kz3():
    time.sleep(3)
    print("Ещё один закон предусматривает постройку школ")
    time.sleep(3)
    print("Детям надо где-то учиться")
    time.sleep(3)
    print("А то уровень грамотности падает из года в год")
    time.sleep(3)
    print("Но на это прийдётся выделять много средств")
    time.sleep(3)
    print("Так что надо всё обдумать")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("Выбирайте:")
    time.sleep(3)
    print("1.Принять закон\n2.Отказаться от принятия")
def Kzp():
    print("Жители довольны вашим решением")
    print("Они рады таким поправкам")
    print("Вы отлично действуете")  
def Kzm():
    print("Жители недавольны вашим решением")
    print("Ваши советники также обеспокоены")
    print("Вы неверно поступили")
    

role()
role=input()
if role=="2":
    Kpred()
    Kz1()
    z1=input()
    if z1=="1":
       Kzp()
    elif z1=="2":
        Kzm()  
    Kz2()
    z2=input()
    if z2=="1":
       Kzp()
    elif z2=="2":
        Kzm() 
    Kz3()
    z3=input()
    if z3=="1":
       Kzp()
    elif z3=="2":
        Kzm() 
    
else: print("Error")

 


import random
import time
#
#
#Король
def role():
    print("Добро пожаловать в королевство")
    time.sleep(3)
    print("Выберите роль:")
    time.sleep(1)
    print("3.Рыцарь\n2.Король")
def Kpred():
    time.sleep(3)    
    print("Hello world!")
    time.sleep(3)
    print("Ладно это не всё")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("Вам очень повезло")
    time.sleep(3)
    print("Вы родились наследником короля")
    time.sleep(3)
    print("Ну очень большого королевства")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("Шли годы")
    time.sleep(3)
    print("Вы выросли")
    time.sleep(3)
    print("Пора становиться королём")
    time.sleep(1.5)
    print("...")

    time.sleep(1.5)    
    print("Вы стали королём")
    time.sleep(3)
    print("К сожалению ваш отец скончался")
    time.sleep(3)
    print("Он был великим королём")
    time.sleep(3)
    print("Надеюсь он оставил хорошего наследника")
    time.sleep(3)
    print("Это мы сейчас и проверим")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("Вам надо решить несколько вопросов")
    time.sleep(3)
    print("Помошники предложили принять несколько законов")
    time.sleep(3)
    print("Чтож начнём")
def Kz1():
    time.sleep(3)
    print("Первый закон предусматревает поддержку купцов вашего королевства")
    time.sleep(3)
    print("Для этого надо увеличить таможенные сборы")
    time.sleep(3)
    print("Выбирайте:")
    time.sleep(3)
    print("1.Принять закон\n2.Отказаться от принятия")
def Kz2():
    time.sleep(3)
    print("Следующий закон")
    time.sleep(3)
    print("Надо понизить уровень бедности")
    time.sleep(3)
    print("Для этого построим несколько государственных ферм")
    time.sleep(3)
    print("Бедняки будут на них работать")
    time.sleep(3)
    print("Приносить 50% урожая вам, остальное забирать себе")
    time.sleep(3)
    print("Выдадим также каждому по участку земли")
    time.sleep(3)
    print("Выбирайте:")
    time.sleep(3)
    print("1.Принять закон\n2.Отказаться от принятия")
def Kz3():
    time.sleep(3)
    print("Ещё один закон предусматривает постройку школ")
    time.sleep(3)
    print("Детям надо где-то учиться")
    time.sleep(3)
    print("А то уровень грамотности падает из года в год")
    time.sleep(3)
    print("Но на это прийдётся выделять много средств")
    time.sleep(3)
    print("Так что надо всё обдумать")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("Выбирайте:")
    time.sleep(3)
    print("1.Принять закон\n2.Отказаться от принятия")
def Kzp():
    print("Жители довольны вашим решением")
    print("Они рады таким поправкам")
    print("Вы отлично действуете")  
def Kzm():
    print("Жители недавольны вашим решением")
    print("Ваши советники также обеспокоены")
    print("Вы неверно поступили")
    

role()
role=input()
if role=="2":
    Kpred()
    Kz1()
    z1=input()
    if z1=="1":
       Kzp()
    elif z1=="2":
        Kzm()  
    Kz2()
    z2=input()
    if z2=="1":
       Kzp()
    elif z2=="2":
        Kzm() 
    Kz3()
    z3=input()
    if z3=="1":
       Kzp()
    elif z3=="2":
        Kzm() 
    
else: print("Error")

 
