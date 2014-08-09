from steps.trash_existing_tables import trash_existing_tables
from steps.create_tables import create_tables
from steps.populate_tables import populate_tables
from steps.remove_duplicate_players import remove_duplicate_players

if __name__ == '__main__':
    trash_existing_tables()
    create_tables()
    populate_tables()
    remove_duplicate_players()
