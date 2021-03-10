# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# declaring a variable for each player that scored

playerOne = 'Ruud Gullit' 
playerTwo = 'Marco van Basten'

# declaring a variable for each minute of the match that a goal was scored in

goal_0 = 32
goal_1 = 54

scorers = playerOne + ' ' + str(goal_0) +', ' + playerTwo + ' ' + str(goal_1)

report = f'{playerOne} scored in the {goal_0}nd minute\n{playerTwo} scored in the {goal_1}th minute'

player = 'Igor Belanov'

first_name = player[:player.find(' ')]

first_name_len = len(player[:player.find(' ')])

last_name_len = len(player[player.find(' ') + 1:])

name_short = str(player[0] + '. ' + player[player.find(' ') + 1:])

chant = ((first_name + '! ') * 3) + (first_name + '!')

good_chant = chant[-1] != ' '