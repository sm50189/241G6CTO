from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class User(Base):
	__tablename__ = 'Users'
	id = Column(Integer, primary_key=True)
	first_name = Column(Text)
	last_name = Column(Text)
	password = Column(Integer)
	stu_id = Column(Integer)
	
	def change_password(self, new_password):
		self.password = password