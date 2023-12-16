import csv
import pandas as pd

#Takes a nested array and turns it into a one-dimensional array
def flatten(list):
    result = []
    for item in list:
        if hasattr(item, "__iter__") and not isinstance(item, str):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

#Not currently used, should be considered for deletion
def get_search_data():
    shows_and_actors = {}
    with open("netflix_titles.csv") as imported_data:
        csv_reader = csv.DictReader(imported_data)
        for title in csv_reader:
            shows_and_actors[title["title"]] = title["cast"]
        return shows_and_actors

#returns an array of all actors in the csv file  
def get_actors():
    #read the csv file with pandas
    df = pd.read_csv("netflix_titles.csv", usecols=['cast'], skip_blank_lines=True)
    df_no_blanks = df.dropna()
    df_no_duplicates = df_no_blanks.drop_duplicates()
    actor_pre_list = df_no_duplicates.values.tolist()
    #splits the list by comma, converts it to one dimension, and removes duplicates and whitespace
    actor_list_flattened = flatten(actor_pre_list)
    actor_list = []
    for actor in actor_list_flattened:
        split_actors = actor.split(",")
        actor_list.append(split_actors)
    flat_actor_list = flatten(actor_list)
    final_actor_list = []
    for actor in flat_actor_list:
        final_actor_list.append(actor.strip())
    no_duplicates_list = list(dict.fromkeys(final_actor_list))
    
    return no_duplicates_list

def get_show_list():
    #read the csv file with pandas
    df = pd.read_csv("netflix_titles.csv", usecols=['title'], skip_blank_lines=True)
    df_no_blanks = df.dropna()
    df_no_duplicates = df_no_blanks.drop_duplicates()
    actor_pre_list = df_no_duplicates.values.tolist()
    #splits the list by comma, converts it to one dimension, and removes duplicates and whitespace
    actor_list_flattened = flatten(actor_pre_list)
    actor_list = []
    for actor in actor_list_flattened:
        split_actors = actor.split(",")
        actor_list.append(split_actors)
    flat_actor_list = flatten(actor_list)
    final_actor_list = []
    for actor in flat_actor_list:
        final_actor_list.append(actor.strip())
    no_duplicates_list = list(dict.fromkeys(final_actor_list))
    
    return no_duplicates_list

#returns a dictionary of shows associated with the actor passed in as the argument
def get_show_by_actor(actor):
    data = pd.read_csv('netflix_titles.csv', skip_blank_lines=True)
    data_no_blank_values = data.dropna()
    data_dict = data_no_blank_values.to_dict(orient='records')
    shows_by_actor = {}
    for show in data_dict:
        if actor in show["cast"]:
            shows_by_actor[show["show_id"]] = show
    return shows_by_actor

def get_show_by_show(i_show):
    data = pd.read_csv('netflix_titles.csv', skip_blank_lines=True)
    data_no_blank_values = data.dropna()
    data_dict = data_no_blank_values.to_dict(orient='records')
    shows_by_actor = {}
    for show in data_dict:
        if i_show in show["title"]:
            shows_by_actor[show["show_id"]] = show
    return shows_by_actor
    

