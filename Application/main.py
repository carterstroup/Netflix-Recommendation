#Imports
import time
from recommend import recommend_init
from search import search_init

#Asks the user if they wish to use the search or recommendation feature and 
#calls the appropriate function using a helper function (get_start_input)
#Runtime: O(1)
def program_start(run_num=0):
    if run_num == 0: #checks if this is the first time the function has been called.
        print("Welcome to the Netflix Search and Recommendation Platform!")
        time.sleep(1)
        print("Would you like to search for a show or get a recommendation?")
        get_start_input()
    else:
        print("Please enter 'recommendation' or 'search'.")
        get_start_input()
        
#Gets the user input to help the program_start function.
#It ensures the input is valid, and calls the appropriate function. 
#Runtime: O(1)         
def get_start_input():
    valid_recommendation_inputs = ["recommend", "recomend", "recommendation", "recommendations", "get a recommendation"]
    valid_search_inputs = ["lookup", "look up", "search", "search for a show"]
    movie_or_show_selection = input().strip().lower()
    if movie_or_show_selection in valid_search_inputs:
        search_init()
    elif movie_or_show_selection in valid_recommendation_inputs:
        recommend_init()
    else:
        return program_start(1) #the input was not valid, it will start the process over again

#Start the program
program_start()