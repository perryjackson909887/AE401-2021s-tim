from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True:
   x,y,z=mc.player.getTilePos()
    
   a=mc.getBlock(x,y-1,z)
   b=mc.getBlock(x+1,y-1,z)
   c=mc.getBlock(x,y-1,z+1)
   d=mc.getBlock(x-1,y-1,z)
   e=mc.getBlock(x,y-1,z-1)
   if a==2 or b==2 or c==2 or d==2 or  e==2:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,46)
        
        a=0
while a<20:
            mc.setBlocks(x+30,y-1,z,x-30,y-10,z,46)
            z=z-5
            a=a+1
while True:
    x,y,z=mc.player.getTilePos()
    setBlock(x,y,z,8)
    setBlock(x,y,z,19)
    time.sleep(5)        