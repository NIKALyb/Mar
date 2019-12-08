#connect library
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import mcpi.block as block
import random 
import time
#tp
mc.player.setTilePos(50,132,50)
#set
#mc.setBlocks(-4,125,-4,54,135,54)
#mc.setBlocks(-1,131,-1,51,132,51,22)
#mc.setBlocks(0,132,0,50,132,50,0)
#variable
def CGB():
	x = random.randint(0,50)
	z = random.randint(0,50)
	mc.setBlock(x,y,z,41)
a = 0
y = 135
#loop
CGB
while a<20:
	pos = mc.player.getTilePos()
	if round(pos.x) == x and round(pos.z) == z:
		mc.setBlock(x,y,z,0)
		mc.postToChat("You found gold")
		a += 1
