# coding=utf-8
"""
author = jamon
"""

import asyncio


class DataException(Exception):

    pass
    

class ObProtocol(asyncio.Protocol):
    """消息协议，包含消息处理"""

    def __init__(self):
        self.handfrt = "iii"  # (int, int, int)  -> (message_length, command_id, version)
        self.identifier = 0
        # self.encode_ins = None
        self.version = 0

        self._buffer = b""    # 数据缓冲buffer
        self._head = None     # 消息头

    def pack(self, data, command_id):
        """
        打包消息， 用於傳輸
        :param data:  傳輸數據
        :param command_id:  消息ID
        :return:
        """
        raise NotImplementedError

    def process_data(self, data):
        raise NotImplementedError

    def connection_made(self, transport):
        super(ObProtocol, self).connection_made(transport)

    def data_received(self, data):
        raise NotImplementedError

    def eof_received(self):
        raise NotImplementedError

    def connection_lost(self, error):
        super(ObProtocol, self).connection_lost(error)


