#Calculator application
import os

class calculator_api:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def op_add(self):
        return self.a + self.b

    def op_sub(self):
        return self.a - self.b


if __name__ == '__main__':
    obj_cal = calculator_api(3, 4)
    a = obj_cal.op_add()
    b = obj_cal.op_sub()
    print (f'Result ADD={a}')
    print (f'Result DUB={b}')


