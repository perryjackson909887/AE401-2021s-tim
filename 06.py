from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,0,"1","2","3","4")
"""
while True:
    hits=mc.event.pollBlockHits()
    if (len(hits) > 0):
        hit = hits[0]
        x,y,z,=hit.pos.x, hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
       print("55555"+str(block)

while True:
    hits=mc.event.pollBlockHits() 
    if (len(hits) > 0):
        hit = hits[0]
        x,y,z,=hit.pos.x, hit.pos.y,hit.pos.z
        mc.setBlocks(x,y,z,57)
    """
    pos=mc.player.getPos()
    
    while True:   
        x=pos.x+uniform(20,-20)
        z=pos.z+uniform(20,-20)
        y=pos.y+50
        mc.spawnEntity(x,y,z,50)
        time.sleep(0.1)