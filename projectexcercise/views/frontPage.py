from pyramid.view import view_config
from sqlalchemy.orm.exc import NoResultFound
from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )
from ..models.Project import Project

@view_config(route_name = 'frontPage')
def go_to_home_page(request):
	next_location = request.route_url('feedpage', page_number= '1')
	return HTTPFound(location=next_location)

@view_config(renderer = '../templates/frontpage.pt', route_name= 'feedpage')
def front_page(request):
	session = request.db_session
	page_number = request.matchdict['page_number']

	def return_page(session, page_number):
		Page_url = []
		for i in range(1 + ((5 * page_number) - 5), (5 * page_number) + 1):
			try:
				get_page = session.query(Project).filter_by(id=i).one()
				Page_url.append(get_page)
			except NoResultFound:
				break
		return Page_url

	Page = return_page(session , int(page_number))
	print '\n\n\n\n\n\n Page **********************************************************************************88\n\n\n\n\n'
	return dict(Pages= Page) 
