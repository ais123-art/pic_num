import numpy as np

number = np.random.randint(1, 101)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно
     или меньше нужного. Функция принимает загаданное число и возвращает число попыток '''
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 4
        elif number < predict:
            predict -= 5
    return (count) # выход из цикла, если угадали


def score_game(game_core_v2):
        '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
        count_ls = []
        np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
        random_array = np.random.randint(1, 101, size=(1000))
        for number in random_array:
            count_ls.append(game_core_v2(number))
        score = int(np.mean(count_ls))
        print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
        return (score)


# Проверяем
score_game(game_core_v2)

count = game_core_v2(number)

print(f"Вы угадали число {number} за {count} попыток.")
