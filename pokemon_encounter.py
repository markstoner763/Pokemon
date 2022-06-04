class Pokemon:
	def __init__(self, name, element, hp, mp):
		self.name = name
		self.element = element
		self.hp = hp
		self.mp = mp


#	def printName(self):
#		print(self.name)


class Player:
	def __init__ (self, name, hometown):
		self.name = name
		self.hometown = hometown


	def display_player_name(self):
		print(Player.name)


	def display_player_hometown():
		print(Player.hometown)

class Move:
	def __init__ (self, name, element, opponent_hp_effect, player_creature_mp_effect):
		self.name = name
		self.element = element
		self.opponent_hp_effect = opponent_hp_effect
		self.player_creature_mp_effect = player_creature_mp_effect


ember = Move("Ember", "Fire", 5, 2)	

def ember_attack(self):
	opponentCreature.hp = opponentCreature.hp - 5
	return int(opponentCreature.hp)

class BattleRecord:
	def __init__ (self, victory_count, loss_count):
		self.victory_count = victories
		self.loss_count = losses
	#Where does the actual count begin? Where is it stored exactly?	When is it affected?
	#BattleRecord class will track number of wins and print it to the user after a fight

	Victory: When opponentCreature HP <= 0

	def increase_win_count():

	def increase_loss_count():

	def display_record():


class Battlefield:
	def __init__ (self, landscape, weather):
		self.landscape = landscape
		self.weather = weather

	#def affect_move_strength
	#	if move.type == "Water" and landscape == "ocean"
			# WaterMoves increase strength by 1.5x

playerCreature = Pokemon("Olive", "Fire", 20, 10)

opponentCreature = Pokemon("Atlas", "Grass", 20, 10)

print("\nA wild " + opponentCreature.name + " appeared!")
print(opponentCreature.name + " has " + str(opponentCreature.hp) + " HP.")


#while opponentPokemon.hp > 0 and playerPokemon.hp > 0: STRETCH GOAL


class Battle:
	def __init__(self, BattleRecord, Battlefield):

	def run_encounter (
		while playerCreature.hp > 0:
			print(opponentCreature.name + " took 5 damage!")
			print(opponentCreature.name + " has " + str(opponentCreature.hp) + " HP remaining!")
		)

encounter = Battle()


userInput = input("\nDo you want " + playerCreature.name + " to use Ember? \n\nEnter 'Yes' or 'No' \n")
#At end of combat, ask if player wants to go again, and then successively track/count wins in subsequent battles

if userInput == "yes" or userInput == "Yes" or userInput == "y" or userInput == "Y":
	playerCreature.ember_attack()
else:
	print(opponentCreature.name + " tackled you!!")

#ember_attack = playerCreature.ember  Stretch goals!
#ember_attack()

# Do not use if/else statements to "block" off certain moves
# Convert to snake_case
# I want to see my victory points (Wins) e.g. win_tracker+=1 at the end of a fight
# I want to see my HP and my opponent's HP
# I want to decide what my player's name is
# I want to decide where my player's home town is
# I want to decide on the battle field's element 
# Find a better place for the Ember function / rename the function to a verb
# Give opponent creature a move that does less damage




