from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
for i in range(20):
    for w in range(60):
        mc.setBlock(x+i+w,y-1,z+i, 1)
        
for i in range(20):
    mc.setBlock(x+i,y-1,z+i, 1)
    mc.setBlock(x+i+1,y-1,z+i, 1)
    mc.setBlock(x+i+2,y-1,z+i, 1)
    
for i in range(20):
    mc.setBlock(x+i,y-1,z+i, 1,x+i+2,y-1,z+i,1)
    
    x,y,z=mc.player.getTilePos()
    mc.setBlocks(x+1,y+6,z+1,x-1,y+4,z-1,79)
    mc.setBlocks(x,y+1,z,x,y+5,z,17)