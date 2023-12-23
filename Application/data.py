#Imports
import pandas as pd
import time

#Memoization:
complete_csv_data = None

#Gets and validates inputs.
#Runtime: O(1)
def get_user_input(prompt, valid_options=None, error_message="Invalid input. Please try again."):
    while True:
        print(prompt)
        user_input = input().strip().lower()
        if valid_options is not None and user_input not in valid_options:
            print(error_message)
            continue
        return user_input

#Takes a nested array and turns it into a one-dimensional array
#Runtime: O(n)
def flatten(nested_list):
    result = []
    for item in nested_list:
        if hasattr(item, "__iter__") and not isinstance(item, str):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

#Retrieves the whole CSV file in a nested dict.
#Runtime: O(1)
def get_complete_csv_data(memoized, file_name="netflix_titles.csv"):
    if memoized == None:
        #splits the year to the first three digits to determine the decade
        #reads the data, could be memoized
        data = pd.read_csv(file_name, skip_blank_lines=True)
        data.fillna('Not Available', inplace=True)
        data_dict = data.to_dict(orient='records')
        complete_csv_data = data_dict
        return data_dict
    else:
        return complete_csv_data

#retrieves a list of actors or show names from the csv file and stores them in a list
#cleans the data in the process by skipping blanks, changing non-values to 'Not Available' and removes duplicates
#O(n)
def get_search_data(type, file_name="netflix_titles.csv"):
    #gets certain data based on need to reduce runtime
    if type == "name":
        df = pd.read_csv(file_name, usecols=['title'], skip_blank_lines=True)
    elif type == "actor":
        df = pd.read_csv(file_name, usecols=['cast'], skip_blank_lines=True)
    df.fillna('Not Available', inplace=True) #replaces non-values to string
    df_no_duplicates = df.drop_duplicates() #removes duplicates
    df_to_list = df_no_duplicates.values.tolist() #converts the elements to a nested list, but the entire cell of actors is one string
    #splits the list by comma, converts it to one dimension, and removes duplicates and whitespace : giving each actor their own index in the list of strings
    actor_list_flattened = flatten(df_to_list)
    starting_list = []
    for item in actor_list_flattened:
        split = item.split(",")
        starting_list.append(split)
    flat_list = flatten(starting_list)
    final_list = []
    #removes whitespace in strings and removes duplicates by converting it to a dict and back
    for item in flat_list:
        final_list.append(item.strip())
    no_duplicates_list = list(dict.fromkeys(final_list))
    return no_duplicates_list

#retrieves a list of shows by either the show name or actors who are in the show
#type is name/actor indicating search method, and by_method is the string holding the show or actor name
#Runtime: O(n)
def get_show_by_search(search_type, name):
    data_dict = get_complete_csv_data(complete_csv_data) #converts the data frame to a dict
    shows_list = {}
    #iterates through all fo the data to form and return a nested dict with all of the show information
    if search_type == "name":
        for show in data_dict:
            if name in show["title"]:
                shows_list[show["show_id"]] = show
    elif search_type == "actor":
        for show in data_dict:
            if name in show["cast"]:
                shows_list[show["show_id"]] = show
    return shows_list

#takes an input of a nested dict full of shows with all the show info, and unpacks it one by one for the user to see
#Runtime: O(n)
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
        time.sleep(1)

#Runs the first time to get genres or return shows, could probably be combined with function get_results_second
#Runtime: O(n)
def get_genres_by_option(options):
    return_list = {}
    return_genres = []
    #reads the data, could be memoized
    data_dict = get_complete_csv_data(complete_csv_data)
    #exception for no rating preference input
    if options[2] == "":
        for show in data_dict:
            if show["type"] == options[0]:
                if options[1] in str(show["release_year"]):
                    return_list[show["show_id"]] = show
                    return_genres.append(show["listed_in"])
    else:
        for show in data_dict:
            if show["type"] == options[0]:
                if options[1] in str(show["release_year"]):
                    if show["rating"] == options[2]:
                        return_list[show["show_id"]] = show
                        return_genres.append(show["listed_in"])
    #if there are more than five shows, send back genres. If not, send shows
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
    #handle no results
    if len(return_list) == 0:
        return "0"
    return return_list 

#Runs the second time to narrow down based on genres, could possibly be combined.
#Runtime: O(n)
def get_shows_by_genre(options):
    return_list = {} #first for reading
    return_list_2 = {} #used to create results of the first list since dicts are immutable
    #Gets file data
    data_dict = get_complete_csv_data(complete_csv_data)
    #gets all of the shows that match the previous options, probably could be memoized
    #handles no rating input option
    if options[2] == "":
        for show in data_dict:
            if show["type"] == options[0]:
                if options[1] in str(show["release_year"]):
                    return_list[show["show_id"]] = show
    else:
        for show in data_dict:
            if show["type"] == options[0]:
                if options[1] in str(show["release_year"]):
                    if show["rating"] == options[2]:
                        return_list[show["show_id"]] = show     
    if len(options[3]) == 1:
        for key, show in return_list.items():
                if options[3][0] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
    elif len(options[3]) == 2:
        for key, show in return_list.items():
            if options[3][0] in show["listed_in"] and options[3][1] in show["listed_in"]:
                return_list_2[show["show_id"]] = show
                
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][0] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
                    
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][1] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
    else:
    
        #checks based on genres, it starts with shows that match the most recommendations in the input order
        for key, show in return_list.items():
            if options[3][0] in show["listed_in"] and options[3][1] in show["listed_in"] and options[3][2] in show["listed_in"]:
                return_list_2[show["show_id"]] = show
        
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][0] in show["listed_in"] and options[3][1] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
                    
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][1] in show["listed_in"] and options[3][2] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
                    
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][1] in show["listed_in"] and options[3][2] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
                    
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][0] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
                    
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][1] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show
        
        if len(return_list_2) < 4:
            for key, show in return_list.items():
                if options[3][2] in show["listed_in"]:
                    return_list_2[show["show_id"]] = show

    #If there are more than five results, it will only take the top 5
    if len(return_list_2) > 5:
        while len(return_list_2) > 5:
            return_list_2.popitem()
    return return_list_2