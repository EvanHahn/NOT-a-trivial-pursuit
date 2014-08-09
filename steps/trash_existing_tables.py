import os

def trash_existing_tables():
    database_path = os.path.abspath('archive.db')
    if os.path.isfile(database_path):
        print 'Removing existing database...'
        os.remove(database_path)
        print 'Database removed.'
