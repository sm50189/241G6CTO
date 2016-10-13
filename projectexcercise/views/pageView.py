from pyramid.view import view_config
from ..models.Project import Project

@view_config(renderer = '../templates/pageView.pt', route_name= 'pageView')
def page_view(request):
	session = request.db_session
	project_id = request.matchdict['id_project']
	def return_project(session, project_id):
		goal = session.query(Project).filter_by(id=project_id).one()
		return goal
	Page = return_project(session , project_id)
	return {'Page':Page}
