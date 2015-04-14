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
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			self.newGameButton.color = [0.6,0.6,1,True]
			if mouseClick.positive:
				#dodelat vyskakujici okno pro potvrzeni
				self.scene.replace('game')
		else:
			self.newGameButton.color = [0.1,.6,1,True]

	def continueGame(self):
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			self.continueButton.color = [0.6,0.6,1,True]
			if mouseClick.positive:
				#dodelat vyskakujici okno pro potvrzeni
				bge.logic.endGame()
		else:
			self.continueButton.color = [0.1,.6,1,True]

	def loadGame(self):
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			self.loadButton.color = [0.6,0.6,1,True]
			if mouseClick.positive:
				#dodelat vyskakujici okno pro potvrzeni
				bge.logic.endGame()
		else:
			self.loadButton.color = [0.1,.6,1,True]

	def settings(self):
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			self.settingsButton.color = [0.6,0.6,1,True]
			if mouseClick.positive:
				self.scene.addObject("settings","center",0)
				self.scene.addObject("killButton","center",0)
		else:
			self.settingsButton.color = [0.1,.6,1,True]
		
	def quit(self):
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			self.quitButton.color = [0.6,0.6,1,True]
			if mouseClick.positive:
				#dodelat vyskakujici okno pro potvrzeni
				bge.logic.endGame()
		else:
			self.quitButton.color = [0.1,.6,1,True]

	def killWindow(self):
		#have to made it trought the for cycle scene,object and check if parent is killButton 
		killButton = self.scene.objects['killButton']
		mouseOver = self.cont.sensors['mouseOver']
		mouseClick = self.cont.sensors['mouseClick']
		if mouseOver.positive:
			killButton.color = [0,1,.5,True]
			if mouseClick.positive:
				self.scene.objects['settings'].endObject()
				self.scene.objects['killButton'].endObject()
		else:
			killButton.color = [1,1,0,True]



def settings():
	sett = MainMenu()
	sett.settings()

def killWindow():
	kill = MainMenu()
	kill.killWindow()

def newGame():
	new = MainMenu()
	new.newGame()

def continueGame():
	cont = MainMenu()
	cont.continueGame()

def quit():
	end = MainMenu()
	end.quit()

def loadGame():
	load = MainMenu()
	load.loadGame()

