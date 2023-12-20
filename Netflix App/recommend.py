#Imports
import time
from data import list_shows_and_info, get_genres_by_option, get_shows_by_genre

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

#Takes the options list from recommend_init, retrieves a list of show genres matching these options with helper functions.
#It then presents these options and manages the input.
#Runtime: O(n)
def get_genres(options, run_num=0):
    if run_num != 0:
        print("Invalid Input. Please try again.")
    options_list = options
    check_result = get_genres_by_option(options_list)#gets a list of shows, if there are fewer than five it will print them, otherwise it will print the genre options and execute
    if check_result == "0":
        recommend_init(1)
    if type(check_result) == list: #if its a list it means genres were returned, not results
        #assigns nums to the dict and prints it out
        time.sleep(1.2)
        print("Please choose up to three categories by entering their number followed by a space (i.e. 3 6 7)")
        working_dict = {} #will eventually house a number that corresponds to an option passed into the function
        idx_track = 0 #tracks the index of the list to assign that same number to the key for working_dict
        #iterates through the list passed in and assigns each to the working_dict
        for item in check_result:
            working_dict[str(idx_track)] = item
            idx_track += 1
        #Prints the dictionary in user-friendly fashion, rather than in dict form
        for key, value in working_dict.items():
            print(key + ": " + value)
        
        #Converts the number inputs back into genre names before passing it on to the function that searches for shows.
        genre_selections = input().strip()
        try: #will except if the input is not a valid option
            genre_selections_list = None
            if len(genre_selections) == 1:
                genre_selections_list = [working_dict[genre_selections]]
            else:
                new_array_used = []
                genre_selections_list = genre_selections.split()
                for i in genre_selections_list:
                    new_array_used.append(working_dict[i])
                genre_selections_list = new_array_used
        except:
            return get_genres(options_list, 1)
        options_list.append(genre_selections_list)
        time.sleep(1.2)
        print("We have found these shows we think you'll love!")
        time.sleep(1.2)
        list_shows_and_info(get_shows_by_genre(options_list))
    else:
        time.sleep(1.2)
        list_shows_and_info(get_genres_by_option(options_list)) 

#Asks and retrieves the user input for TV Show ratings.
#Runtime: O(1)
def get_rating_tv(options, run_num=0):
    options_list = options
    if run_num == 0:
        time.sleep(1.2)
        print("Do you have a rating preference (TV-Y, TV-G, TV-PG, TV-14, TV-MA or No Preference)?")
    else:
        print("Please enter a valid option (i.e. 'TV-G' or 'No Preference').")
    rating_pref = input().strip().lower()
    if len(rating_pref) < 14:
        if "tv-y" in rating_pref:
            options_list.append("TV-Y")
            print("We will stick to TV-Y shows.")
        elif "tv-g" in rating_pref:
            options_list.append("TV-G")
            print("We will stick to TV-G shows.")
        elif "tv-pg" in rating_pref:
            options_list.append("TV-PG")
            print("We will stick to TV-PG shows.")
        elif "tv-14" in rating_pref:
            options_list.append("TV-14")
            print("We will stick to TV-14 shows.")
        elif "tv-ma" in rating_pref:
            options_list.append("TV-MA")
            print("We will stick to TV-MA shows.")
        elif "no" in rating_pref:
            options_list.append("")
            print("We won't search via rating.")
        else:
            return get_rating_tv(options, 1)
    else:
        return get_rating_tv(options, 1)
    return options_list

#Works the same as the TV function, but asks questions pertinent to movies instead.
#Runtime: O(1)
def get_rating_movie(options, run_num=0):
    options_list = options
    if run_num == 0:
        time.sleep(1.2)
        print("Do you have a rating preference (G, PG, PG-13, R, NC-17, or No Preference)?")
    else:
        print("Please enter a valid option (i.e. 'PG' or 'No Preference').")
    rating_pref = input().strip().lower()
    if len(rating_pref) < 14:
        if "pg-13" in rating_pref:
            options_list.append("PG-13")
            print("We will stick PG-13 movies.")
            return options_list
        elif "pg" in rating_pref:
            options_list.append("PG")
            print("We will stick to PG movies.")
            return options_list
        elif "g" in rating_pref:
            options_list.append("G")
            print("We will stick to G movies.")
            return options_list
        elif "r" in rating_pref:
            options_list.append("R")
            print("We will stick to R movies.")
        elif "nc-17" in rating_pref:
            options_list.append("NC-17")
            print("We will stick to NC-17 movies.")
        elif "no" in rating_pref:
            options_list.append("")
            print("We won't sort via rating.")
        else:
            return get_rating_movie(options, 1)
    else:
        return get_rating_movie(options, 1)
    return options_list

#Asks and retrieves TV show or movie.
#Runtime: O(1)
def get_category(run_num=0):
    options_list = []
    if run_num == 0:
        time.sleep(1.2)
        print("Would you like to watch a TV Show or Movie?")
    else:
        print("Please enter a valid option (i.e. 'TV').")
    tv_or_movie = input().strip().lower()
    if len(tv_or_movie) < 11:
        if "tv" in tv_or_movie or "television" in tv_or_movie:
            options_list.append("TV Show")
            print("Great! We will find you an excellent TV Show.")
        elif "movie" in tv_or_movie:
            options_list.append("Movie")
            print("Great! We will find you an excellent Movie.")
        else:
            return get_category(1)
    else:
        return get_category(1)
    return options_list

#Asks and retrieves the input for the decade of the show.
#Runtime: O(1)
def get_year(options, run_num=0):
    if run_num == 0:
        time.sleep(1.2)
        print("Which decade do you want your TV show from? (1940s-2020s)")
    else:
        print("Please enter a valid decade. (i.e. '2010' or '1960')")
    options_list = options
    decade_choice = input().strip().lower()
    if len(decade_choice) < 6:
        if "1940" in decade_choice:
            options_list.append("1940")
            print("We think the 1940s were pretty cool too.")
        elif "1950" in decade_choice:
            options_list.append("1950")
            print("The 1950s were certainly an excellent time!")
        elif "1960" in decade_choice:
            options_list.append("1960")
            print("We think the 1960s were pretty cool too.")
        elif "1970" in decade_choice:
            options_list.append("1970")
            print("The 1970s were certainly an excellent time!")
        elif "1980" in decade_choice:
            options_list.append("1980")
            print("We think the 1980s were pretty cool too.")
        elif "1990" in decade_choice:
            options_list.append("1990")
            print("The 1990s were certainly an excellent time!")
        elif "2000" in decade_choice:
            options_list.append("2000")
            print("We think the 2000s were pretty cool too.")
        elif "2010" in decade_choice:
            options_list.append("2010")
            print("The 2010s were certainly an excellent time!")
        elif "2020" in decade_choice:
            options_list.append("2020")
            print("We think the 2020s are pretty cool too.")
        else:
            return get_year(options, 1)
    else:
        return get_year(options, 1)
    return options_list