from vpython import *
import random, math, time
import numpy as np

#The Pagoda Contour Generation
l_thickness = .2   #The Layer thickness
base_l_radius = base_brl_radius = 25   #The bottom layer radius
base_pos = -13
opac = .1

#COLORS
dana = vector(0.86, 0.51, 0.07)
sila = vector(0.43, 0.25, 0.04)
bhavana = vector(0.53, 0.49, 0.45)

def colors_list(dana_num, sila_num, bhavana_num):
    col_list = []
    for n in range(dana_num):
        col_list.append(dana)
    for m in range(sila_num):
        col_list.append(sila)
    for o in range(bhavana_num):
        col_list.append(bhavana)
    return col_list

pagoda = []

#The gradually narrowing cylindrical layers, each placed at the top of the preceding one
for m in range(1, 21):
    for n in range(11):
        pagoda.append(cylinder(color=color.white, opacity=opac, radius=base_l_radius - 3.5*n/m*l_thickness, axis=vector(0, 1, 0), pos=vector(0, base_pos + n*l_thickness, 0), length=l_thickness))
    base_pos += 10 * l_thickness
    base_l_radius -= 35/m*l_thickness

Shwe = compound(pagoda)
time.sleep(13)

#FILLING OF THE PAGODA SHAPE WITH BRICKS
br_length = 3
br_width = 2
br_height = 4 * l_thickness

#List of the brick positions within a single brick layer made of three pagoda layers
def layer_positions(l_number, section_num):
    positions = []
    y = -13 + l_number * br_height
    limit = base_brl_radius - 3.5*l_number*3/section_num*l_thickness
    for x in np.linspace(-limit, limit, int(2*base_brl_radius/br_length)):
        zlimit = int(math.sqrt(pow(limit,2)-pow(x,2))*.9)
        for z in np.linspace(-zlimit, zlimit, int(2*zlimit/br_width)):
            positions.append(vector(x, y, z))
    return positions
    
    
for layer in range(5):
    
    pos_list = layer_positions(layer, 1)
    l = len(pos_list)

    while l > 0:
        rate(1000)
        colors = colors_list(15, 3, 1)
        index = random.randrange(l)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list[index])
        time.sleep(.1)
        pos_list.pop(index)
        l -= 1

base_brl_radius -= 3.5*8*l_thickness

for layer2 in range(5, 10):
    pos_list2 = layer_positions(layer2, 2)
    l2 = len(pos_list2)
    
    while l2 > 0:
        rate(1000)
        colors = colors_list(1, 15, 3)
        index2 = random.randrange(l2)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list2[index2])
        time.sleep(.1)
        pos_list2.pop(index2)
        l2 -= 1

base_brl_radius -= 14*l_thickness
br_length = 2.6
br_width = 1.7

for layer3 in range(10, 17):
    pos_list3 = layer_positions(layer3, 3)
    l3 = len(pos_list3)
    
    while l3 > 0:
        rate(1000)
        colors = colors_list(1, 4, 20)
        index3 = random.randrange(l3)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list3[index3])
        time.sleep(.1)
        pos_list3.pop(index3)
        l3 -= 1

base_brl_radius -= 8*l_thickness
br_length = 1.5
br_width = 1.5

for layer3 in range(17, 35):
    pos_list3 = layer_positions(layer3, 5)
    l3 = len(pos_list3)
    
    while l3 > 0:
        rate(1000)
        colors = colors_list(1, 3, 30)
        index3 = random.randrange(l3)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list3[index3])
        time.sleep(.1)
        pos_list3.pop(index3)
        l3 -= 1

while True:
    pass