import logging
import pandas
from termcolor import colored

def loaddata(fn):
        return pandas.read_csv(fn,dtype='str').fillna('').to_dict(orient='records')

def MyLog(name,level):
        log = logging.getLogger(name)
        if not log.handlers:
            ch = logging.StreamHandler()
            ch.setLevel(level)
        
            fh = logging.FileHandler('my_output.log')
            fh.setLevel(logging.DEBUG)

            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s = %(message)s')
        
            fh.setFormatter(formatter)
        
            log.addHandler(ch)
            log.addHandler(fh)        
#        log.setLevel(level)
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
