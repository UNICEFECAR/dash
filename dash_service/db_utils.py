from .models import Page, DataExplorer, Project
from sqlalchemy import and_


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

    def page_slug_exists(self, prj_slug, page_slug):
        page_type = self.get_page_type(prj_slug, page_slug)
        if page_type == db_utils.TYPE_UNKNOWN:
            print("RET FALSE")
            return False
        return True
