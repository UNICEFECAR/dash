from flask_admin.contrib.sqla import ModelView

from .extensions import admin, db
from .models import Page


admin.add_view(ModelView(Page, db.session))
