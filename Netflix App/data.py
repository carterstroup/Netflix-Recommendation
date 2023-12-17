#Imports
import pandas as pd

#Takes a nested array and turns it into a one-dimensional array
#Runtime: O(n)
def flatten(list):
    result = []
    for item in list:
        if hasattr(item, "__iter__") and not isinstance(item, str):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

#retrieves a list of actors or show names from the csv file and stores them in a list
#cleans the data in the process by skipping blanks, changing non-values to 'Not Available' and removes duplicates
#O(n)
def get_data(type):
    #gets certain data based on need to reduce runtime
    if type == "name":
        df = pd.read_csv("netflix_titles.csv", usecols=['title'], skip_blank_lines=True)
    elif type == "actor":
        df = pd.read_csv("netflix_titles.csv", usecols=['cast'], skip_blank_lines=True)
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
def get_show(type, by_method):
    data = pd.read_csv('netflix_titles.csv', skip_blank_lines=True) #gets data
    data.fillna('Not Available', inplace=True) #changes non-values to string Not Available
    data_dict = data.to_dict(orient='records') #converts the data frame to a dict
    shows_list = {}
    #iterates through all fo the data to form and return a nested dict with all of the show information
    if type == "name":
        for show in data_dict:
            if by_method in show["title"]:
                shows_list[show["show_id"]] = show
    elif type == "actor":
        for show in data_dict:
            if by_method in show["cast"]:
                shows_list[show["show_id"]] = show
    return shows_list