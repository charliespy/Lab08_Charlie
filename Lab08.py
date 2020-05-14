#Charlie Sun
#13 May 2020
#Lab08.py

import time

# These are the different stats of the player that change as the game progresses, they're global variables
fame = 10
relationship = 10
strength = 10
love = False

# This is my helper function
def ask_for_input_any(variable, value, l, correct):
    answer = input(str(l[0])) # Ask for an input
    # Determines which one is the correct answer and which one is the wrong one
    if correct == 'A':
        wrong = 'B'
    elif correct == 'B':
        wrong = 'A'
    elif correct == 'all':
        print(l[1])
        variable += value
        return variable

    if answer == correct:
        print(l[1]) # If the player enters the correct answer, then your stats go up/down
        print(type(variable))
        print(type(value))
        variable += value
    elif answer == wrong:
        print(l[2])
    else:
        print('Invalid input, try again!') # If a value that's not A or B is inputted, input again
        ask_for_input_any(variable, value, l, correct)
    return variable

# These are the plot functions that push the plot to move forward (The first one is commented)
def go_to_Webb(v):
    # Some instructions & story-telling before the input
    print("You couldn't do anything else but to go with parents to California the following day.")
    print('However, the moment you guys drove in from the front gate of Webb, you felt something strange.')
    print('You could not figure out what is it that is making you so uncomfortable, so you decided to:  ')
    l = [
        'type "A" to tell your dad about your feelings OR type "B" to keep it in your mind: ' # First one is the instruction of input
        , '\nObviously, your dad was triggered, not only by you, but also the traffic. He yelled: "Can you stop f**king around please! Now shut up because we are about to meet the assistant head of schools Dr.Thmish." THIS WAS NOT HOW YOUR DAD NORMALLY TALKS. You were scared.' # Second one is answer for A
        , '\nYou held your discomfort and did not say anything. The car entered Webb in silence. Everybody was nervous to see the place where you guys are gonna live for the next god knows how many years.' # Third one is answer for B
    ]
    this_point = ask_for_input_any(v, -5, l, "A") # Call the helper function and return the value
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
    point = ask_for_input_any(v, 3, l, 'B')
    return point

def run_away(v):
    print('At this moment, you recalled a Youtube video you saw the other day about making bears\' voices. You decided to give it a try')
    l = [
        'type "A" or "B" to mimic bears\'s voice ---> A = "AHHHHHHHH", B = "RAWWWWWWW": '
        , '\nObviously, this is not how bears talk, but you somehow shocked the bear. It stood there in amazement while you ran away as quick as you could.'
        , '\nWell, that was not the voice of bears, but rather tigers. Bears are afriad of tigers, so is this one. You watched the bear ran away from you in amazement.'
    ]
    point = ask_for_input_any(v, 5, l, 'B')
    return point

def semester_starts(v):
    print('It has been almost a month since the bear incident happened. You guys are on your freshman retreat.')
    print('However, just when you were going on the bus, a huge bear popped out and was walking toward the bus.')
    print('Your advisor, Ms. Kenared, tried to calm people down but in vain. The crowd bursted into a panic.')
    print('For some reason, someone pushed you. You fell hard on the ground, 5 feet away from the bear. What should you do now?')
    l = [
        'type "A" to run back to the bus or type "B" to pretend you\'re dead: '
        , '\nYou ran away, but so did the crowd. Everybody thought you were gonna attract the bear toward them. Only your advisor Ms. Kenared left there with you.'
        , '\nYou lied there, silently. The bear saw you as a plancon seat or something, and tried to sit on you. Luckily, Ms. Kenared sprinted toward you and saved you from the bears\' ass.'
    ]
    this_point = ask_for_input_any(v, -5, l, 'A')
    return this_point

def become_famous(v):
    print('The bear is only 3 feet away from you and Ms. Kenared. It\'s about to attack you. You know, something must be done to save both your lives.')
    print('You suddenly recalled a kick you learned in the taekwondo lessons you used to take at second grade. Should you try it?')
    l = [
        'type "A" to try the taekwondo-kick on the bear or type "B" to wait for Ms. Kenared to save you: '
        , '\nIt worked! The bear was totally outpowered. You kicked it hard in the face, and it lied there still as if it\'s dead'
        , '\nObviously, Ms. Kenared cannot do anything to stop the bear. The bear severely hurt you.'
    ]
    point = ask_for_input_any(v, 10, l, 'A')
    return point

