from generate_sets_of_numbers import generate_sets_of_numbers
from show_landing_page import show_landing_page

# RUNNING BEFORE START OF AN APPLICATION
with open('./store/stored_sets.txt', 'r') as sets_data_file_handler:
    if len(sets_data_file_handler.readlines()) < 1:
        generate_sets_of_numbers(3, 15)

def runApp():
    show_landing_page()

runApp()