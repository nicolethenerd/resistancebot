class Game(object):
	def __init__(self, name):
		self.name = name
		self.players = []
		self.rounds = []
        self.current_round = None
		self.leader_index = None

    @property
    def num_players(self):
        return len(self.players)

    def change_leader(self):
        self.leader_index = (self.leader_index + 1) % self.num_players

    def next_round(self):
        self.current_round = Round()
        self.rounds.append(self.current_round)

    def start_game(self):
        str.format("Welcome to game {game}!", game=self.name)



class Round(object):
    def __init__(self):
        self.votes = []