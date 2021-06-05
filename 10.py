from mcpi.minecraft import Minecraft
import time
import random
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

for i in range(20):
    f=random.randrange(1,5)
    
    if f==1:
        mc.setBlocks(x,y,z,x+4,y,z,57)
        x += 4
    elif f==2:
        mc.setBlocks(x,y,z,x-4,y,z,57)
        x -= 4
    elif f==3:
        mc.setBlocks(x,y,z,x,y,z+4,57)
        z += 4
    elif f==4:
        mc.setBlocks(x,y,z,x,y,z-4,57)
        z-=4
        
while True:
    mc.executeCommand("time add 50" )
    time.sleep(0.1)        