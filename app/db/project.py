from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import String
from sqlalchemy.dialects.mysql import INTEGER as Integer

Base = declarative_base()
class ProjectTable(Base):
    __tablename__ = 'project'
    __table_args__ = {'mysql_engine': 'InnoDB',
                      'mysql_charset': 'utf8'}
    
    id = Column(Integer(unsigned=True), autoincrement=True, primary_key=True)
    name = Column(String(length=256), nullable=False)
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return "<id:%s name:%s>" % (self.id, self.name)

