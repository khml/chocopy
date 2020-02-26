# -*- coding:utf-8 -*-


class Completer:
    def __init__(self, words):
        self._words = words
        self._prefix = None
        self._matching_list = []

    def complete(self, text: str, state: int):
        if text != self._prefix:
            self._prefix = text
            self._matching_list = [word for word in self._words if word.startswith(text)]
        try:
            return self._matching_list[state]
        except IndexError:
            return None
