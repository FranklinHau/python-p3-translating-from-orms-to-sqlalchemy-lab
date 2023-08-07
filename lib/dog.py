from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dog  # Ensure this import is correct

# SQLite Database setup
DATABASE_URL = 'sqlite:///dogs.db' 
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_table(base, engine):
    """Create the tables in the database using the provided declarative_base and engine."""
    base.metadata.create_all(engine)

def save(session, dog):
    """Save a new dog or update an existing one."""
    if not dog.name:
        raise AttributeError("Dog instance must have a 'name' attribute.")
    session.add(dog)
    session.commit()

def get_all(session):
    """Return all dogs."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Return dogs with a specific name."""
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    """Return a dog with a specific ID."""
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    """Return dogs with a specific name and breed."""
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    """Update the breed of a dog."""
    dog.breed = breed
    session.add(dog)
    session.commit()