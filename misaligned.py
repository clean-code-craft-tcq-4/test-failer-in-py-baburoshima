pair_number_end = 25
pair_number_start = 1
major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_color_map():
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = get_pairnumber(i,j)
            [first_sep_idx,second_sep_idx] = get_separator_index(format_string(pair_number, major, minor))
            print(format_string(pair_number, major, minor))
            color_map.append((pair_number, [first_sep_idx,second_sep_idx]))
    return len(major_colors) * len(minor_colors),color_map

def format_string(pair_number, major_color, minor_color):
  return f'{pair_number:3} | {major_color:6} | {minor_color}' #added proper space to align separator

def get_separator_index(formatted_string):
    [first_sep_idx,second_sep_idx] = [index for index, separator in enumerate(formatted_string) if separator == '|']
    return [first_sep_idx,second_sep_idx]

def get_pairnumber(major_color, minor_color):
    return major_color * len(major_colors) + minor_color + 1

#Test function to check 
# 1.formating by separator index 
# 2. pair number within range (1,25)
def test_color_map(color_map):
    assert(color_map[0][0]==1) # check if the first pair number is 1
    for i in range(pair_number_start,pair_number_end):
        assert([color_map[i][1][0],color_map[i][1][1]]==[color_map[pair_number_end-i][1][0],color_map[pair_number_end-i][1][1]])
        assert(color_map[i][0] == i+1)

result,color_map = print_color_map()
assert(result == 25)
test_color_map(color_map)
print("All is well :)\n")
