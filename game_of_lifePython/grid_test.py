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
