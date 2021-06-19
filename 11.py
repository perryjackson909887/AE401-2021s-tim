from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange
for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    for _ in range(10):
        r=randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)
l=randrange(1,16)
while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
if data == r:
    mc.postToChat("恭喜你找到我>//<")
    mc.setBlock(hit.pos,57)
    break
elif data<r:
    mc.postToChat("找錯了" )
elif data>r:
    mc.postToChat("找錯了" )
def LinnearSearch():
    for i in range(10000001):
        if i==r:
            return i
def BinarySearch():
    low = 0
    high = 10000000
    while low>=high:
        mid=(low+high)//2
        if mid > r:
            high=mid-1
        elif mid <r:
            low = mid+1
        else:
            return mid
