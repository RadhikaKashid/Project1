import random



def swg(computer,mine):
    if (computer == mine):
        return None
    
    if(computer =='s' and mine =='g'):
        return True
    elif (computer=='w' and mine=='s'):
        return True
    elif (computer =='g' and mine =='w'):
        return True
    else:
        return False
    


choice =('s','w','g')
computer= random.randint(0,2)
computer = choice[computer]
# print(computer)
mine = input('choice ether s,w or g: \n')

win = swg(computer,mine)
print(f"you chose {mine} and the computer chose {computer}")
if win is  None:
    print("Match Drawn")
if win:    
    print("you won!!")
else:
    print("Computer Won!!!")