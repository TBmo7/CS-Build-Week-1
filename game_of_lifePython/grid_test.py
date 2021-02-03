def gridmaker():
    rows = 15
    cols = 15
    grid = {}
    for x in range(rows):
        for y in range(cols):
            grid[(x,y)] = {'Alive':False, 'Age':0}    
            
    
    #for x in grid:
    #    grid[x] = {'Alive':False, 'Age':0}
    print(grid)
    grid[(0,1)]['Alive'] = True #This is how you update this set
    grid[(0,1)]['Age'] = 24
    print(grid[(0,1)].get('Alive'))
    print(grid[(0,1)].get('Age'))

print(gridmaker())


def alive(dictin,x,y):
    thisisadict = dictin
    thisisadict[(x,y)] = {'Alive':True}
    return thisisadict
def dead(dictin,x,y):
    thisisadict = dictin
    thisisadict.pop((x,y))
    return thisisadict
def donothing(dictin):
    return dictin
def mergedict(alive,dead):
    outdict = {}
    outdict.update(alive)
    outdict.update(dead)
    return outdict

def randomize(grid_in):
    alive_out = {}
    for i in grid_in:
        x,y = i
        choice = random.randint(0,1)
        if choice == 1:
            alive_out[(x,y)] = {'Alive':True}
    return alive_out

def simulate(grid_in,dict_in,value):
    current_grid = grid_in
    current_dict = dict_in 
    i = 0
    while i is not value:
        inner_grid = current_grid
        inner_dict = rules_of_life(inner_grid,current_dict)
        value+=1
        current_dict = inner_dict
    return current_dict

def clear_board(grid_in):
    alive_out = {}
    for i in grid_in:
        x,y = i
        alive_out[(x,y)] = {'Alive':False}
    return alive_out