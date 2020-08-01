from glob import glob
from contextlib import nullcontext


class Controller:

    def __init__(self, foo_a: callable, foo_b: callable, foo_c: callable):
        self.foo_a = foo_a
        self.foo_b = foo_b
        self.foo_c = foo_c
    
    def process_in(self):
        
        with nullcontext():
            self.foo_a()
            self.foo_b()
    
    def process_out(self):
        
        with nullcontext():
            self.foo_c()


control_dict = {}
specs_list = glob('specs_*.py')
for specs in specs_list:
    file = __import__(specs[:-3])
    foos = (file.foo_a, file.foo_b, file.foo_c)
    key = file.hashkey
    control_dict[key] = Controller(*foos)
