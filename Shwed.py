from vpython import *
import random, math, time
import numpy as np

#The Pagoda Contour Generation
l_thickness = .2   #The Layer thickness
base_l_radius = base_brl_radius = 25   #The bottom layer radius & the radius of the base layer of each section when laying bricks
base_pos = -13 #Setting how high the base of the pagoda will be displayed on the screen
opac = .1  #Transparency of the model

#COLORS - setting colors for bricks representing three kinds of actions: dana=act of giving, sila=act of restraining of unwholesome urges, bhavana=acts of mental cultivation
dana = vector(0.86, 0.51, 0.07)
sila = vector(0.43, 0.25, 0.04)
bhavana = vector(0.81, 0.75, 0.68)

#Helper function creating a list in which colors are given different weights (number of times that a color is repeated in the list) depending on which of the three types of actions are emphasized
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
time.sleep(30)

#FILLING OF THE PAGODA SHAPE WITH BRICKS
br_length = 3
br_width = 2
br_height = 4 * l_thickness

#Timing of the animation
tact = .2   #How frequently are bricks layed down
pause = 4

#List of the brick positions within a single brick layer made of four pagoda-model layers
def layer_positions(l_number, section_num):
    positions = []
    y = -13 + l_number * br_height
    limit = base_brl_radius - 3.5*l_number*3/section_num*l_thickness
    for x in np.linspace(-limit, limit, int(2*base_brl_radius/br_length)):
        zlimit = int(math.sqrt(pow(limit,2)-pow(x,2))*.9)
        for z in np.linspace(-zlimit, zlimit, int(2*zlimit/br_width)):
            positions.append(vector(x, y, z))
    return positions

#GRADUAL filling up the pagoda-model with bricks, section by section, each subsequent section having steeper sides than the preceding one

#The bottom section made primarily of "dana"-bricks, 5 layers representing 5 lifetimes of practice
for layer in range(5):
    
    pos_list = layer_positions(layer, 1)
    l = len(pos_list)

    while l > 0:
        rate(1000)
        colors = colors_list(15, 5, 1)
        index = random.randrange(l)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list[index])
        time.sleep(tact)
        pos_list.pop(index)
        l -= 1

#The 2nd section made primarily of "sila"-bricks, 5 layers representing 5 years of dependence on a qualified supervisor
base_brl_radius -= 28*l_thickness
time.sleep(pause)

for layer in range(5, 10):
    pos_list = layer_positions(layer, 2)
    l = len(pos_list)
    
    while l > 0:
        rate(1000)
        colors = colors_list(1, 15, 3)
        index = random.randrange(l)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list[index])
        time.sleep(tact)
        pos_list.pop(index)
        l -= 1
time.sleep(pause)

#The 3rd section made primarily of "bhavana"-bricks
base_brl_radius -= 14*l_thickness
br_length = 2.6
br_width = 1.7

for layer in range(10, 17):
    pos_list = layer_positions(layer, 3)
    l = len(pos_list)
    
    while l > 0:
        rate(1000)
        colors = colors_list(1, 4, 20)
        index = random.randrange(l)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list[index])
        time.sleep(tact)
        pos_list.pop(index)
        l -= 1
time.sleep(pause)

#The 4th section, made primarily of meditation bricks representing building of mental powers culminating in maturity for liberation
base_brl_radius -= 19*l_thickness
br_length = 1.5
br_width = 1.5

for layer in range(17, 35):
    pos_list = layer_positions(layer, 6)
    l = len(pos_list)
    
    while l > 0:
        rate(1000)
        colors = colors_list(1, 3, 30)
        index = random.randrange(l)
        box(color=colors[random.randint(0,len(colors)-1)], size=vector(br_length, br_height, br_width), pos=pos_list[index])
        time.sleep(tact)
        pos_list.pop(index)
        l -= 1
time.sleep(3*pause)

# #Adding the very top part of the pagoda, representing the event of penetration the truth, the quantum leap of enlightenment
# crown = []
# op = 0
# op_increase = .02
# base_radius = 3.5
# base_position = 9

# #This is basicaly the same process as at the beginning, just limited to the uppermost part, with the animation of gradually increasing opacity
# for m in range(12, 20):
#     for n in range(11):
#         rate(1000)
#         if op+op_increase < 1:
#             op += op_increase
#         crown.append(cylinder(color=color.yellow, opacity=op, radius=base_radius - 3.5*n/m*l_thickness, axis=vector(0, 1, 0), pos=vector(0, base_position + n*l_thickness, 0), length=l_thickness))
#     base_position += 10 * l_thickness
#     base_radius -= 35/m*l_thickness

# Crown = compound(crown)

timing = .04
time_incr = .0004
crown2 = cone(color=color.yellow, opacity=0, radius=3.5, pos=vector(0, 9, 0), axis=vector(0, 1, 0), length=15)
for transp in np.linspace(0, 1, 70):
    crown2.opacity = transp
    time.sleep(timing)
    timing -= time_incr 

while True:
    pass
