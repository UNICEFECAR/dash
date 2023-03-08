from .models import Page, DataExplorer, Project
from sqlalchemy import and_, func
from .extensions import db


class db_utils:
    TYPE_UNKNOWN = -1
    TYPE_DATAEXPLORER = 0
    TYPE_DASHBOARD = 1

    def get_page_type(self, prj_slug, page_slug):

        # look for the proj and page slugs in the Dashboard table
        p = (
            Page.query.join(Page.project)
            .filter(and_(Project.slug == prj_slug, Page.slug == page_slug))
            .first()
        )
        if p is not None:
            return db_utils.TYPE_DASHBOARD

        p = (
            DataExplorer.query.join(DataExplorer.project)
            .filter(and_(Project.slug == prj_slug, DataExplorer.slug == page_slug))
            .first()
        )
        if p is not None:
            return db_utils.TYPE_DATAEXPLORER

        return db_utils.TYPE_UNKNOWN
    
    #check if the slug exists in the Pages
    def slug_exists_in_page_prj(
        self,
        prj_slug,
        page_slug,
    ):

        page_slug_count = (
            db.session.query(func.count(Page.id))
            .join(Project)
            .filter(and_(Project.slug == prj_slug, Page.slug == page_slug))
            .scalar()
        )
        if page_slug_count > 0:
            return True
        return False

    #check if the slug exists in the Data explorers
    def slug_exists_in_dataexplorer_prj(
        self,
        prj_slug,
        de_slug,
    ):

        de_slug_count = (
            db.session.query(func.count(DataExplorer.id))
            .join(Project)
            .filter(and_(Project.slug == prj_slug, DataExplorer.slug == de_slug))
            .scalar()
        )
        if de_slug_count > 0:
            return True
        return False


