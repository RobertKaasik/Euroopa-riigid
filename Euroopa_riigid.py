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
while True:
    b=input("Просмотр столиц/стран-[1]\n")
    if b=="1":
        print("Если введете столицу то выведет город, и наоборот")
        a=input("Введите столицу или город:")
        if a.title()=="Нидерланды":
            print("Амстердам")
        elif a.title() =="Андорра":
            print("Андорра-ла-Велья")
        elif a.title() =="Греция":
            print("Афины")
        elif a.title() =="Сербия":
            print("Белград")
        elif a.title() =="Германия":
            print("Берлин")
        elif a.title() =="Швейцария":
            print("Берн")
        elif a.title() ==" Словакия":
            print("Братислава")
        elif a.title() =="Бельгия":
            print("Брюссель")
        elif a.title() =="Венгрия":
            print("Будапешт")
        elif a.title() =="Румыния":
            print("Бухарест")
        elif a.title() =="Лихтенштейн":
            print("Вадуц")
        elif a.title() =="Мальта":
            print("Валлетта")
        elif a.title() =="Польша":
            print("Варшава")
        elif a.title() =="Ватикан":
            print("Ватикан")
        elif a.title() =="Австрия":
            print("Вена")
        elif a.title() =="Литва":
            print("Вильнюс")
        elif a.title() =="Ирландия":
            print("Дублин")
        elif a.title() =="Хорватия":
            print("Загреб")
        elif a.title() =="Украинa":
            print("Киев")
        elif a.title() =="Молдавия":
            print("Кишинёв")
        elif a.title() =="Дания":
            print("Копенгаген")
        elif a.title() =="Португалия":
            print("Лиссабон")
        elif a.title() =="Великобритания":
            print("Лондон")
        elif a.title() =="Словения":
            print("Любляна")
        elif a.title() =="Люксембург":
            print("Люксембург")
        elif a.title() =="Испания":
            print("Мадрид")
        elif a.title() =="Белоруссия":
            print("Минск")
        elif a.title() =="Монако":
            print("Монако")
        elif a.title() =="Россия":
            print("Москва")
        elif a.title() =="Норвегия":
            print("Осло")
        elif a.title() =="Франция":
            print("Париж")
        elif a.title() =="Черногория":
            print("Подгорица")
        elif a.title() =="Чехия":
            print("Прага")
        elif a.title() =="Исландия":
            print("Рейкьявик")
        elif a.title() =="Латвия":
            print("Рига")
        elif a.title() =="Италия":
            print("Рим")
        elif a.title() =="Сан-Марино":
            print("Сан-Марино")
        elif a.title() =="Босния и Герцеговина":
            print("Сараево")
        elif a.title() =="Северная Македония":
            print("Скопье")
        elif a.title() =="Болгария":
            print("София")
        elif a.title() =="Швеция":
            print("Стокгольм")
        elif a.title() =="Эстония":
            print("Таллин")
        elif a.title() =="Албания":
            print("Тирана")
        elif a.title() =="Финляндия":
            print("Хельсинки")
        elif a.title() =="Амстердам":
            print("Нидерланды")
        elif a.title() =="Андорра-ла-Велья":
            print("Андорра")
        elif a.title() =="Афины":
            print("Греция")
        elif a.title() =="Белград":
            print("Сербия")
        elif a.title() =="Берлин":
            print("Германия")
        elif a.title() =="Берн":
            print("Швейцария")
        elif a.title() =="Братислава":
            print("Словакия")
        elif a.title() =="Брюссель":
            print("Бельгия")
        elif a.title() =="Будапешт":
            print("Венгрия")
        elif a.title() =="Бухарест":
            print("Румыния")
        elif a.title() =="Вадуц":
            print("Лихтенштейн")
        elif a.title() =="Валлетта":
            print("Мальта")
        elif a.title() =="Варшава":
            print("Польша")
        elif a.title() =="":
            print("Ватикан")
        elif a.title() =="Вена":
            print("Австрия")
        elif a.title() =="Вильнюс":
            print("Литва")
        elif a.title() =="Дублин":
            print("Ирландия")
        elif a.title() =="Загреб":
            print("Хорватия")
        elif a.title() =="Киев":
            print("Украина")
        elif a.title() =="Кишинёв":
            print("Молдавия")
        elif a.title() =="Копенгаген":
            print("Дания")
        elif a.title() =="Лиссабон":
            print("Португалия")
        elif a.title() =="Лондон":
            print("Великобритания")
        elif a.title() =="Любляна":
            print("Словения")
        elif a.title() =="Люксембург":
            print("Люксембург")
        elif a.title() =="Мадрид":
            print("Испания")
        elif a.title() =="Минск":
            print("Белоруссия")
        elif a.title() =="Монако":
            print("Монако")
        elif a.title() =="Москва":
            print("Россия")
        elif a.title() =="Осло":
            print("Норвегия")
        elif a.title() =="Париж":
            print("Франция")
        elif a.title() =="Подгорица":
            print("Черногория")
        elif a.title() =="Прага":
            print("Чехия")
        elif a.title() =="Рейкьявик":
            print("Исландия")
        elif a.title() =="Рига":
            print("Латвия")
        elif a.title() =="Рим":
            print("Италия")
        elif a.title() =="Сан-Марино":
            print("Сан-Марино")
        elif a.title() =="Сараево":
            print("Босния и Герцеговина")
        elif a.title() =="Скопье":
            print("Северная МакедонияСкопье")
        elif a.title() =="София":
            print("Болгария")
        elif a.title() =="Стокгольм":
            print("Швеция")
        elif a.title() =="Таллин":
            print("Эстония")
        elif a.title() =="Тирана":
            print("Албания")
        elif a.title() =="Хельсинки":
            print("Финляндия")
        else:
            c=input("В европе нет такой страны или столиции, хотите добавить" +Country+ "для красоты? - Да[1] нет[0]\n")
            if c=="1":
                l=input("Введите название столицы или страны: ")
                Capitals.update({Сountry: l})#Метод update вставляет указанные элементы в словарь.
            elif c=="0":
                print("Прощайте!")
globle()