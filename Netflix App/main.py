#Imports
import time
from data_import import get_search_data, get_authors, get_show_by_actor

#Initialization
def program_start():
    print("Welcome to the Netflix Show/Movie Search and Recomendation Platform")
    time.sleep(1)
    print("Would you like to search for a show or have the program make a recomendation?")
    movie_or_show_selection = input()
    if movie_or_show_selection == "lookup":
        pass
        #call lookup function
    elif movie_or_show_selection == "recomend":
        pass
        #call recomendation function

#Lookup Function: Allows the user to search Netflix shows based on the name or actors
def lookup_init():
    print("Would you like to search via actors or the name of the show")
    actors_or_show_name = input()
    if actors_or_show_name == "name":
        pass
        #call name lookup function
    elif actors_or_show_name == "actors":
        pass
        #call actor lookup function
    
def lookup_actor():
    list_of_authors = get_authors()
    print("Please type part or all of an actor's name")
    actor_input = input()
    list_of_init_matches = []
    for actor in list_of_authors:
        if actor_input in actor:
            list_of_init_matches.append(actor)
    final_actor_list = []
    while True:
        print("We need to narrow the search further, please enter a more specific name")
        more_specific_input = input()
        list_of_nxt_matches = []
        for actor in list_of_authors:
            if more_specific_input in actor:
                list_of_nxt_matches.append(actor)
        if len(list_of_nxt_matches) > 10:
            continue
        else:
            final_actor_list += list_of_nxt_matches
            break
    print("Our records have found these actors.")
    print("Please enter the number that correlates to the name of your intended actor for a list of Netflix shows and movies")
    author_and_number_dict = {}
    idx_track = 0
    for actor in final_actor_list:
        author_and_number_dict[str(idx_track)] = actor
        idx_track += 1
        
    print(author_and_number_dict)
    
    actor_selection = input()
    
    print("You have selected " + author_and_number_dict[actor_selection])
    
    print("This actor has appeard in the following moviews and TV Shows")
    
    list_shows_and_info(get_show_by_actor(author_and_number_dict[actor_selection]))

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


#Recomendation Function: Suggests shows/movies to the user based on questions asked about ratings, country, genre, etc.

#Function Calls / Application Management
#program_start()
lookup_actor()