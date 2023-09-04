from typing import Any, Dict, List, Optional, Tuple, Union


class RepeatQrCode:
    Group = {}

    def __init__(self) -> None:
        # self.Group = {}
        pass
    def add(self, gid: str):
        """
        新增猜歌群，防止重复指令
        """
        self.Group[gid] = {}

    def end(self, gid: str):
        """
        结束猜歌
        """
        del self.Group[gid]


repeatQR = RepeatQrCode()
