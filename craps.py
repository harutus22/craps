import random

turning_point = 7
game_start_winner = 11
loosing_numbers = (2, 3, 12)
goal_number = 0

def dice_sum(dice_pair):
	return dice_pair[0] + dice_pair[1]
	
def random_roll_for_pair():
	first_dice = random.randint(1, 6)
	second_dice = random.randint(1, 6)
	return (first_dice, second_dice)
	
def print_roll_result(pair_of_dice):
	first_dice = pair_of_dice[0]
	second_dice = pair_of_dice[1]
	print(f"The sum of dice is {first_dice} + {second_dice} = {dice_sum(pair_of_dice)}")
	
def check_for_win(result: int):
	if goal_number == 0 and (result == turning_point or result == game_start_winner):
		return True
	elif goal_number > 0 and result == goal_number:
		return True
	else:
		return False
		
def check_for_lose(result: int):
	if goal_number == 0 and result in loosing_numbers:
		return True 
	elif goal_number > 0 and result == turning_point:
		return True
	else:
		return False
 
def check_result(result: int):
	if check_for_win(result):
		print("You won") 
		exit()
	elif check_for_lose(result):
		print("You lose")
		exit()
	else: 
		global goal_number
		if goal_number == 0:
			print("Now your goal number is", result)
			goal_number = result
	
first_roll = random_roll_for_pair()
print_roll_result(first_roll)
result = dice_sum(first_roll)
check_result(result)

while(True):
	random_roll = random_roll_for_pair()
	result = dice_sum(random_roll)
	print_roll_result(random_roll)
	check_result(result)
	
