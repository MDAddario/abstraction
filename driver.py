from contextlib import suppress

from control import control_dict


if __name__ == '__main__':
    
    for key, controller in control_dict.items():
        with suppress(KeyError):
            print(f"The key is {key}:")
            controller.process_in()
            controller.process_out()
