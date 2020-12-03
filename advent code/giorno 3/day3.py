pattern = {}
i=0
tree1 = 0
tree2 = 0
tree3 = 0
tree4 = 0
tree5 = 0


with open('input.txt', 'r') as liner:
    while True:
        cur_line = liner.readline()
        if cur_line == '':
            pattern[i] = cur_line
            break
        else:
            pattern[i] = cur_line
            i = i+1

line_length = len(pattern[0])-1
dict_length = len(pattern)

def general_calc_tree(right,down,line_length,dict_length):

    tree=0
    x = right
    y = down
    out= False

    while(not out):

        print(str(y))
        print(str(x))

        if pattern[y][x] == '#' and x <= line_length and y < dict_length:
            tree = tree+1
        
        buffx = line_length - x

        if x < line_length-right:
            print("a)")
            x=x+right
        else:
            print("b)")
            x=right-buffx

        if y < dict_length-down-1:
            print("c)")
            y=y+down
        else:
            print("d)")
            out = True
    
    return tree   
    

tree1 = general_calc_tree(1,1,line_length,dict_length)
tree2 = general_calc_tree(3,1,line_length,dict_length)
tree3 = general_calc_tree(5,1,line_length,dict_length)
tree4 = general_calc_tree(7,1,line_length,dict_length)
tree5 = general_calc_tree(1,2,line_length,dict_length)

print(tree1*tree2*tree3*tree4*tree5)
