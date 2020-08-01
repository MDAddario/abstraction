from control import control_dict


if __name__ == '__main__':
    
    for key, controller in control_dict.items():
        print(f"\nThe key is {key}:")
        controller.process_in()
        controller.process_out()
