from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Project(Base):
	__tablename__ = 'Project'
	id = Column(Integer, primary_key=True)
	title = Column(Text)
	description = Column(Text)
	status = Column(Text)
	owner_id = Column(Integer)
	
	def change_status(self, st):
		self.status = st
		
	def change_describ(self, des)
		self.description = des