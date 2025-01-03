
# "Tasodifiy raqamni top" o'yini

import random
from colorama import Fore, Style

isRunning = True
print(Fore.MAGENTA + "Chiqish uchun 'exit' deb yozing" + Style.RESET_ALL)

while isRunning:
    random_number = random.randrange(0, 10)
    try:
        userInput = input("Kompyuter sonning kiriting: ")
        if int(userInput) == random_number:
            print(Fore.GREEN + f"Tabriklaymiz siz to'g'ri topdingiz, kompyuter {random_number} ni o'ylagan edi." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Siz topa olmadingiz, kompyuter {random_number} ni o'ylgan edi." + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + "Iltimos, to'g'ri ma'lumot kirgazing!" + Style.RESET_ALL)
        isRunning = False


