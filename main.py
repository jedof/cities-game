from ast import Break


def get_cities_list():
    cleaned_cities_list = []

    with open('cities.txt', encoding='utf-8') as f:
        cities = f.readlines()
        for city in cities:
            if city.strip():
                cleaned_cities_list.append(city.strip().replace('Оспаривается', ''))
    return cleaned_cities_list

cities = get_cities_list()
used_cities = []
score = 0

while True:
    print(f"Ваш счет {score}")
    user_choise = input("название города: ")
    if user_choise in cities:
        if user_choise not in used_cities:
            used_cities.append(user_choise)
            score += 1

            for city in cities:
                if city not in used_cities:
                    if user_choise[-1] == city[0].lower():
                        print("я выбераю город:", city)
                        used_cities.append(city)
                        break
        else:
            print("город уже использован, вы потеряли 1 бал")
            score -= 1
    else:
        print("такого города нет в России, вы потеряли 1 бал")
        score -= 1

    if score == 0:
        print("вы проиграли")
        break