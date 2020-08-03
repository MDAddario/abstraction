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
for path in glob('specs/*.py'):

    if '__init__' in path: continue
    
    file = __import__(path[:-3].replace('/', '.'), fromlist=['foo_a', 'foo_b', 'foo_c'])
    foos = (file.foo_a, file.foo_b, file.foo_c)
    key = path[6:-3]
    control_dict[key] = Controller(*foos)
