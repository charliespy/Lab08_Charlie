#Charlie Sun
#13 May 2020
#Lab08.py

fame = 10
relationship = 10
fitness = 10
love = False

def ask_for_input_any(variable, value, l, correct):
    answer = input(str(l[0]))
    if correct == 'A':
        wrong = 'B'
    elif correct == 'B':
        wrong = 'A'
    elif correct == 'all':
        correct = 'A' or 'B'

    if answer == correct:
        print(l[1])
        variable += value
    elif answer == wrong:
        print(l[2])
    else:
        print('Invalid input, try again!')
        ask_for_input_any(p, l)
    return variable

def go_to_Webb(v):
    print("You couldn't do anything else but to go with parents to California the following day.")
    print('However, the moment you guys drove in from the front gate of Webb, you felt something strange.')
    print('You could not figure out what is it that is making you so uncomfortable, so you decided to:  ')
    l = [
        'type "A" to tell your dad about your feelings OR type "B" to keep it in your mind: '
        , '\nObviously, your dad was triggered, not only by you, but also the traffic. He yelled: "Can you stop f**king around please! Now shut up because we are about to meet the assistant head of schools Dr.Thmish." THIS WAS NOT HOW YOUR DAD NORMALLY TALKS. You were scared.'
        , '\nYou held your discomfort and did not say anything. The car entered Webb in silence. Everybody was nervous to see the place where you guys are gonna live for the next god knows how many years.'
    ]
    this_point = ask_for_input_any(v, -5, l, "A")
    return this_point

def settle_down(v):
    print('It \'s late July. You will become a freshman once the year starts. The school gave you guys some time to settle down before the year is kicked off.')
    print('One day when you\'re roaming around the campus, you see a huge bear standing beside the trash.')
    print('You are obviously very scared. What should you do?')
    l = [
        'Type "A" to run away or type "B" to take pictures: '
        , '\nIn fact, the bear didn\'t spot you until you were running. It sprinted toward you and tried to kill you.'
        , '\nYou took many awesome pictures of the bear, but just when you were about to sneak away, the bear spotted you. It sprinted toward you and tried to kill you.'
    ]
    ask_for_input_any(v, 3, l, 'B')

def run_away(v):
    print('At this moment, you recalled a Youtube video you saw the other day about making bears\' voices. You decided to give it a try')
    l = [
        'type "A" or "B" to mimic bears\'s voice ---> A = "AHHHHHHHH", B = "RAWWWWWWW": '
        , '\nObviously, this is not how bears talk, but you somehow shocked the bear. It stood there in amazement while you ran away as quick as you could.'
        , '\nWell, that was not the voice of bears, but rather tigers. Bears are afriad of tigers, so is this one. You watched the bear ran away from you in amazement.'
    ]
    point = ask_for_input_any(v, 10, l, 'B')
    return point

def semester_starts(v):
    print('It has been almost a month since the bear incident happened. You guys are on your freshman retreat.')
    print('However, just when you were going on the bus, a huge bear popped out and was walking toward the bus.')
    print('Your advisor, Ms. Kenared, tried to calm people down but in vain. The crowd bursted into a panic.')
    print('For some reason, someone pushed you. You fell hard on the ground, 5 feet away from the bear. What should you do now?')
    l = [
        'type "A" to run back to the bus or type "B" to pretend you\'re dead: '
        , 'You ran away, but so did the crowd. Everybody thought you were gonna attract the bear toward them. Only your advisor Ms. Kenared left there with you.'
        , 'You lied there, silently. The bear saw you as a plancon seat or something, and tried to sit on you. Luckily, Ms. Kenared sprinted toward you and saved you from the bears\' ass.'
    ]
    this_point = ask_for_input_any(v, -5, l, 'A')
    return this_point

def become_famous(v):
    print('The bear is only 3 feet away from you and Ms. Kenared. It\'s about to attack you. You know, something must be done to save both your lives.')
    print('You suddenly recalled a kick you learned in the taekwondo lessons you used to take at second grade. Should you try it?')
    l = [
        'type "A" to try the taekwondo-kick on the bear or type "B" to wait for Ms. Kenared to save you'
        , 'It worked! The bear was totally outpowered. You kicked it hard in the face, and it lied there still as if it\'s dead'
        , 'Obviously, Ms. Kenared cannot do anything to stop the bear. The bear severely hurt you.'
    ]
    point = ask_for_input_any(v, 20, l, 'A')
    return point

if __name__ == '__main__':
    name = input('Please enter your name: ')
    print("\nYou are a 5-year old kid who lives in Boston. Both your parents are professors in Harvard. However, one day, you mom tells you that your family is moving to California because they decided to work in a new school named The Webb Schools.")
    print("You are very surprised. Obviously, you don't want to leave all your friends in Boston. So you...")

    l = [
        'type "A" to cry OR type "B" to request a new iPhone from your mom: '
        , '\nMom: OH MY GOD Stop it! '+name+'! You are the most disobedient kid I have ever seen!'
        , '\nMom: OH MY GOD Stop it! '+name+'! You are the most disobedient kid I have ever seen!'
    ]
    ask_for_input_any(relationship, -3, l, 'all')

    relationship = go_to_Webb(relationship)
    fame = settle_down(fame)
    fitness = run_away(courage)
    fame = semester_starts(fame)
    fame = become_famous(fame)
    