from random import randint, uniform


def main():
    current_color_action = None
    while True:
        if current_color_action is None:
            print('''
Please choose the color format for the generated color:
1. RGB
2. Hex
3. RGBA
4. HSL
5. HSLA
6. CMYK
            ''')

            choice = input('Enter your choice (or type "exit" to quit): ').strip().lower()
            if choice == 'exit':
                break

            action = color_format_actions.get(choice)
            if action:
                current_color_action = action
            else:
                print('Invalid choice. Please try again.')
                continue

        color_format, color = current_color_action()
        print(f'\nYou chose {color_format} format.\nGenerated color: {color}\n')

        responce = input('Do you want to copy this color to the clipboard? (pyperclip required; type "yes" or "no"): ').strip().lower()
        if responce == 'yes':
            try:
                from pyperclip import copy
                copy(color)
                print('The color has been copied to the clipboard.')
            except ImportError:
                print('Pyperclip is not installed. Clipboard functionality is unavailable.')

        again = input('Do you want to generate another color in the same format? (yes/no): ').strip().lower()
        if again != 'yes':
            reset = input('Do you want to choose a different color format? (yes/no): ').strip().lower()
            if reset == 'yes':
                current_color_action = None
            else:
                break


def generate_random_rgb_color() -> tuple[str, str]:
    color_format = 'RGB'
    color = f'{randint(0, 255)},{randint(0, 255)},{randint(0, 255)}'
    return color_format, color


def generate_random_rgba_color() -> tuple[str, str]:
    color_format = 'RGBA'
    color = f'{randint(0, 255)},{randint(0, 255)},{randint(0, 255)},{randint(0, 255)}'
    return color_format, color


def generate_random_hex_color() -> tuple[str, str]:
    color_format = 'HEX'
    color = f'{randint(0, 0xFFFFFF):06X}'
    return color_format, color


def generate_random_hsl_color() -> tuple[str, str]:
    color_format = 'HSL'
    color = f'{randint(0, 360)},{randint(0, 100)}%,{randint(0, 100)}%)'
    return color_format, color


def generate_random_hsla_color() -> tuple[str, str]:
    color_format = 'HSLA'
    color = f'{randint(0, 360)},{randint(0, 100)}%,{randint(0, 100)}%,{round(uniform(0, 1), 2)}'
    return color_format, color


def generate_random_cmyk_color() -> tuple[str, str]:
    color_format = 'CMYK'
    color = f'{randint(0, 100)}%,{randint(0, 100)}%,{randint(0, 100)}%,{randint(0, 100)}%'
    return color_format, color


color_format_actions = {
    '1': generate_random_rgb_color,
    '2': generate_random_rgba_color,
    '3': generate_random_hex_color,
    '4': generate_random_hsl_color,
    '5': generate_random_hsla_color,
    '6': generate_random_cmyk_color
}


if __name__ == '__main__':
    main()