from backend.database.database import init_db
from backend.database.seed import data_insertion

def initialize_db():
    init_db()
    data_insertion()