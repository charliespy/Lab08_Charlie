#Charlie Sun
#5 May 2020
#Lab08.py

def ask_for_input_A(p, l):
    answer = input(str(l[0]))
    if answer == 'A':
        print(l[1])
        p+=1
    elif answer == 'B':
        print(l[2])
    else:
        print('Invalid input, try again!')
        ask_for_input_A(p, l)
    return p

def ask_for_input_B(p, l):
    answer = input(str(0))
    if answer == 'A':
        print(l[1])
    elif answer == 'B':
        print(l[2])
        p+=1
    else:
        print('Invalid input, try again!')
        ask_for_input_B(p, l)
    return p

def ask_for_input(l):
    answer = input(str(l[0]))
    if answer == 'A':
        print(l[1])
    elif answer == 'B':
        print(l[2])
    else:
        print('Invalid input, try again!')
        ask_for_input(l)

def go_to_Webb(p):
    print("You couldn't do anything else but to go with parents to California the following day.")
    print('However, the moment you guys drove in from the front gate of Webb, you felt something strange.')
    print('You could not figure out what is it that is making you so uncomfortable, so you decided to:  ')
    l = [
        'type "A" to tell your dad about your feelings OR type "B" to keep it in your mind: '
        , '\nObviously, your dad was triggered, not only by you, but also the traffic. He yelled: "Can you stop f**king around please! Now shut up because we are about to meet the assistant head of schools Dr.Thmish." THIS WAS NOT HOW YOUR DAD NORMALLY TALKS. You were scared.'
        , '\nYou held your discomfort and did not say anything. The car entered Webb in silence. Everybody was nervous to see the place where you guys are gonna live for the next god knows how many years.'
    ]
    this_point = ask_for_input_A(p, l)
    return this_point

if __name__ == '__main__':
    point = 0
    name = input('Please enter your name: ')
    print("\nYou are a 5-year old kid who lives in Boston. Both your parents are professors in Harvard. However, one day, you mom tells you that your family is moving to California because they decided to work in a new school named The Webb Schools.")
    print("You are very surprised. Obviously, you don't want to leave all your friends in Boston. So you...")

    my_list = [
        'type "A" to cry OR type "B" to request a new iPhone from your mom: '
        , '\nMom: OH MY GOD Stop it! '+name+'! You are the most disobedient kid I have ever seen!'
        , '\nMom: OH MY GOD Stop it! '+name+'! You are the most disobedient kid I have ever seen!'
    ]
    ask_for_input(my_list)

    point = go_to_Webb(point)
    print(point)