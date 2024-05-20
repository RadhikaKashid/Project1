import random
l={1:'Rock',
   2:'Paper',
   3:'Sesor'}
print(l)
ch=['1','2','3']
print(ch)
i=1
c=0
while(i==1):
    c=c+1
    
    print("Iteration no:", c)
    
    p1=int(input('make a choise from the above list: '))
    p2=int(random.choice(ch))
    print('random computer choice: ', p2)

    if p1==1 and p2 ==2:
        print('conratulation player2!!!!')
    elif p1==1 and p2==3:
        print('congratulation player1 !!!')
    elif p1==2 and p2==1:
        print('congratulation player1 !!!')
    elif p1==2 and p2==3:
        print('congratulation player2 !!!')
    elif p1==3 and p2==1:
        print('congratulation player2 !!!')
    elif p1==3 and p2==2:
        print('congratulation player1 !!!')
    elif p1==p2:
        print('==Tie==')
    else:
        print('invalid choice')
    i=int(input('print 1 if you want to continue or 0 for exit'))
    

