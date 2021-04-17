from Organism import Organism, stage_1_organisms
from Player import Player
from Game import Game
from copy import deepcopy

def create_player(client):
	client.send("Send name: ".encode())
	name = (client.recv(BUF_SIZE)).decode('utf-8')
	organism_choices = '\n\n'.join([f"{index} {str(organism)} \n{str(organism.ability)}" 
		for index, organism in enumerate(stage_1_organisms.values())])
	client.send(f"Pick 2 organisms. eg 'Bonzumi Sepahnix'.\n{organism_choices}\n\n".encode())
	selection = (client.recv(BUF_SIZE)).decode('utf-8')
	organisms = [deepcopy(stage_1_organisms[name]) for name in selection.split()]
	return Player(organisms[0], organisms[1], name)
	
def end_session(client):
	client.send("Session over.\n".encode())

from PrepareSocket import *

#Connecting to clients
sock.bind((TCP_IP, T_PORT))
sock.listen()
client1, addr1 = sock.accept()
client2, addr2 = sock.accept()

#Getting player names and organism choices
player1 = create_player(client1)
player2 = create_player(client2)

print(player1)
print(player2)

game = Game(player1, player2)
game.randomise_arena()

end_session(client1)
end_session(client2)
