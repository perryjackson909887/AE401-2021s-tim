from mcpi.minecraft import Minecraft
mc=Minecraft.create()
def planttree(x,y,z):
   
    mc.setBlocks(x+1,y+6,z+1,x-1,y+4,z-1,79)
    mc.setBlocks(x,y+1,z,x,y+5,z,17)
x,y,z=mc.player.getTilePos()
planttree(x,y,z)

x,y,z=mc.player.getTilePos()
for i in range (20):
    planttree(x+i*5,y,z)
x,y,z=mc.player.getTilePos()
for i in range (20):
   for f in range (20):
    planttree(x+i*5,y,z+f*5)
    
    
x,y,z=mc.player.getTilePos()
for i in range (20):
    for j in range (5):
        planttree(x+i*5,y+i*j,z)
        
        
        
        
        
x,y,z=mc.player.getTilePos()
for i in range (20):
    for j in range (5):
        for l in range (10):
            planttree(x+i*5,y+j*4,z+i*l)