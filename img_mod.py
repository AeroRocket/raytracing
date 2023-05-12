from size import size

def img_regen(picture):
    new_picture = []
    
    weight_table = [-1, 0, 1,
                    -1, 1, 1,
                    -1, 0, 1]


    for x in range(1, size[0]-1):
        line = []
        for y in range(1, size[0]-1):
            rgb_list = []
            for i in range(3):
                pixel_value = (picture[x-1][y-1][i]*weight_table[6] + picture[x][y-1][i]*weight_table[7] + picture[x+1][y-1][i]*weight_table[8] + picture[x-1][y][i]*weight_table[3] + picture[x][y][i]*weight_table[4] + picture[x+1][y][i]*weight_table[5] + picture[x-1][y+1][i]*weight_table[0] + picture[x][y+1][i]*weight_table[1] + picture[x+1][y+1][i]*weight_table[2])/9
                rgb_list.append(picture[x][y][i]*pixel_value)

            line.append(tuple(rgb_list))
        new_picture.append(line)


    return new_picture


            


