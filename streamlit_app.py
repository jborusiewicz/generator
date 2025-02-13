import random
import streamlit as st

#lists
hair_colors = ["dark", "light", "medium", "bright"]
eye_colors = ["black", "brown", "hazel", "green", "blue", "other"]
height_variants = ["very short(2-4ft)", "short(4-4.5ft)", "tall(5.5-6.5ft)",
                   "very tall(6.5+ft)"]
gender_pref = ["only men", "men", "other", "women", "only women", "all"]
race_pref = ["human", "elf (high)", "elf (not high)", "tiefling", "dragonborn"
        "dwarf", "gnome", "halfling", "tabaxi", "half-elf", "half-orc",
        "genasi", "bugbear", "goliath", "aasimir", "gith", "yuan ti",
        "kenku", "triton", "firebolg"]

#code
def choose_attraction(target):
    res = random.randrange(1, len(target))
    res = target[res]
    return res
hair = choose_attraction(hair_colors)
eye = choose_attraction(eye_colors)
height = choose_attraction(height_variants)
gender = choose_attraction(gender_pref)
race = choose_attraction(race_pref)


def print_attraction(type, variable):
    creatureName=input("What is the name of the creature?")
    type = str(type)
    print(creatureName + "'s preferred " + type + " is " + variable + ".")

print_attraction("hair color", hair)
print_attraction("eye color", eye)
print_attraction("height", height)
print_attraction("gender", gender)
print_attraction("race", race)

st.write("attraction generator")
