#Charlie Sun
#30 Apr 2020
#Lab08.py

def go_to_Webb(p):
    print("You couldn't do anything else but to go to parents to California the following day.")
    print('However, the moment you guys drove in from the front gate of Webb, you felt something strange.')
    print('You could not figure out what is it that is making you so uncomfortable, so you decided to:  ')
    answer = input('type "A" to tell your dad about your feelings OR type "B" to keep it in your mind: ')
    if (answer == 'A'):
        print('Obviously, your dad was triggered, not only by you, but also the traffic. He yelled:')
        print('"Can you stop f**king around please! Now shut up because we are gonna meet our new friends."')
        print('THIS was NOT HOW YOUR DAD NORMALLY TALKS. You were scared.')
        p+=1
    if (answer == 'B'):
        print('You held your discomfort and did not say anything. The car entered Webb in silence. Everybody was nervous to see the place where you guys are gonna live for the next god knows how many years.')

if __name__ == '__main__':
    point = 0
    name = input('Please enter your name:   ')
    print("You are a 5-year old kid who lives in Boston. Both your parents are professors in Harvard. However, one day, you mom tells you that your family is moving to California because they decided to work in a new school named The Webb School")
    print("You are very surprised. Obviously, you don't want to leave all your friends in Boston. So you...")
    answer1 = input('type "A" to cry OR type "B" to request a new iPhone from your mom: ')
    if (answer1 == 'A'):
        print('Mom: OH MY GOD Stop it! '+name+' You are the most disobedient kid I have ever seen!')
        
    elif (answer1 == 'B'):
        print('Mom: OH MY GOD Stop it! '+name+' You are the most disobedient kid I have ever seen!')

    go_to_Webb(point)
    