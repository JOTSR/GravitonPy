from time import sleep
from definition import Acceleration, Length, Mass
from model.position import update_position
from ui.display import Display
from cluster import Cluster

cluster = Cluster([800, 800], 1e3) #2d Cluster of 800x800 with 1000 bodies
display = Display(cluster)

display.start()

"""Update bodies position at the given interval in ms"""
#TODO change loop t async callback to avoid thread blocking
while True:
	bodies, field, τ = cluster.unpack()
	display.update(cluster.bodies)

	updatedBodies = update_position(bodies, field, τ)
	cluster.bodies = updatedBodies

	sleep(16 / 1000)
	#60 fps max