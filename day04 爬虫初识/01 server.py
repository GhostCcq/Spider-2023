#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   01 server.py
@Time    :   2023/09/20 22:54:30
@Author  :   GhostC 
@Version :   1.0
'''
import logging
from logging.handlers import RotatingFileHandler
import socket

def log_config():
  LOG_FORMAT = '[%(asctime)s][%(levelname)s]: %(message)s'
  level = logging.INFO
  logging.basicConfig(level=level, format=LOG_FORMAT)
  #创建RotatingFileHandler对象,满2MB为一个文件，共备份3个文件
  log_file_handler = RotatingFileHandler(filename='test.log', maxBytes=2*1024*1024, backupCount=3)
  # 设置日志打印格式
  formatter = logging.Formatter(LOG_FORMAT)
  log_file_handler.setFormatter(formatter)
  logging.getLogger('').addHandler(log_file_handler)


def socket_server():
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8888))
    sk.listen(5)
    logging.info('server is waiting...')
    conn, addr = sk.accept()
    data = conn.recv(1024)
    logging.info(f'conn--->{conn}, addr--->{addr}, data--->{data}')
    message = conn.send(b'message has receivesd')
    logging.info(f'message--->{message}')
def main():
    log_config()
    socket_server()
    socket_server()

if __name__ == '__main__':
    main()


