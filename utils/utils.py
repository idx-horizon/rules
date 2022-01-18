import logging
from termcolor import colored

def MyLog(name,level):
        log = logging.Logger(name)
        log.addHandler(logging.StreamHandler())
        log.setLevel(level)
        return log

def NZ(arg):
        return arg if arg else ''

def traffic_light(score):
        if score[0] > 0:
                return colored('POSITIVE','green')
        elif score[0] < 0:
                return colored('NEGATIVE','red')
        else:
                return colored('NEUTRAL','yellow')

def convertTuple(tup):
    _ = ''
    for item in tup:
        _ = _ + str(item) + ','
    return _[:-1]
