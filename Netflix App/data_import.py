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
    
def get_actors():
    df = pd.read_csv("netflix_titles.csv", usecols=['cast'], skip_blank_lines=True)
    df_modified = df.dropna()
    df_modified2 = df_modified.drop_duplicates()
    actor_pre_list = df_modified2.values.tolist()
    actor_list = flatten(actor_pre_list)
    actor_list_2 = []
    for actor in actor_list:
        split_actors = actor.split(",")
        actor_list_2.append(split_actors)

    final_actor_list = flatten(actor_list_2)
    new_final = []
    for actor in final_actor_list:
        new_final.append(actor.strip())
    no_dups = list(dict.fromkeys(new_final))
    
    return no_dups

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
    

