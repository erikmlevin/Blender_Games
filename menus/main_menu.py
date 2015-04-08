import bge
import GameLogic 
class MainMenu():
	"""docstring for MainMenu"""
	def __init__(self):
		bge.logic.mouse.visible = True

		self.scene = bge.logic.getCurrentScene()
		self.cont = bge.logic.getCurrentController()

		self.newGameButton = self.scene.objects['newGameButton']
		self.continueButton = self.scene.objects['continueButton']
		self.loadButton = self.scene.objects['loadButton']
		self.settingsButton = self.scene.objects['settingsButton']
		self.quitButton = self.scene.objects['quitButton']

		

	def newGame(self):
		pass
	def continueGame(self):
		pass
	def load(self):
		pass
	def settings(self):
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			self.settingsButton.color = [0.6,0.6,1,True]
			if mouseClick.positive:
				self.scene.addObject("settings","center",0)
				self.scene.addObject("killButton","center",0)
				GameLogic.globalDict['killstack'] = []
				GameLogic.globalDict['killstack'].append(self.scene.objects["settings"])#hhave to made it global prop
				GameLogic.globalDict['killstack'].append(self.scene.objects["killButton"])
		else:
			self.settingsButton.color = [0.1,.6,1,True]
		
	def quit(self):
		pass
	def killWindow(self):
		killButton = self.scene.objects['killButton']
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			killButton.color = [0,1,.5,True]
			if mouseClick.positive:
				self.scene.objects['settings'].endObject()
				self.scene.objects['killButton'].endObject()
		else:
			killButton.color = [0,1,.8,True]



def settings():
	sett = MainMenu()
	sett.settings()

def killWindow():
	kill = MainMenu()
	kill.killWindow()
