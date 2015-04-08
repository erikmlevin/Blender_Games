import bge
import Rasterizer as R
import math
import mathutils as mathu

class MouseLook(object):
	"""docstring for MouseLook"""
	def __init__(self):
		self.SENSITIVITY = .005 # mouse sensitivity
		self.walkSpeed = 5 # walk speed, will defined by prop of Player
		self.sprint = 2.25 # 

		self.scene = bge.logic.getCurrentScene()
		self.playerCamera = self.scene.objects['playerCamera']
		self.playerBody = self.scene.objects['playerBody']
	
	def look(self):
		cont = bge.logic.getCurrentController()
		mouse = cont.sensors['playerMouse']

		if 'x' not in self.playerCamera:
			self.playerCamera['x'] = math.pi / 2
			self.playerCamera['y'] = math.pi / 6
			x = R.getWindowWidth() // 2
			y = R.getWindowHeight() // 2
			self.playerCamera['size'] = (x,y)

		xpos = self.playerCamera['size'][0]
		ypos = self.playerCamera['size'][1]
		x = (xpos - mouse.position[0])*self.SENSITIVITY
		y = (ypos - mouse.position[1])*self.SENSITIVITY

		R.setMousePosition(xpos,ypos)

		self.playerCamera['x'] += x
		self.playerCamera['y'] += y

		#corelation of x(z) angle
		if self.playerCamera['x'] > 2 * math.pi:
			self.playerCamera['x'] -= 2*math.pi
		if self.playerCamera['x'] < 0:
			self.playerCamera['x'] += 2*math.pi
		#corelation of y(x) angle
		if self.playerCamera['y'] > math.pi / 2:
			self.playerCamera['y'] = math.pi / 2
		if self.playerCamera['y'] < -math.pi / 2:
			self.playerCamera['y'] = -math.pi / 2

		x = -self.playerCamera['y'] + math.pi / 2
		y = self.playerCamera['x'] + math.pi / 2

		v = mathu.Vector((-x,0,-y))
		w = mathu.Vector((0,0,y-math.pi))

		self.playerCamera.localOrientation = v
		self.playerBody.localOrientation = w



	def move(self):
		pass


#method for import module
def mouseLook():
	mLook = MouseLook()
	mLook.look()
