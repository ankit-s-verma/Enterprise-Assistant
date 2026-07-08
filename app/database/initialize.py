from app.database.database import init_db
from app.database.seed import data_insertion

def initialize_db():
    init_db()
    data_insertion()