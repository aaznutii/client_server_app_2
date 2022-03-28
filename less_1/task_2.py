"""
2. Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1) для перебора ip-адресов из
заданного диапазона. Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться
соответствующее сообщение.
"""
import sys
sys.path.append('../')
from ipaddress import ip_interface
from task_1 import host_ping


def host_range_ping(ip_range, ip_addr):
    ip_net = ip_interface(ip_addr)
    range_ip_lst = list(ip_net.network)[int(ip_range[0]):int(ip_range[1] + 1)]
    host_ping(1, range_ip_lst)


def main():
    ip_addr = '80.0.1.0/28'
    ip_range = (3, 10)
    host_range_ping(ip_range, ip_addr)


if __name__ == '__main__':
    main()