def president(v):
    print('YOU BECAME FAMOUS here at Webb! Your accomplishements quickly spread in the school.')
    print('When you guys came back from retreat, and it was time to elect class president, everyone was crying on you to become the president.')
    print('You didn\'t really want to be the president, but thinking of the strange force that nearly drove you crazy, you thought there might be something in the ASB that can help you')
    print('After you became the president, Mr. Stock, the head master, called you to his office. Should you go or not?')
    l = [
        'type "A" to go and "B" to not go: '
        , '\nYou went, and as soon as you entered his office, you felt that same force that\'s been haunting you for so long.'
        , '\nYou didn\'t want to go, and Mr. Stock was very angry. He hyjacted you and forced you to go. As soon as you entered his office, you felt that same force that\'s been haunting you for so long.'
    ]
    point = ask_for_input_any(v, -10, l, 'B')
    return point

def the_special_force(r, f, s):
    print('This is not nice, you thought as you walked in and saw Mr. Stock facing outside the window.')
    print('Mr. Stock said:"For 99 years, this has been guarding Webb from beasts and wild animals." (took out a black stone)')
    print('I am the 21st guard since 1922, but my time is coming to an end. Therefore I have to pass on this power to someone else --- YOU!')

    answer = input('Type A to ask "Why me" and type B to say "what is the stone\'s power?: "')
    if answer == 'A':
        print('\nBecause you are the ONLY one in your class to be able to sense this power. Other guys can\'t even perceive it.')
        print('Okay you know what? I think I might need a little more time to rethink through this subject of matter. Now go back to your classes!')
        print('THE END: You walked out of the room, with your memory about that incident completely wiped out. The special force has never haunted you ever again till the end of your life.')
    elif answer == 'B':
        print('\nIt will give you unimaginable power, although the side effect is that your body conditions will be devasted.')
        confirmation(r, f, s)
    else:
        print('Invalid input, try again!')
        the_special_power(r,f,s)

# These two are the functions that eventually determine the endings.
def confirmation(r, f, s):
    print('Young man, congradulations! You have passed my first test. Now do you wish to attempt the final trial? If you pass you\'re going to possess the stone an its power!')
    answer = input('Type "A" to proclaim that you want to keep going, or type "B" to say you don\'t want to proceed: ')
    if answer == "A":
        final_trial(r, f, s)
    elif answer == 'B':
        print('\nWell okay, I respect your choice. It\'s a tough decision, but if you ever have a second thought come back to me at any time.')
        print('THE END: You continue to live a normal live, the special force has never haunted you ever again till the end of your life.')
    else:
        print('Invalid input, try again!')
        confirmation(r, f, s)

def final_trial(r, f, s):
    print('Alright now, slowly put your hands on the stone, and if it accepts you, it will blend into your body. If it doesn\'t, it will not blend into your body.')
    print('(You put your hands on the stone and closed your eyes. Something\'s happening, the stone was analyzing all parts of you - your RELATIONSHIP with others, your FAME, strength and everything)')
    print('Now wait for 5 seconds as the stone assesses you...')
    time.sleep(5) # Wait for 5 seconds

    if r>=0 and f>=20 and s>=10:
        print('\nThe stone slowly blended into your body. You instantly felt like you had infinite power, the type of eliminating half of universe with a snap sort of power.')
        print('THE END: Congradulations! You figured out the problem of Webb and successfully became the strongest human on Earth!')
    else: 
        print('\nTHE END: Unfortunately, the stone did not blend into your body. Mr. Stock said:"It\'s okay young man. If you were to relive these days again, would you be able to get it? ...')

# What actually gets excecuted
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
    strength = run_away(strength)
    fame = semester_starts(fame)
    fame = become_famous(fame)
    relationship = president(relationship)
    the_special_force(relationship, fame, strength)