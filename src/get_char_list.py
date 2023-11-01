from src.keyboard import keyboard_lines

def get_char_list(keys):
    char_list = []
    for coord in keys:
        char = keyboard_lines[coord[1]][coord[0]]
        char_list.append(char)
    return char_list