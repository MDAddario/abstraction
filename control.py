from contextlib import nullcontext


class Controller:

    def __init__(self, foo_a: callable, foo_b: callable, foo_c: callable):
        self.foo_a = foo_a
        self.foo_b = foo_b
        self.foo_c = foo_c
    
    def process_in(self):
        
        with nullcontext() as _:
            self.foo_a()
            self.foo_b()
    
    def process_out(self):
        
        with nullcontext() as _:
            self.foo_c()
