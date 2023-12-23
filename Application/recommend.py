#Imports
import time
from data import list_shows_and_info, get_genres_by_option, get_shows_by_genre, get_user_input

#Prints messages with delay for readability.
#Runtime: O(1)
def print_message(message):
    print(message)
    time.sleep(1.2)

#Starts and manages the recommendation program up to the genre selection.
#Runtime: O(1)
def recommend_init(run_num=0):
    if run_num == 0:
        print("Awesome! Let's start with a few questions.")
    else:
        print("We couldn't find a match for your search. Please try again.")
    time.sleep(1.2)
    #Gets data from input functions before compiling it and sending it to the genre function.
    show_category = get_category()
    show_year_and_category = get_year(show_category)
    full_options_list = None
    if show_year_and_category[0] == "TV Show":
        full_options_list = get_rating_tv(show_year_and_category)
    elif show_year_and_category[0] == "Movie":
        full_options_list = get_rating_movie(show_year_and_category)
    get_genres(full_options_list)

#Displays a list of genres for selection in an easy to read way.
#Runtime: O(n)
def display_genre_options(working_dict):
    print("Please choose up to three categories by entering their number followed by a space (e.g., 3 6 7)")
    for key, value in working_dict.items():
        print(f"{key}: {value}")

#Converts the user number input back into the String name of the genre selected.
#Runtime: O(n)
def convert_input_to_genre_names(working_dict):
    genre_selections = input().strip()
    try:
        genre_selections_list = None
        if len(genre_selections) == 1:
            genre_selections_list = [working_dict[genre_selections]]
        else:
            new_array_used = []
            genre_selections_list = genre_selections.split()
            for i in genre_selections_list:
                new_array_used.append(working_dict[i])
            genre_selections_list = new_array_used
        return genre_selections_list
    except:
        return None  # Handle invalid input

#Manages the entire process of displaying genres, taking responses, and displaying results using helper functions above.
#Runtime: O(n)
def get_genres(options):
    while True:
        options_list = options
        check_result = get_genres_by_option(options_list)
        if check_result == "0":
            recommend_init(1)
        if type(check_result) == list:
            time.sleep(1.2)
            display_genre_options_dict = {}
            idx_track = 0
            for item in check_result:
                display_genre_options_dict[str(idx_track)] = item
                idx_track += 1
            display_genre_options(display_genre_options_dict)
            genre_selections_list = convert_input_to_genre_names(display_genre_options_dict)
            if genre_selections_list is not None:
                options_list.append(genre_selections_list)
                time.sleep(1.2)
                print("We have found these shows we think you'll love!")
                time.sleep(1.2)
                list_shows_and_info(get_shows_by_genre(options_list))
                break  # Exit the loop if valid input is received
        else:
            print("Invalid input. Please try again.")
            
#Asks and retrieves the user input for TV Show ratings.
#Runtime: O(1)
def get_rating_tv(options):
    options_list = options
    rating_pref = get_user_input("Do you have a rating preference (TV-Y, TV-G, TV-PG, TV-14, TV-MA, or No Preference)?", ["tv-y", "tv-g", "tv-pg", "tv-14", "tv-ma", "no preference"], "Please enter a valid option (e.g., 'TV-G' or 'No Preference').")
    if "tv-y" in rating_pref:
        options_list.append("TV-Y")
    elif "tv-g" in rating_pref:
        options_list.append("TV-G")
    elif "tv-pg" in rating_pref:
        options_list.append("TV-PG")
    elif "tv-14" in rating_pref:
        options_list.append("TV-14")
    elif "tv-ma" in rating_pref:
        options_list.append("TV-MA")
    elif "no" in rating_pref:
        options_list.append("")
    print_message(f"Great! We will stick to TV shows rated {rating_pref.capitalize()}.")
    return options_list

#Gets the wanted rating for movie search.
#Runtime: O(1)
def get_rating_movie(options):
    options_list = options
    rating_pref = get_user_input("Do you have a rating preference (G, PG, PG-13, R, NC-17, or No Preference)?", ["g", "pg", "pg-13", "r", "nc-17", "no preference"], "Please enter a valid option (e.g., 'PG' or 'No Preference').")
    if "pg-13" in rating_pref:
        options_list.append("PG-13")
        return
    elif "pg" in rating_pref:
        options_list.append("PG")
        return
    elif "g" in rating_pref:
        options_list.append("G")
        return
    elif "r" in rating_pref:
        options_list.append("R")
    elif "nc-17" in rating_pref:
        options_list.append("NC-17")
    elif "no preference" in rating_pref:
        options_list.append("")
    print_message(f"Great! We will stick to movies rated {rating_pref.capitalize()}.")
    return options_list

#Asks for TV Shows or Movie search.
#Runtime: O(1)
def get_category():
    options_list = []
    tv_or_movie = get_user_input("Would you like to watch a TV Show or Movie?", ["tv", "television", "movie", "tv show", "television show"], "Please enter a valid option (e.g., 'TV').")
    options_list.append("TV Show" if "tv" in tv_or_movie else "Movie")
    print_message(f"Great! We will find you an excellent match.")
    return options_list

#Asks and retrieves the input for the decade of the show.
#Runtime: O(1)
def get_year(options):
    options_list = options
    decade_options = ["1940", "1950", "1960", "1970", "1980", "1990", "2000", "2010", "2020", "1940s", "1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s", "2020s"]
    decade_choice = get_user_input("Which decade do you want your TV show from? (1940s-2020s)", decade_options, "Please enter a valid decade (e.g., '2010' or '1960').")
    if "1940" in decade_choice:
        options_list.append("194")
    elif "1950" in decade_choice:
        options_list.append("195")
    elif "1960" in decade_choice:
        options_list.append("196")
    elif "1970" in decade_choice:
        options_list.append("197")
    elif "1980" in decade_choice:
        options_list.append("198")
    elif "1990" in decade_choice:
        options_list.append("199")
    elif "2000" in decade_choice:
        options_list.append("200")
    elif "2010" in decade_choice:
        options_list.append("201")
    elif "2020" in decade_choice:
        options_list.append("202")
    print_message(f"{decade_choice.capitalize()} is a great choice.")
    return options_list
