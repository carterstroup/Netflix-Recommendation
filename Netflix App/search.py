#Imports
import time
from data import get_search_data, get_show_by_search, list_shows_and_info, get_user_input

#Allows the user to choose between searching by actors or by the name of the show.
#Uses a helper function (lookup_input_helper) to get user input and validate it.
#Runtime: O(1)
def search_init():
    user_choice = get_user_input("Would you like to search by an actor or the name of a show?", ["actor", "actors", "search by actors", "search for actors", "name", "show name", "show"], "Please enter 'name' or 'actor'.")
    if "actor" in user_choice:
        lookup("actor")
    elif "show" in user_choice or "name" in user_choice:
        lookup("name")

#Searches the data sourced in data.py by actor or name (indicated by 'type' argument) depending on user choice earlier in the program.
#It then passes on the narrowed data to get_selection.
#Runtime: O(n)
def lookup(type):
    working_list = None #will be assigned a list of actors or show titles based on user search method
    final_list = [] #the list that will be returned
    #modifies working_list based on user search option, indicated in the functions arguments
    if type == "name":
        working_list = get_search_data("name")
        print("Please enter part or all of a show's name.")
    elif type == "actor":
        working_list = get_search_data("actor")
        print("Please enter part or all of an actor's name.")
    #runs through all of the data in working_list comparing it to the user input (search).
    #it will then append the matching data to a list, if the list is greater than 9, the program will ask for a more specific search.
    #If the list is empty, it will ask for a different search.
    #If the list is between 1-9, it will pass the data on to get_selection
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
        elif len(list_of_matches) == 0:
            print("There were no results for your search. Please try something else.")
            time.sleep(1.2)
            continue
        else:
            final_list += list_of_matches
            break
    get_selection(type, final_list)
             
#takes the list of 1-9 names or show titles from lookup, presents the data for the user to choose, then passes the selection
#on to list_shows_and_info for the final result to be displayed.
#Runtime: O(n)
def get_selection(type, output_list):
    if type == "name":
        print("We have found the following shows from our records.")
        time.sleep(1.2)
        print("Please enter the number of your intended show for more information.")
    elif type == "actor":
        print("We have found the following actors from our records.")
        time.sleep(1.2)
        print("Please enter the number of your intended actor for a list of shows.")
    working_dict = {} #will eventually house a number that corresponds to an option passed into the function
    idx_track = 0 #tracks the index of the list to assign that same number to the key for working_dict
    #iterates through the list passed in and assigns each to the working_dict
    for item in output_list:
        working_dict[str(idx_track)] = item
        idx_track += 1
    #Prints the dictionary in user-friendly fashion, rather than in dict form
    for key, value in working_dict.items():
        print(key + ": " + value)
    #uses the input_helper helper function to validate the user choice as an actual option based on the dict
    final_selection = input_helper(working_dict)
    print("You have selected " + working_dict[final_selection])
    time.sleep(1.2)
    #finishes the function by calling list_shows_and_info on the final user selection
    if type == "name":
        print("Here is some more information about this show:")
        time.sleep(1.2)
        list_shows_and_info(get_show_by_search("name", working_dict[final_selection]))
    elif type == "actor":
        print("Here is a list of shows this actor has appeared in.")
        time.sleep(1.2)
        list_shows_and_info(get_show_by_search("actor", working_dict[final_selection]))        

#helps get_selection by validating the input is in the dict and returns the valid choice as a key to the dict
#Runtime: O(n)
def input_helper(dict):
    a_input = input().strip()
    num_options = [] #houses keys from passed in dict, which are input options
    #adds the keys to num_options
    for num in dict:
        num_options.append(num)
    #checks if the user input matches an option in num_options
    for option in num_options:
        if a_input == option:
            return option
    print("Please enter a valid option.")
    return input_helper(dict)