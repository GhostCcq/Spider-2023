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


def socket_client():
    sk = socket.socket()
    sk.connect(('127.0.0.1', 8888))
    sk.send(b'hello world')
    res = sk.recv(1024)
    logging.info(f'服务端响应数据: {res.decode()}')

def main():
    log_config()
    socket_client()

if __name__ == '__main__':
    main()


