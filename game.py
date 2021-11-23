"""Игра угадай число"""

import numpy as np



# количество попыток
count = 0

number = np.random.randint(1, 101) # загадываем число


while count<20:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")
    
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break #конец игры выход из цикла
