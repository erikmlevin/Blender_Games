import bge
class Settings():
	"""docstring for Settings"""
	def __init__(self):
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		self.window = self.scene.objects['settings']
	def save(self):
		#this mathod should save settings for game(with next start-up should be used like default settngs) 
		pass
	def default(self):
		#method for reset settins to default(pre-defined sate)
		pass
	def resolution(self):
		# method for changing resolution in game(by list box)
		pass
	def sound(self):
		#method for changing volume in game probably gonna need new class for that (3 types of sounds in game - enviroments, music, voice)
		pass
	