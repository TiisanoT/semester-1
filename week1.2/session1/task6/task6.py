# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music = {
    "Drake": ["Views", "Take Care", "Scorpian"],
    "Kabza de small": ["KOA II Part1", "I am the king of amapiano"],
    "Black coffee": ["Subconciously", "Pieces of me "]
}




# Pretty-print the data structure
pprint(music)

# Display details of one album recorded by a specific artist

print(music["Drake"][0])
