
import subprocess

process = []

# Для запуска под виндовс пришлось поставить PyQt5 через консоль. Иначе не видел библиотеку.
# Возможное решение на перспективу - Иначе прописать в самом server.py положение библиотек. ил pyinstaller
# pyinstaller испытал в ветке py_to_exe. Повозился, но получилось.

process.append(subprocess.Popen(f'python server.py'))
while True:
    action = input('Выберите действие: q - выход , s - запустить сервер и клиенты, x - закрыть все окна:')
    if action == 'q':
        break
    elif action == 's':
        clients_count = int(input('Введите количество тестовых клиентов для запуска: '))

        # Запускаем клиентов:
        for i in range(clients_count):
            process.append(subprocess.Popen(f'python client.py -n test{i + 1}', creationflags=subprocess.CREATE_NEW_CONSOLE))
    elif action == 'x':
        while process:
            process.pop().kill()