"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
(Внимание! Аргументом сабпроцеса должен быть список, а не строка!!! Крайне желательно использование потоков.)
"""
import chardet   # для получения актуальной кодировки
import subprocess
import platform
from ipaddress import ip_address
"""
Если верно понял ТЗ.
"""

COUNT = 1
IP_1 = ip_address('173.194.220.93')
IP_2 = ip_address('5.255.255.60')
PING_TO_LIST = [IP_1, IP_2]


def host_ping(count, ping_to_list):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    # Проходим по адресам
    for el in ping_to_list:
        args = ['ping', param, str(count), str(el)]
        resources = subprocess.Popen(args, stdout=subprocess.PIPE)
        # Декодируем сообщение
        resources = [line.decode(chardet.detect(line)['encoding']) for line in resources.stdout]
        # Определяем статус доступности ресурса
        result = f'Узел доступен: {el}' if 'Обмен пакетами' in resources[1] else f'Узел недоступен: {el}'
        print(result)



def main():

    host_ping(COUNT, PING_TO_LIST)


if __name__ == '__main__':
    main()
