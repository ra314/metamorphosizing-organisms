from Organism import Organism, stage_1_organisms
from Player import Player
from Game import Game
from copy import deepcopy
from time import sleep

def enumerate_choices(choices):
	output = ""
	for choice, index in enumerate(choices):
		output += f"[{index}]: {choice}\n"
	return output

def create_player(client):
	client.send("Send name: ".encode())
	name = (client.recv(BUF_SIZE)).decode('utf-8')
	
	organism_choices = enumerate_choices(list(stage_1_organisms.values()))
	client.send(f"{organism_choices}\n".encode())
	indexes = (client.recv(BUF_SIZE)).decode('utf-8')
	organisms = [deepcopy(list(stage_1_organisms.values())[int(index])) for index in indexes.split()]
	return Player(organisms[0], organisms[1], name)
	
def broadcast(client1, client2, message, sleep_time):
	client1.send(message.encode())
	client2.send(message.encode())
	sleep(sleep_time)
	
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

#Creating a game, randomising the arena and broadcasting it
game = Game(player1, player2)
display = game.randomise_arena()
broadcast(client1, client2, message, 3)

#Selecting and broadcasting the first player
display = game.select_first_player()
broadcast(client1, client2, message, 2)

#Gameplay loop
game.initialize_grid()

#TODO
Game object has a state
The state can either be displaying or requesting input from a specific player.
If the state is display, then display and get the next state
If the state is to get input, then ask the client for input.
Make it so that clients know when they need to respond and when they don't need to, so they're not stuck.



#Ending connections with clients
end_session(client1)
end_session(client2)
