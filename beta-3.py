

import random
import time
#
#
#Рыцарь
def role():
    print("Добро пожаловать в королевство")
    time.sleep(3)
    print("Выберите роль:")
    time.sleep(1)
    print("1.Рыцарь\n2.Король")
def Rpred1():
    print("Вы стали рыцарем великого королевства")
    time.sleep(3)
    print("Много участь и работая вы достигли чина полководца")
    time.sleep(3)
    print("Вам поручен один из полков великой армии")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("На королевство собираются нападать орки")
    time.sleep(3)
    print("Король ожидает достойного отпора")
    time.sleep(3)
    print("Выберите действия в бою")
    time.sleep(3)
    print("1.Агресивная тактика\n2.Тактика главнокомандуещего")
    time.sleep(3) 
def R1Bagrm():
    print("Вы атаковали войска орков")
    time.sleep(3)
    print("Увы они оказались сильнее")
    time.sleep(3)        
    print("Вы невовремя проявили свою агрессию")
    time.sleep(3)
    print("Ваше войска разбито, а вы погибли")
    time.sleep(3)
    print("Это нанесло урон по всей армии")
    time.sleep(3)
    print("Game Over!")
def R1Bagrp():
    print("Вы атаковали войска орков")
    time.sleep(1)
    print("Ваша агрессия оказалась очень кстати")
    time.sleep(3)
    print("Вам попалось войско неопытных орков ")
    time.sleep(3)
    print("Вы с легкастью одалели их")
    time.sleep(3)
    print("Бой выигран")
    time.sleep(3)
    print("Поздравляю вас!")
    time.sleep(3)
    print("Вы успешно прошли боевое крещение")
def R2Btakt():
    time.sleep(1)
    print("Вы атаковали войска орков")
    time.sleep(3)
    print("Вы отлично управляете полком")
    time.sleep(3)
    print("Тактика оказалась действующей")
    time.sleep(3)
    print("Ваше королевство победило орков")
    time.sleep(3)
    print("Орки отступили")
    time.sleep(3)
    print("Поздравляю вас!")
    time.sleep(3)
    print("Вы успешно прошли боевое крещение")
###
def Rpred2():
    print("Нынешний полководец состарился\n и хочет провести последнии года в спокойствии") 
    time.sleep(3)
    print("За вашу смелость вы назначены на его пост")
    time.sleep(3)
    print("Теперь вы руководите всей армией королевства")  
    time.sleep(3)
    print("Король очень надеется на вас")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("Орки не смогли выдержать поражение")
    time.sleep(3)
    print("Они снова обьявляют войну")
    time.sleep(3)
    print("Король выбирает между войной и миром")
    time.sleep(3)
    print("Вы можете советоваться с королём")
    time.sleep(3)
    print("1.Согласиться с войной\n2.Обьявить переговоры")       
def Rpereg():
    print("Переговоры прошли успешно")
    time.sleep(3)
    print("Вы договрились по некоторым аспектам с орками")
    time.sleep(3)
    print("Они передумали обьявлять войну")
    time.sleep(3)
    print("Вы оказывается еще и отличный политик")
    time.sleep(3)
    print("Король хватит вас")
def Rwar1():
    print("Вы решаете объявить войну")
    time.sleep(3)
    print("Вы с войском отправляетесь к границам государства")
    time.sleep(3)
    print("Пора принять первый бой")
    time.sleep(3)
    print("Выберите тактику")
    time.sleep(3)
    print("1.Тактика котла(окружение) 2.Динамичная атака 3.Стрела")
def Rtaktp(): #Тактика+(Котел и ДА)
    print("Тактика оказалась действующей")
    time.sleep(3)
    print("Вы успешно атаковали орков")
    time.sleep(3)
    print("Вы победили!")
    time.sleep(3)
    print("Орки отступили")
    time.sleep(3)
    print("Поздравляю вас")
def Rtaktm(): #Тактика стрела
    print("Вы атаковали орков")
    time.sleep(3)
    print("Тактика оказалась безуспешной")
    time.sleep(3)
    print("Вы потеряли много солдат")
    time.sleep(3)
    print("Вам пришлось отступать")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("Орки догнали вас и добили окончательно")
    time.sleep(3)
    print("Вы погибли")
    time.sleep(3)
    print("Game over!")
###
def Rpred3():
    print("После вашего сражения орки отступили")
    time.sleep(3)
    print("Позже произошло ещё несколько сражений")
    time.sleep(3)
    print("В итоге вы выиграли войну")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("Не стоило расслабляться...")
    time.sleep(3)
    print("Игра ещё не окончена")
    time.sleep(3)
    print("Орки неугомонные")
    time.sleep(3)
    print("Они собираются мстить")
    time.sleep(3)
    print("Приготовтесь дать последнее сражение")
    time.sleep(3)
    print("Выберите татику")
    time.sleep(3)
    print("1.Тактика котла(окружение) 2.Динамичная атака")
def Rbtlp():
    print("Вы атаковали орков")
    time.sleep(3)
    print("И атаковали успешно")
    time.sleep(3)
    print("Орки почуствовали ваще могущество")
    time.sleep(3)
    print("Они бегут")
    time.sleep(3)
    print("Теперь они точто не прийдут на ваши земли")
    time.sleep(3)
    print("В королевстве большой праздник")
    time.sleep(3)
    print("Вы стали героем!") 
def Rbtlm():
    print("Вы атаковали орков")
    time.sleep(3)
    print("Но эта тактика не прошла с ними второй раз")
    time.sleep(3)
    print("Они были готовы")
    time.sleep(3)
    print("Увы вы проиграли")
    time.sleep(3)
    print("Game over!")
###
def Rend():
    time.sleep(1.5)
    print("Вы стали поистине легендой")
    time.sleep(3)
    print("Вы победили во всех сражениях")
    time.sleep(3)
    print("Родина вам благодарна")
    time.sleep(3)
    print("Вы прошли игру!")
    time.sleep(1.5)
    print("Game End!")
#
#
#
role()
role=input()
if role=="1":
    Rpred1()
    battle=input()
    
    if battle=="1":
        a=random.randint(0,1)
        if a==0:
            R1Bagrm()
            exit()
        elif a==1:
            R1Bagrp()    
    elif battle=="2":
        R2Btakt()        

    Rpred2()
    vim=input()
    if vim=="1":
        Rwar1()
        takt1=input()
        if takt1=="2" or "3":
            Rtaktp()
        elif takt1=="1":
            Rtaktm() 
            exit()
    elif vim=="2":
        Rpereg()
    Rpred3()
    takt2=input()
    if takt2==takt1:
        Rbtlm()
        exit()
    elif takt2!=takt1:
        Rbtlp()
    Rend()

else: print("error") 

       
