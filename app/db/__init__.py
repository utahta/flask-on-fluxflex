from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import scoped_session
from app.settings import DB_CONFIG

db_engine = create_engine(DB_CONFIG)
db_session = scoped_session(sessionmaker(bind=db_engine))

def session_remove():
    db_session.remove()
    