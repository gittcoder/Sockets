import threading
from time import sleep

def print_something():
    i=10
    print("Hello There")

def print_ok():
    sleep(2)
    print("ok")

def main():
    print_something()
    print_ok()

if __name__=='__main__':
    t1=threading.Thread(target=print_something)
    t2=threading.Thread(target=print_ok)
    t1.start()
    t2.start()
    print("Hello")
    print("This is after threads finished")