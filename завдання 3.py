import random

secret_number = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10, У тебе є 3 спроби, щоб його вгадати")

for i in range(1, attempts + 1):
    guess = int(input(f"Спроба {i}: Введи число: "))

    if guess == secret_number:
        print("Вітаємо! Ти вгадав число!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"На жаль, спроби закінчилися. Я загадав число {secret_number}.")