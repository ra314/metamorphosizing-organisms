from Organism import stage_1_organisms
from Player import Player
from Game import Game
from copy import deepcopy

def enumerate_choices(choices):
	output = "Pick to number to select a choice\n"
	for index, choice in enumerate(choices):
		output += f"[{index}]: {choice}\n"
	return output

def create_player(client):
	client.send("Send name: ".encode())
	name = (client.recv(BUF_SIZE)).decode('utf-8')
	
	organism_choices = [str(organism) + '\n' + str(organism.ability) for organism in stage_1_organisms.values()]
	client.send(f"{enumerate_choices(organism_choices)}\nSelect 2 eg (1 2)\n".encode())
	indexes = (client.recv(BUF_SIZE)).decode('utf-8')
	organisms = [deepcopy(list(stage_1_organisms.values())[int(index)]) for index in indexes.split()]
	return Player(organisms[0], organisms[1], name)
	
def broadcast(client1, client2, message):
	message = message + separator
	client1.send(message.encode())
	client2.send(message.encode())
	
def receive_and_send_client_action(clients, game):
	curr_player, actions_str = game.request_move()
	if not actions_str:
		return 0
	client = clients[str(curr_player)]
	client.send((
		f"{game.draw_buffer.pop(0)} \n\n"
		f"{enumerate_choices(actions_str)}{separator}").encode())
	response = (client.recv(BUF_SIZE)).decode('utf-8')
	response = [int(num) for num in response.split()]
	index = response[0]
	additional_arguments = response[1:]
	game.process_move(index, additional_arguments)
	return 1
	
def end_session(client):
	client.send("Session Over.\n".encode())

from PrepareSocket import *

#Connecting to clients
sock.bind((TCP_IP, T_PORT))
sock.listen()
client1, addr1 = sock.accept()
client2, addr2 = sock.accept()

#Getting player names and organism choices
player1 = create_player(client1)
player2 = create_player(client2)
clients = {str(player1): client1, str(player2): client2}
game = Game(player1, player2)

#Gameplay Loop
while True:
	while game.draw_buffer:
		broadcast(client1, client2, game.draw_buffer.pop(0))
	if receive_and_send_client_action(clients, game) == 0:
		break

#Ending connections with clients
end_session(client1)
end_session(client2)
