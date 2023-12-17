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

def get_data(type):
    #read the csv file with pandas
    if type == "name":
        df = pd.read_csv("netflix_titles.csv", usecols=['title'], skip_blank_lines=True)
    elif type == "actor":
        df = pd.read_csv("netflix_titles.csv", usecols=['cast'], skip_blank_lines=True)
    df.fillna('Not Available', inplace=True)
    df_no_duplicates = df.drop_duplicates()
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

def get_show(type, by_method):
    data = pd.read_csv('netflix_titles.csv', skip_blank_lines=True)
    data.fillna('Not Available', inplace=True)
    data_dict = data.to_dict(orient='records')
    shows_list = {}
    if type == "name":
        for show in data_dict:
            if by_method in show["title"]:
                shows_list[show["show_id"]] = show
    elif type == "actor":
        for show in data_dict:
            if by_method in show["cast"]:
                shows_list[show["show_id"]] = show
    return shows_list