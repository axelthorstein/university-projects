class Player(object):

	def getMove(self):
		return "whatever"

class TicTacToePlayer(Player):

	def __init__(self, game):
		self.game = game

	def getMove(self):
		if self.game.grid:
			#do something with grid
			pass

class ComputerTicTacToePlayer(Player):
	
	def __init__(self, game):
		self.game = game

	def getMove(self):
		if self.game.grid:
			#do something with grid
			pass

class Game(object):

	def __init__(self):
		self.done = False
		self.players = self.generatePlayers()

	def generatePlayers(self):
		computer = Player()
		human = Player()
		return [human, computer]

	def completed(self):
		#some condition
		return False

	def getPlayers(self):
		return self.players

	def update(self):
		if self.completed():
			self.done = True

		else:
			for player in self.players:
				player.getMove()

class TicTacToe(Game):
	def __init__(self):
		Game.__init__(self)
		self.grid =[[".",".","."],[".",".","."],[".",".","."]]

	def generatePlayers(self):
		computer = ComputerTicTacToePlayer(self)
		human = TicTacToePlayer(self)
		return [human, computer]

	def completed(self):
		#some different condition
		pass

game = TicTacToe()

while not game.done:
	game.update()