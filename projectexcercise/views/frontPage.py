# from sqlalchemy import *
# from sqlalchemy.orm import *
# from sqlalchemy.ext.declarative import declarative_base

def front_page(request):
	def return_page(session, page_number):
		Page_url = []
		for i in range(1 + ((5 * page_number) - 5), (5 * page_number) + 1):
			get_page = session.query(web_db).filter_by(id=i).one()
			Page_url.append(get_page.peb_url)
		return Page_url