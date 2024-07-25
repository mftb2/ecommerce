def introduction():
    print("You are a brave little dog named Max. One day, you wander into the woods while chasing a butterfly.")
    print("Suddenly, you realize you are lost! Your adventure begins now.")
    print("1. Search for a way back home.")
    print("2. Explore the forest further.")
    print("3. Sit down and wait for help.")

def search_for_home():
    print("\nYou decide to search for a way back home.")
    print("After a while, you come across a fork in the path.")
    print("1. Take the left path.")
    print("2. Take the right path.")

    choice = input("Which path will you choose? (1 or 2): ")
    if choice == '1':
        encounter_with_ranger()
    elif choice == '2':
        meet_other_dog()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        search_for_home()

def explore_forest():
    print("\nYou decide to explore the forest further.")
    print("You come across a beautiful clearing with a stream and some berries.")
    print("1. Drink water from the stream.")
    print("2. Eat some berries.")

    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        drink_water()
    elif choice == '2':
        eat_berries()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        explore_forest()

def sit_and_wait():
    print("\nYou decide to sit down and wait for help.")
    print("Hours pass, and you start to get hungry and tired.")
    print("Suddenly, you hear footsteps approaching!")
    print("1. Bark loudly to get attention.")
    print("2. Remain quiet and hope for the best.")

    choice = input("What will you do? (1 or 2): ")
    if choice == '1':
        rescue_by_hiker()
    elif choice == '2':
        rescue_by_search_party()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        sit_and_wait()

def encounter_with_ranger():
    print("\nYou take the left path and soon meet a friendly ranger.")
    print("The ranger helps you find your way back home!")
    print("Congratulations, you made it back safely!")

def meet_other_dog():
    print("\nYou take the right path and meet another friendly dog.")
    print("The dog guides you back to your home!")
    print("Congratulations, you made it back safely!")

def drink_water():
    print("\nYou drink some refreshing water from the stream.")
    print("You feel much better and decide to head back home.")
    print("On the way, you find a ranger who helps you find your way back home!")
    print("Congratulations, you made it back safely!")

def eat_berries():
    print("\nYou eat some berries from the clearing.")
    print("Unfortunately, the berries were not good for you.")
    print("You feel sick and a search party eventually finds you and takes you home.")
    print("You’re home, but be careful about what you eat in the forest!")

def rescue_by_hiker():
    print("\nYou bark loudly to get attention.")
    print("A hiker hears you and comes to your rescue.")
    print("The hiker helps you find your way back home!")
    print("Congratulations, you made it back safely!")

def rescue_by_search_party():
    print("\nYou remain quiet and hope for the best.")
    print("After a long time, a search party finally finds you.")
    print("You’re tired and hungry but are safely taken back home.")
    print("Be more careful next time!")

def start_adventure():
    introduction()
    choice = input("What will you do? (1, 2, or 3): ")
    if choice == '1':
        search_for_home()
    elif choice == '2':
        explore_forest()
    elif choice == '3':
        sit_and_wait()
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        start_adventure()

# Start the adventure
start_adventure()
