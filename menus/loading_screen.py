import bge
from Random import choice
class LoadingScreen(object):
	"""docstring for LoadingScreen
		loading screen function + progress bar
	"""
	def __init__(self, arg):
		self.cont = bge.logic.getCurrentController()
		self.scene = bge.logic.getCurrentScene()
		self.loadingBar = self.scene.objects['loadingBar']
		self.tipsField = self.scene.objects['tipsField']
	def loadBar(self):
		#conting for progress of loading bar
		pass
	def tips(self):
		#text of tips for game -> radnom changing 
		#reprasentated by List of strings
		#from some external file
		self.tipsField.text = choice([])
		pass

