#Imports
import time
from data_import import get_actors, get_show_by_actor, get_show_list, get_show_by_show

#Initialization
#Asks the user if they wish to use the search or recommendation function and calls the appropriate function
def program_start(run_num):
    if run_num == 0:
        print("Welcome to the Netflix Search and Recommendation Platform!")
        time.sleep(1)
        print("Would you like to search or get a recommendation?")
        get_start_input()
    else:
        print("Please enter 'recommendation' or 'search'.")
        get_start_input()
        
#gets the user input to assist the program start function            
def get_start_input():
    movie_or_show_selection = input().strip().lower()
    if movie_or_show_selection == "lookup" or movie_or_show_selection == "look up" or movie_or_show_selection == "search":
        lookup_init(0)
    elif movie_or_show_selection == "recommend" or movie_or_show_selection == "recomend" or movie_or_show_selection == "recommendation" or movie_or_show_selection == "recommendations":
        pass
        #call recommendation function
    else:
        return program_start(1)

#Lookup Function: Allows the user to search Netflix shows based on the name or actors
def lookup_init(run_num):
    if run_num == 0:
        print("Would you like to search by actors or the name of a show?")
        lookup_input_helper()
    else:
        print("Please enter 'name' or 'actor'.")
        lookup_input_helper()

#assists with managing the user input for the lookup_init
def lookup_input_helper():
    actors_or_show_name = input().strip().lower()
    if actors_or_show_name == "actor" or actors_or_show_name == "actors" or actors_or_show_name == "search by actors" or actors_or_show_name == "search for actors":
        lookup_actor()
    elif actors_or_show_name == "name" or actors_or_show_name == "show name" or actors_or_show_name == "show":
        lookup_show_name()
    else:
        return lookup_init(1)
    
    
def lookup_show_name():
    list_of_shows = get_show_list()
    final_show_list = []
    
    print("Please enter part or all of the show name")
    while True:
        user_input = input().strip()
        list_of_matches = []
        for actor in list_of_shows:
            if user_input in actor:
                list_of_matches.append(actor)
        if len(list_of_matches) > 10:
            print("Please make your search more specific.")
            time.sleep(1.2)
            continue
        else:
            final_show_list += list_of_matches
            break
        
    print("Our records have found these shows.")
    time.sleep(1.2)
    print("Please enter the number that correlates to the name of your intended show for more info.")
    show_and_number_dict = {} #assigns a number to the actor for easy input selection
    idx_track = 0
    for actor in final_show_list:
        show_and_number_dict[str(idx_track)] = actor
        idx_track += 1
    #printing the dictionary in a more readable fashion
    for key, value in show_and_number_dict.items():
        print(key + ": " + value)

    actor_selection = actor_selection_input_helper(show_and_number_dict)
    
    print("You have selected " + show_and_number_dict[actor_selection])
    time.sleep(1.2)
    print("This actor has appear in the following movies and TV Shows")
    time.sleep(1.2)
    list_shows_and_info(get_show_by_show(show_and_number_dict[actor_selection]))
    
    
    
    
    
    
    

#Searches the Netflix shows based on a full or partial actor name.
def lookup_actor():
    list_of_actors = get_actors()
    final_actor_list = []
    #requests an input until the resulting actor list is 9 or fewer
    print("Please enter part or all of an actors name.")
    while True:
        user_input = input().strip()
        list_of_matches = []
        for actor in list_of_actors:
            if user_input in actor:
                list_of_matches.append(actor)
        if len(list_of_matches) > 10:
            print("Please make your search more specific.")
            time.sleep(1.2)
            continue
        else:
            final_actor_list += list_of_matches
            break
    #display the actors that were found in the search
    print("Our records have found these actors.")
    time.sleep(1.2)
    print("Please enter the number that correlates to the name of your intended actor.")
    actor_and_number_dict = {} #assigns a number to the actor for easy input selection
    idx_track = 0
    for actor in final_actor_list:
        actor_and_number_dict[str(idx_track)] = actor
        idx_track += 1
    #printing the dictionary in a more readable fashion
    for key, value in actor_and_number_dict.items():
        print(key + ": " + value)

    actor_selection = actor_selection_input_helper(actor_and_number_dict)
    
    print("You have selected " + actor_and_number_dict[actor_selection])
    time.sleep(1.2)
    print("This actor has appear in the following movies and TV Shows")
    time.sleep(1.2)
    list_shows_and_info(get_show_by_actor(actor_and_number_dict[actor_selection]))
    
def actor_selection_input_helper(dict):
    a_input = input().strip()
    num_options = []
    for num in dict:
        num_options.append(num)
    for option in num_options:
        if a_input == option:
            return option
    print("Please enter a valid option.")
    return actor_selection_input_helper(dict)

def list_shows_and_info(show_list):
    key_list = []
    for key in show_list:
        key_list.append(key)
    for key in key_list:
        show = show_list
        print("")
        print("---------------------------------------")
        if show[key]["type"] == "Movie":
            print("Movie Name: " + show[key]["title"])
            print("Release Year: " + str(show[key]["release_year"]))
            print("Rating: " + show[key]["rating"])
            print("Genre: " + show[key]["listed_in"])
            print("Description: " + show[key]["description"])
            print("---------------------------------------")
            print("")
        else:
            print("TV Show Name: " + show[key]["title"])
            print("Release Year: " + str(show[key]["release_year"]))
            print("Rating: " + show[key]["rating"])
            print("Duration: " + show[key]["duration"])
            print("Genre: " + show[key]["listed_in"])
            print("Description: " + show[key]["description"])
            print("---------------------------------------")
            print("")

#Recommendation Function: Suggests shows/movies to the user based on questions asked about ratings, country, genre, etc.

#Function Calls / Application Management
program_start(0)