import json
import os

FILE_PATH = "data/users/user_profile.json"


def load_profile():

    if not os.path.exists(FILE_PATH):

        default_profile = {
            "name": None,
            "age": None,
            "weight": None,
            "goal": None
        }

        with open(FILE_PATH, "w") as file:
            json.dump(default_profile, file, indent=4)

        return default_profile

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_profile(profile):

    with open(FILE_PATH, "w") as file:
        json.dump(profile, file, indent=4)


def save_name(name):

    profile = load_profile()
    profile["name"] = name
    save_profile(profile)


def save_weight(weight):

    profile = load_profile()
    profile["weight"] = weight
    save_profile(profile)


def save_goal(goal):

    profile = load_profile()
    profile["goal"] = goal
    save_profile(profile)


def get_name():

    profile = load_profile()
    return profile["name"]


def get_weight():

    profile = load_profile()
    return profile["weight"]


def get_goal():

    profile = load_profile()
    return profile["goal"]


def get_profile():

    return load_profile()