from itertools import count
from os.path import exists, splitext
from typing import Literal


class SaveAnother:
    counter = count(0)

    def __init__(self, file: str, mode: Literal['r', 'w']):
        self.file = file
        self.mode = mode
        self.obj = None

    def __enter__(self):
        if exists(self.file):
            file_name, file_extension = splitext(self.file)
            incremented_file_name = '{}{}{}'.format(
                file_name, next(self.counter), file_extension
            )
            self.obj = open(incremented_file_name, self.mode)
            return self.obj
        self.obj = open(self.file, self.mode)
        return self.obj

    def __exit__(self, type, value, traceback):
        print(
            'Type: {} - Value: {} - Traceback: {}'.format(
                type, value, traceback
            )
        )
        self.obj.close()
