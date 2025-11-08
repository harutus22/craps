import random

turning_point = 7
loosing_numbers = (2, 3, 12)
goal_number = 0
	
def random_roll_for_pair():
	first_dice = random.randint(1, 6)
	second_dice = random.randint(1, 6)
	return (first_dice, second_dice)
	
def print_roll_result(pair_of_dice):
	print(f"The sum of dice is {pair_of_dice[0]} + {pair_of_dice[1]} = {sum(pair_of_dice)}")
	
def check_for_win(result: int):
	return (goal_number == 0 and (result == turning_point or result == 11)) or (goal_number > 0 and result == goal_number)
		
def check_for_lose(result: int):
	return (goal_number == 0 and result in loosing_numbers) or (goal_number > 0 and result == turning_point)
 
def check_result(result: int):
	if check_for_win(result):
		print("You won") 
		exit()
	elif check_for_lose(result):
		print("You lose")
		exit()
	global goal_number
	if goal_number == 0:
		print("Now your goal number is", result)
		goal_number = result
			
def play_roll_dice():
	dice_roll = random_roll_for_pair()
	print_roll_result(dice_roll)
	result = sum(dice_roll)
	check_result(result)
	
while(True):
	play_roll_dice()
	
