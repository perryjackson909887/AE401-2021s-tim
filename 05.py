from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
try:
    x,y,z=mc.player.getTilePos()
    ID=int(input("ID"))
    mc.setBlock(x,y,z,ID)
except:
    print:("bibibi")
    us=input("name")
    message=input("發言")
    mc.postToChat(" ["+us+"] " +message)
    
    x,y,z=mc.player.getTilePos()
    
    mc.setBlocks(x+3,y,z+13,y+10,z+9,1)
    mc.setBlocks(x+4,y+1,z+1,z+12,y+9,z+9,0)
    
x,y,z=mc.player.getTilePos()
    
hight=int(input("high"))
length=int(input("long"))
width=int(input("wid"))
BlockID=int(input("ID"))
    
mc.setBlocks(x,y+1,z,x+length-1,y+hight,z+width-1,BlockID)
mc.setBlocks(x+1,y+2,x+length-2,y+hight-1,z+width-2,0)
mc.setBlocks(x+2,y+2,z,y+3,z,0)