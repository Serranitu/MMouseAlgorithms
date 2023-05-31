import sys
sys.path.insert(0, '..')
import API


def main():
    if not API.wallLeft():
        API.turnLeft()
    while API.wallFront():
        API.turnRight()
    API.moveForward()
