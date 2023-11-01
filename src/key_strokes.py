from string import ascii_lowercase
from src.keyboard import keyboard_lines
from src.get_char_list import get_char_list

def key_strokes(keys):
    cap_next = False
    char_list = get_char_list(keys)
    new_string = ''
    
    i = 0
    while i < len(char_list):  
        if cap_next == True:
            if (char_list[i] == ' ' or char_list[i] == '\'' or char_list[i] == '.' or char_list[i] == '?' or char_list[i] == ';') and new_string[-1] == 'i':
                last_char_upper = new_string[-1].upper()
                new_string = new_string[:-1] + last_char_upper + char_list[i]
                cap_next = False
            elif char_list[i] not in ascii_lowercase:
                new_string += char_list[i]
            elif char_list[i] not in [' ', '\''] and new_string[-1] == 'i':
                new_string += char_list [i]
                cap_next = False
            else:
                new_string += char_list[i].upper() 
                cap_next = False
        else:
            new_string += char_list[i]
        
        if char_list[i] == '.' or char_list[i] == '?':
            cap_next = True
        
        if new_string[-1] == 'i' and (new_string[-2] == ' ' or new_string[-2] == '\'' or new_string[-2] == ','):
            cap_next = True

        i += 1
    
    if new_string[-1] == 'i' and new_string[-2] == ' ':
        new_string = new_string[:-1] + new_string[-1].upper()

    result_string = new_string[0:1].upper() + new_string[1:]

    return result_string   