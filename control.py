from os import listdir
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
spec_dir = 'specs'

for path in listdir(spec_dir):
    
    if '__pycache__' in path: continue
    
    name = path[:-3]
    mod = __import__(f"{spec_dir}.{name}", fromlist=[None])
    foos = (mod.foo_a, mod.foo_b, mod.foo_c)
    control_dict[name] = Controller(*foos)
