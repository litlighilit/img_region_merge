
import os.path as path
from os.path import dirname, join
def get_ext(fname: str) -> str:
    # eg 'tt.png' -> '.png'
    return '.'+fname.rsplit('.', 1)[1]
isabs = lambda p: not path.abspath(p)
