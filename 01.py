# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
print(mc.player.getTilePos())
x=116
y=180
z=82
mc.player.setTilePos(x,y,z)