import random

list_of_word = ["apple", "juicer", "nas", "dimon", "kotko", "digital"]
random_word = random.choice(list_of_word)
count_guess = int(input("Введіть кількість спроб: "))
new_list = ["*"] * len(random_word)

while True:
    if count_guess < 1:
        print("game over, спробуйте ще")
        break
    input_letter_or_words = input("Введіть слово або букву: ")

    if len(input_letter_or_words) == 1:
        if input_letter_or_words in random_word:
            for index, let in enumerate(random_word):
                if let == input_letter_or_words:
                    new_list[index] = let
            print("".join(new_list))
        else:
            count_guess -= 1
            print("Вашої літери немає")
            print(f"У вас лишилось {count_guess} спроб, {"".join(new_list)}")
        if "".join(new_list) == random_word:
            print(f"you win, your word is {random_word}")

    elif len(input_letter_or_words) > 1:
        if input_letter_or_words == random_word:
            print(f"Вітаю ви вгадали слово - це слово {input_letter_or_words}")
        else:
            count_guess -= 1
            print("Ви не вгадали слово")
            print(f"У вас лишилось {count_guess} спроб")


