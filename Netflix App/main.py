#Imports
import time
from data_import import get_data, get_show

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
        lookup("actor")
    elif actors_or_show_name == "name" or actors_or_show_name == "show name" or actors_or_show_name == "show":
        lookup("name")
    else:
        return lookup_init(1)

def lookup(type):
    working_list = None
    final_list = []
    if type == "name":
        working_list = get_data("name")
        print("Please enter part or all of a show's name.")
    elif type == "actor":
        working_list = get_data("actor")
        print("Please enter part or all of an actor's name.")
    while True:
        user_input = input().strip()
        list_of_matches = []
        for item in working_list:
            if user_input in item:
                list_of_matches.append(item)
        if len(list_of_matches) > 10:
            print("Please make your search more specific.")
            time.sleep(1.2)
            continue
        else:
            final_list += list_of_matches
            break
    if type == "name":
        print("We have found the following shows from our records.")
        time.sleep(1.2)
        print("Please enter the number of your intended show for more information.")
    elif type == "actor":
        print("We have found the following actors from our records.")
        time.sleep(1.2)
        print("Please enter the number that correlates to the name of your intended actor.")
    working_dict = {} 
    idx_track = 0
    for actor in final_list:
        working_dict[str(idx_track)] = actor
        idx_track += 1
    #printing the dictionary in a more readable fashion
    for key, value in working_dict.items():
        print(key + ": " + value)
    final_selection = input_helper(working_dict)
    print("You have selected " + working_dict[final_selection])
    time.sleep(1.2)
    if type == "name":
        print("Here is some more information about this show:")
        time.sleep(1.2)
        list_shows_and_info(get_show("name", working_dict[final_selection]))
    elif type == "actor":
        print("Here is a list of shows this actor has appeared in.")
        time.sleep(1.2)
        list_shows_and_info(get_show("actor", working_dict[final_selection]))

    
def input_helper(dict):
    a_input = input().strip()
    num_options = []
    for num in dict:
        num_options.append(num)
    for option in num_options:
        if a_input == option:
            return option
    print("Please enter a valid option.")
    return input_helper(dict)

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