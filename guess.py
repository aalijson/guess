import random   
NumberToGuess = random.randint(1,100)   
name = input('Введите ваше имя: ')
play1 = input('Введите любую клавишу, чтобы продолжить(нет - чтобы завершить): ')
guesses_made = 0
userGuess = -1        
while play1 != 'нет': 
    userGuess = int(input("Угадай число от 1 до 100: "))    
    guesses_made += 1  
    if userGuess > NumberToGuess:
        print("Число должно быть меньше!")      
    elif userGuess < NumberToGuess:         
        print("Число должно быть больше!")      
    else:         
        print(f'{name}, Вы угадали за {guesses_made} попыток/тки/тку, это число {NumberToGuess}')
        play1 = input('Хотите продолжить?(нет - чтобы завершить) ')
