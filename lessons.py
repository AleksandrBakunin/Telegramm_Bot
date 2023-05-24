HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today = []
tomorrow = []
others = []

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(today)
    print(tomorrow)
    print(others)
  elif command == "add":
    date = input("Введите дату: ")
    if date == "Сегодня":
        task = input("Введите название задачи:")
        today.append(task)
    elif date == "Завтра":
        task = input("Введите название задачи:")
        tomorrow.append(task)
    else:
        task = input("Введите название задачи:")
        others.append(task)
    print("Задача добавлена")
  elif command == "exit":
      print("Спасибо за использование! До свидания!")
      run = False
  else:
      print("Неизвестная команда")
