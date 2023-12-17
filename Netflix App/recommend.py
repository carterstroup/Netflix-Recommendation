import time
import pandas as pd
from data import flatten

#CURRENT STATE: It will currently print out the genres that match the first three parameters if there are more than five shows left
#what needs to happen is for it to take that list, present five of them at a time (around 20 will return max) and ask if they are interested
# in them. If they are, add it to a list until you have 3 or so genres, then re-run the program to hopefully return something,
# each time they pick something, the next element needs to be loaded into the dict visible and there needs to be an option for none of these
# at that point the main functionailty will be done and everyting needs to be connected and significantly simplified












def recommend_init():
    options_list = []
    print("Awesome! I'll ask you a few questions to better understand what you are looking for, then offer you suggestions!")
    time.sleep(1.2)
    print("Would you like to watch a TV Show or Movie?")
    tv_or_movie = input().strip().lower()
    if "tv" in tv_or_movie or "television" in tv_or_movie:
        options_list.append("TV Show")
        print("We will stick to TV shows in our recommendations.")
        time.sleep(1.2)
        print("Which decade do you want your TV show from? (1940s-2020s)")
        decade_choice = input().strip().lower()
        if "1940" in decade_choice:
            options_list.append("1940")
        elif "1950" in decade_choice:
            options_list.append("1950")
        elif "1960" in decade_choice:
            options_list.append("1960")
        elif "1970" in decade_choice:
            options_list.append("1970")
        elif "1980" in decade_choice:
            options_list.append("1980")
        elif "1990" in decade_choice:
            options_list.append("1990")
        elif "2000" in decade_choice:
            options_list.append("2000")
            print("We think the 2000s were pretty cool too.")
            time.sleep(1.2)
            print("Do you have a rating preference (TV-Y, TV-G, TV-PG, TV-14, TV-MAm or No Preference)?")
            rating_pref = input().strip().lower()
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
                print("You have selected TV-MA.")
                check_result = get_results_first(options_list)
                if type(check_result) == list:
                    print(check_result)
                else:
                    list_shows_and_info(get_results_first(options_list))
            elif "no" in rating_pref:
                options_list.append("n")
        elif "2010" in decade_choice:
            options_list.append("2010")
        elif "2020" in decade_choice:
            options_list.append("2020")
    elif "movie" in tv_or_movie:
        options_list.append("movie")
    else:
        #handle exception
        pass
    
def get_results_first(options):
    
    return_list = {}
    return_genres = []
    
    options_year_complete = options[1]
    options_year_sliced = options_year_complete[:-1]
    
    data = pd.read_csv('netflix_titles.csv', skip_blank_lines=True)
    data.fillna('Not Available', inplace=True)
    data_dict = data.to_dict(orient='records')
    
    for show in data_dict:
        if show["type"] == options[0]:
            if options_year_sliced in str(show["release_year"]):
                if show["rating"] == options[2]:
                    return_list[show["show_id"]] = show
                    return_genres.append(show["listed_in"])
    
    if len(return_list) > 5:
        starting_list = []
        for item in return_genres:
            split = item.split(",")
            starting_list.append(split)
        flat_list = flatten(starting_list)
        final_list = []
        #removes whitespace in strings and removes duplicates by converting it to a dict and back
        for item in flat_list:
            final_list.append(item.strip())
        no_duplicates_list = list(dict.fromkeys(final_list))
        return no_duplicates_list
    
    return return_list

def list_shows_and_info(show_dict):
    key_list = [] #holds a list of dict keys
    #appends key_list with the keys of each nested dict
    for key in show_dict:
        key_list.append(key)
    #prints out the info in each nested dict using the nested keys in key_list
    for key in key_list:
        print("")
        print("---------------------------------------")
        if show_dict[key]["type"] == "Movie":
            print("Movie Name: " + show_dict[key]["title"])
        else:
            print("TV Show Name: " + show_dict[key]["title"])
        print("Release Year: " + str(show_dict[key]["release_year"]))
        print("Rating: " + show_dict[key]["rating"])
        print("Duration: " + show_dict[key]["duration"])
        print("Genre: " + show_dict[key]["listed_in"])
        print("Description: " + show_dict[key]["description"])
        print("---------------------------------------")
        print("")
        
        
recommend_init()