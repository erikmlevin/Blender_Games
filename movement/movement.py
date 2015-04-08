import bge
import Rasterize

class MouseLook(object):
	"""docstring for MouseLook"""
	def __init__(self):
		self.SENSITIVITY = .005 # mouse sensitivity
		self.walkSpeed = 5 # walk speed, will defined by prop of Player
		self.sprint = 2.25 # 

		self.scene = bge.logic.getCurrentScene()
		self.player = self.scene.objects['Player']
	
	def look(self):
		



