from contextlib import suppress

from control import control_dict


if __name__ == '__main__':
    
    with suppress(KeyError):
        Pencil = control_dict['pencil']
        Pencil.process_in()
        Pencil.process_out()
