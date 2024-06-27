from math import floor
from time import sleep


def loadingBar(position: int, length: int):
    interval: float = 1/length
    percentage: float = position/length
    end_str: str= '\r'

    previous_progress: int = floor((percentage - interval) * 100)
    current_progress: int = floor(percentage * 100)

    mod_prev: int = previous_progress - (previous_progress % 10)
    mod_current: int = current_progress - (current_progress % 10)

    if mod_current > mod_prev or position == 1:
        if mod_current == 100:
            end_str = '\n'

        arrow: str = '>'
        progress_bar: str = '='*((mod_current//10)*3)
        print(f'[{progress_bar}{arrow} {mod_current}%]', end=end_str)