import logging


logging.basicConfig(level=logging.DEBUG)

def log(func_name):
    def wrapper():
        logging.info("程序执行了")
        return func_name
    return wrapper


@log
def func5():
    print("执行函数")


func5()