from Organism import Organism
from Ability import Ability
from Player import Player

def initialize_organisms():
	Flare_plus = Ability('Flare+: Attacks for 25 HP and matches 2 random columns.', 
		(0,5), ((1,-1),(1,-1)), 0, False, None, None, 8)
	Flare = Ability('Flare: Attacks for 20 HP and matches a random column.', 
		(0,20), ((1,-1)), 0, False, None, None, 8)
	Bonzire = Organism('Bonzumi', Flare_plus, 'fire', None)
	Bonzumi = Organism('Bonzumi', Flare, 'fire', Bonzire)

	Hydro_Rush_plus = Ability('Hydro Rush+: Attacks for 20 HP and converts 23random tiles to Water.', 
		(0,20), None, 3, False, None, None, 6)
	Hydro_Rush = Ability('Hydro Rush: Attacks for 10 HP and converts 2 random tiles to Water.', 
		(0,10), None, 2, False, None, None, 6)
	Sephanix = Organism('Sephanix', Hydro_Rush_plus, 'water', None)
	Pelijet = Organism('Pelijet', Hydro_Rush, 'water', Sephanix)

	Heal_Leaf_plus = Ability('Heal Leaf+: Attacks for 15HP and heals you for 15HP.', 
		(10,10), None, 0, False, None, None, 6)
	Heal_Leaf = Ability('Heal Leaf: Attacks for 10HP and heals you for 10HP.', 
		(10,10), None, 0, False, None, None, 6)
	Karaggon = Organism('Karaggon', Heal_Leaf_plus, 'grass', None)
	Turtleisk = Organism('Turtleisk', Heal_Leaf, 'grass', Karaggon)
	
	return (Bonzumi, Pelijet, Turtleisk)
	
mana_types = ('fire', 'electric', 'water', 'grass')
stage_1_organisms = initialize_organisms()
organism_choices = '\n\n'.join([f"{index} {str(organism)} \n{str(organism.getAbility())}" 
	for index, organism in enumerate(stage_1_organisms)])
		
def create_player(client):
	client.send("Send name: ".encode())
	name = (client.recv(BUF_SIZE)).decode('utf-8')
	client.send(f"Pick 2 organisms. eg '1 3'.\n{organism_choices}\n\n".encode())
	selection = (client.recv(BUF_SIZE)).decode('utf-8')
	organisms = [stage_1_organisms[int(index)] for index in selection.split()]
	return Player(organisms[0], organisms[1], 80, name)

from prepare_socket import *

#Connecting to clients
sock.bind((TCP_IP, T_PORT))
sock.listen()
client1, addr1 = sock.accept()
client2, addr2 = sock.accept()

player1 = create_player(client1)
player2 = create_player(client2)

print(player1)
print(player2)
