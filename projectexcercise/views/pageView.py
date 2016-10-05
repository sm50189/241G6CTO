# from sqlalchemy import *
# from sqlalchemy.orm import *
# from sqlalchemy.ext.declarative import declarative_base

def page_view(request):
	def return_project(session, project_id):
		goal = session.query(web_db).filter_by(id=project_id).one()
		return goal.web_url
		