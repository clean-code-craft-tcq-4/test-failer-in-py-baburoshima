pair_number_end = 25
correct_format_sep1_idx = 4
correct_format_sep2_idx = 13

def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = get_pairnumber(i,j) 
            [first_sep_idx,second_sep_idx] = get_separator_index(format_string(pair_number, major, minor))
            print(format_string(pair_number, major, minor))
    return pair_number,len(major_colors) * len(minor_colors),[first_sep_idx,second_sep_idx]

def format_string(pair_number, major_color, minor_color):
  return f'{pair_number} | {major_color} | {minor_color}'

def get_separator_index(formatted_string):
    [first_sep_idx,second_sep_idx] = [index for index, separator in enumerate(formatted_string) if separator == '|']
    return [first_sep_idx,second_sep_idx]

def get_pairnumber(major_color, minor_color):
    return major_color * 5 + minor_color

pair_number,result,[first_sep_idx,second_sep_idx] = print_color_map()
assert(result == 25)
assert(pair_number==pair_number_end)
assert([first_sep_idx,second_sep_idx]==[correct_format_sep1_idx,correct_format_sep2_idx])
print("All is well (maybe!)\n")
