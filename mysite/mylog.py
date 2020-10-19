import pprint
import time


def log(data):
    with open("log.log", "a") as f:
        f.write(pprint.pformat(data))
        f.write('\n')
