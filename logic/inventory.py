import bge
import GameLogic

class inventory(object):
	"""docstring for inventory
	...
	"""
	def __init__(self):
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()

	def import_into_inventory(self):
		pass
	
