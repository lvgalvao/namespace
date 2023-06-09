from contextlib import contextmanager
from os import chdir, getcwd

@contextmanager
def cd(path):
    old_path = getcwd()
    chdir(path)
    try:
        yield
    finally:
        chdir(old_path)

print(getcwd())
with cd('/'):
    print(getcwd())
print(getcwd())
