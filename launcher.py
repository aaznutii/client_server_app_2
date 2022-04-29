
import subprocess

process = []

# Для запуска под виндовс пришлось поставить PyQt5 через консоль. Иначе не видел библиотеку.
# Возможное решение на перспективу - Иначе прописать в самом server.py положение библиотек. ил pyinstaller
# pyinstaller испытал в ветке py_to_exe. Повозился, но получилось.

def main():
    """
    Функция тестового запуска приложения
    :return:
    """
    process = []

    while True:
        action = input(
            'Выберите действие: q - выход , s - запустить сервер, k - запустить клиенты x - закрыть все окна:')
        if action == 'q':
            break
        elif action == 's':
            # Запускаем сервер!
            process.append(
                subprocess.Popen(
                    'python server.py',
                    creationflags=subprocess.CREATE_NEW_CONSOLE))
        elif action == 'k':
            print('Убедитесь, что на сервере зарегистрировано необходимо количество клиентов с паролем 123456.')
            print('Первый запуск может быть достаточно долгим из-за генерации ключей!')
            clients_count = int(
                input('Введите количество тестовых клиентов для запуска: '))
            # Запускаем клиентов:
            for i in range(clients_count):
                process.append(
                    subprocess.Popen(
                        f'python client.py -n test{i + 1} -p 123456',
                        creationflags=subprocess.CREATE_NEW_CONSOLE))
        elif action == 'x':
            while process:
                process.pop().kill()


if __name__ == '__main__':
    main()