from .models import Page, DataExplorer, Project, Dashboard, MenuPage
from sqlalchemy import and_, func
from .extensions import db


class db_utils:
    TYPE_UNKNOWN = -1
    TYPE_DATAEXPLORER = 0
    TYPE_DASHBOARD = 1
    TYPE_MENU = 2

    def get_page_type(self, prj_slug, page_slug):
        dashboard = (
            Dashboard.query.with_entities(Dashboard.id)
            .join(Project)
            .filter(and_(Project.slug == prj_slug, Dashboard.slug == page_slug))
        ).first()

        if dashboard is not None:
            return db_utils.TYPE_DASHBOARD

        dataexplorer = (
            DataExplorer.query.with_entities(DataExplorer.id)
            .join(Project)
            .filter(and_(Project.slug == prj_slug, DataExplorer.slug==page_slug))
        ).first()

        if dataexplorer is not None:
            return db_utils.TYPE_DATAEXPLORER
        
        menupage = (
            MenuPage.query.with_entities(MenuPage.id)
            .join(Project)
            .filter(and_(Project.slug == prj_slug, MenuPage.slug==page_slug))
        ).first()
        if menupage is not None:
            return db_utils.TYPE_MENU
        
        return db_utils.TYPE_UNKNOWN
