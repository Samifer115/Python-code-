file_path = input("Введіть шлях до файлу: ")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("\nВміст файлу:")
        print(content)

except FileNotFoundError:
    print("Помилка: файл за вказаним шляхом не існує.")

except PermissionError:
    print("Помилка: немає прав доступу до файлу.")

except Exception as e:
    print("Невідома помилка:", e)