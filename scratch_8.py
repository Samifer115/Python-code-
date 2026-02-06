from colorama import init, Fore, Back, Style

init()

print(Fore.CYAN + "Заголовок")
print(Fore.RED + Back.WHITE + Style.BRIGHT + "Увага!")
print(Style.RESET_ALL + "Звичайний текст")