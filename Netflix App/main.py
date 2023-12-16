#Imports
import time
from data_import import get_search_data, get_actors, get_show_by_actor

#Initialization
#Asks the user if they wish to use the search or recommendation function and calls the appropriate function
def program_start():
    print("Welcome to the Netflix Search and Recommendation Platform!")
    time.sleep(1)
    print("Would you like to search or get a recommendation?")
    movie_or_show_selection = input().strip().lower()
    if movie_or_show_selection == "lookup" or "look up" or "search":
        lookup_init()
    elif movie_or_show_selection == "recommend":
        pass
        #call recommendation function
    else:
        pass
        #ensure input is valid

#Lookup Function: Allows the user to search Netflix shows based on the name or actors
def lookup_init():
    print("Would you like to search by actors or the name of a show?")
    actors_or_show_name = input().strip().lower()
    if actors_or_show_name == "name" or "actor" or "actors" or "search by actors" or "search for actors":
        lookup_actor()
    elif actors_or_show_name == "actors":
        pass
        #call actor lookup function
    else:
        pass
        #deal with inputs other than expected

#Searches the Netflix shows based on a full or partial actor name.
def lookup_actor():
    list_of_actors = get_actors()
    final_actor_list = []
    #requests an input until the resulting actor list is 9 or fewer
    while True:
        print("Please enter part or all of an actors name.")
        user_input = input().strip()
        list_of_matches = []
        for actor in list_of_actors:
            if user_input in actor:
                list_of_matches.append(actor)
        if len(list_of_matches) > 10:
            print("Please make your search more specific.")
            continue
        else:
            final_actor_list += list_of_matches
            break
    #display the actors that were found in the search
    print("Our records have found these actors.")
    print("Please enter the number that correlates to the name of your intended actor for a list of Netflix shows and movies")
    actor_and_number_dict = {} #assigns a number to the actor for easy input selection
    idx_track = 0
    for actor in final_actor_list:
        actor_and_number_dict[str(idx_track)] = actor
        idx_track += 1
        
    print(actor_and_number_dict)
    
    actor_selection = input()
    
    print("You have selected " + actor_and_number_dict[actor_selection])
    
    print("This actor has appear in the following moviews and TV Shows")
    
    list_shows_and_info(get_show_by_actor(actor_and_number_dict[actor_selection]))

def lookup_name():
    pass

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
program_start()