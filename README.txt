Move responsibilty of abilitiy activation and ability implementation from Game to the Organism class.
Maybe even get rid of the Ability class.
Have an abstract organim class that all of the organisms inherit from.
Print the mana cost next to the abilities when the players are selecting organisms
Create an abstract class drawable with the abstract method draw.
Make game, player and organism children of this class.
Fix infinite while loop when trying to force a grid match
Fix grid match bug in feeding in the arguments
Add validation for how far you're allowed to mvoe tiles. 
i.e don't allow arbitary swapping of tiles
Fix the bug that occured with boosting magnooki. It was at 6 mana, it needed 10 for activation and you boosted with 4 berries, but it didn't go through.

EVERYTHING ABOVE HAS BEEN DONE
https://old.reddit.com/r/learnprogramming/comments/2khyfd/javaoop_question_im_working_a_pokemon_project/cllsv59/

TO FIX
When it's not your turn as a player if you provide input that is not white space (space or newline), then this input counts when you start your next turn and if the input is malformed, then the server crashes. Make sure that this kind of input is ignored.

Add color to the pinrint of the grid for each type of mana.

NB
Make sure to use the public IP when binding when playing over hamachi.
