import csv
import pandas as pd

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, str):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def get_search_data():
    shows_and_authors = {}
    with open("netflix_titles.csv") as imported_data:
        csv_reader = csv.DictReader(imported_data)
        for title in csv_reader:
            shows_and_authors[title["title"]] = title["cast"]
        return shows_and_authors#
    
def get_authors():
    df = pd.read_csv("netflix_titles.csv", usecols=['cast'], skip_blank_lines=True)
    df_modified = df.dropna()
    df_modified2 = df_modified.drop_duplicates()
    author_pre_list = df_modified2.values.tolist()
    author_list = flatten(author_pre_list)
    actor_list = []
    for actor in author_list:
        split_actors = actor.split(",")
        actor_list.append(split_actors)

    final_actor_list = flatten(actor_list)
    new_final = []
    for actor in final_actor_list:
        new_final.append(actor.strip())
    no_dups = list(dict.fromkeys(new_final))
    
    return no_dups

def get_show_by_actor(actor):
    data = pd.read_csv('netflix_titles.csv', skip_blank_lines=True)
    data_m = data.dropna()
    data_dict = data_m.to_dict(orient='records')
    shows_by_actor = {}
    for show in data_dict:
        if actor in show["cast"]:
            shows_by_actor[show["show_id"]] = show
    return shows_by_actor
    

