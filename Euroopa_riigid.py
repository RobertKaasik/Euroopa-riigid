from module import*
from random import*
Capitals={}
Capitals=dict()
Capitals["Нидерланды"]="Амстердам"
Capitals["Андорра"]="Андорра-ла-Велья"
Capitals["Греция"]="Афины"
Capitals["Сербия"]="Белград"
Capitals["Германия"]="Берлин"
Capitals["Швейцария"]="Берн"
Capitals["Словакия"]="Братислава"
Capitals["Бельгия"]="Брюссель"
Capitals["Венгрия"]="Будапешт"
Capitals["Румыния"]="Бухарест"
Capitals["Лихтенштейн"]="Вадуц"
Capitals["Мальта"]="Валлетта"
Capitals["Польша"]="Варшава"
Capitals["Ватикан"]="Ватикан"
Capitals["Австрия"]="Вена"
Capitals["Литва"]="Вильнюс"
Capitals["Ирландия"]="Дублин"
Capitals["Хорватия"]="Загреб"
Capitals["Украина"]="Киев"
Capitals["Молдавия"]="Кишинёв"
Capitals["Дания"]="Копенгаген"
Capitals["Португалия"]="Лиссабон"
Capitals["Великобритания"]="Лондон"
Capitals["Словения"]="Любляна"
Capitals["Люксембург"]="Люксембург"
Capitals["Испания"]="Мадрид"
Capitals["Белоруссия"]="Минск"
Capitals["Монако"]="Монако"
Capitals["Россия"]="Москва"
Capitals["Норвегия"]="Осло"
Capitals["Франция"]="Париж"
Capitals["Черногория"]="Подгорица"
Capitals["Чехия"]="Прага"
Capitals["Исландия"]="Рейкьявик"
Capitals["Латвия"]="Рига"
Capitals["Италия"]="Рим"
Capitals["Сан-Марино"]="Сан-Марино"
Capitals["Босния и Герцеговина"]="Сараево"
Capitals["Северная Македония"]="Скопье"
Capitals["Болгария"]="София"
Capitals["Швеция"]="Стокгольм"
Capitals["Эстония"]="Таллин"
Capitals["Албания"]="Тирана"
Capitals["Финляндия"]="Хельсинки"
Countries=["Нидерланды", "Андорра", "Греция", "Сербия", "Германия", "Швейцария", "Словакия", "Бельгия", "Венгрия", "Румыния", "Лихтенштейн", "Мальта", "Польша", "Ватикан", "Австрия", "Литва", "Ирландия", "Хорватия", "Украинa", "Молдавия", "Дания", "Португалия", "Великобритания", "Словения", "Люксембург", "Испания", "Белоруссия", "Монако", "Россия", "Норвегия", "Франция", "Черногория", "Чехия", "Исландия", "Латвия", "Италия", "Сан-Марино", "Босния и Герцеговина", "Северная Македония", "Болгария", "Швеция", "Эстония", "Албания", "Финляндия"]
for country in Countries:
    country=input("Введите страну: ")
    if country in Capitals:
        print("Столица страны "+country+": " +Capitals[country])
    else:
        print("В Европе есть такая страна или вы ввели страну которая находиться не в Европейском союзе " +country)
        v=input("Хотите внести " +country+ " в нашу коллекцию?\n1-[Да] или 0-[Нет]? ")
        if v=="1":
            ca=input("Введите столицу страны " +country+": ")
            Capitals.update({country: ca})
            p=input("У нас произошла ошибка, хотите исправить её?\n1-[Да] или 0-[Нет]? ")
            if p=="0":
                print("Адьйос Амиго")
            if p=="1":
                o=input("Введите правильно страну: ")
                l=input("Введите правильно столицу: ")
                Capitals.pop(country)
                Capitals.update({o: l})
