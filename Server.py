from Organism import Organism, stage_1_organisms
from Player import Player

def create_player(client):
	client.send("Send name: ".encode())
	name = (client.recv(BUF_SIZE)).decode('utf-8')
	organism_choices = '\n\n'.join([f"{index} {str(organism)} \n{str(organism.getAbility())}" 
		for index, organism in enumerate(stage_1_organisms.values())])
	client.send(f"Pick 2 organisms. eg 'Bonzumi Sepahnix'.\n{organism_choices}\n\n".encode())
	selection = (client.recv(BUF_SIZE)).decode('utf-8')
	organisms = [stage_1_organisms[name] for name in selection.split()]
	return Player(organisms[0], organisms[1], 80, name)

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


