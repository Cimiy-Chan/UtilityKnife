#Calculator application
import os

class calculator_api:
    def __init__(self):
        pass

    def op_add(self, x, y):
        return x + y

    def op_sub(self, x, y):
        return x - y
    
    def op_mul(self, x, y):
        return x * y

    def op_div(self, x, y):
        return x / y

if __name__ == '__main__':
    obj_cal = calculator_api()
    a = obj_cal.op_add(4,3)
    b = obj_cal.op_sub(10,11)
    c = obj_cal.op_mul(5, 6)
    d = obj_cal.op_div(8,9)

    print (f'Result ADD={a}')
    print (f'Result SUB={b}')
    print (f'Result MUL={c}')
    print (f'Result DIV={d}')

# Add func -10
# Add func - 11
# Add func - 12
