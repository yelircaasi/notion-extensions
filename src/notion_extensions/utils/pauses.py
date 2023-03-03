import random
import time


def pause(min_length: float = 0.3, max_length: float = 0.8):
    time.sleep(min_length + (max_length - min_length) * random.random())


def minipause():
    pause(min_length=0.1, max_length=0.3)


def longpause():
    pause(min_length=2.5, max_length=3)
