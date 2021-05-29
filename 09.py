from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
""""
def buildPyramid(x,y,z,base):
        height=base//2+1
    for i in range(height):
        x1=x+i
        y1=y+i
        z1=z+i
        x2=x+base-i
        z2=x+base-i
        mc.setblock(x1,y1,z1,x2,y1,z1,103)


x,y,z=mc.player.getTilePos
buildPyramid(x,y,z)

list1=[]
list2=[]
list3=[]
for i in range(1,10):
    list1.append(1*i)
    
for i in range(1,10):
    list2.append(2*i)
    
for i in range(1,10):
    list3.append(3*i)






print(list1)
print(list2)
print(list3)

"""


number=1
x,y,z,=mc.player.getTilePos()
for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
        
    number=number*2
    mc.postToChat(str(number))

    
    


                   
  

