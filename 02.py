# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
print(mc.player.getTilePos())
x=55
y=76.0
z=255.678
x,y,z=mc.player.getTilePos()
mc.player.setTilePos(x,y+100,z)


while True:
        x,y,z,=mc.player.getTile()
        mc.postToChat("You are located at" + str(x)"," + str(y) + "," + str(z))
        time.sleep(0.5)