import json
import os.path as op
import pathlib
import os

from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.view import func
import flask_login
from jinja2.utils import markupsafe
from .extensions import admin
from .models import Page, DataExplorer, User
from sqlalchemy.sql import func
from .db_utils import db_utils
from wtforms.validators import ValidationError


def is_admin():
    if flask_login.current_user.is_authenticated:
        if flask_login.current_user.is_admin:
            return True
    return False


def json_formatter(view, context, model, name):
    value = getattr(model, name)
    json_value = json.dumps(value, ensure_ascii=False, indent=2)
    return markupsafe.Markup("<pre>{}</pre>".format(json_value))


class ProjectView(ModelView):
    column_list = ("name", "slug", "description", "created_at", "updated_at")
    column_searchable_list = ("name", "slug", "description")
    column_filters = ("name", "slug", "description")
    form_excluded_columns = ("created_at", "updated_at", "pages")
    form_readonly_columns = ("slug",)

    def is_accessible(self):
        return is_admin()


class PageView(ModelView):
    column_display_all_relations = True
    # column_formatters = {
    #     "content": json_formatter,
    # }
    column_list = (
        "project",
        "title",
        "slug",
        # "content",
        "geography",
        "created_at",
        "updated_at",
    )

    form_widget_args = {
        "created_at": {"disabled": True},
        "updated_at": {"disabled": True},
    }

    items = []
    upload_files_path = (
        f"{pathlib.Path(__file__).parent.parent.absolute()}/dash_service/static"
    )
    up = upload_files_path

    # uploaded_files_path="/dash_service/static"
    for f in os.listdir(upload_files_path):
        if op.isfile(op.join(upload_files_path, f)):
            items.append((f, f))

    form_choices = {"geography": items}

    def is_accessible(self):
        return flask_login.current_user.is_authenticated

    def get_query(self):
        if is_admin():
            return self.session.query(self.model)
        return self.session.query(self.model).filter(
            Page.project_id == flask_login.current_user.project_id
        )

    def get_count_query(self):
        if is_admin():
            return self.session.query(func.count("*"))
        return self.session.query(func.count("*")).filter(
            Page.project_id == flask_login.current_user.project_id
        )

    def on_model_change(self, form, model, is_created):
        # We're updating a Page, check if the slug has already been used in the project for a Data explorer
        exists = db_utils().slug_exists_in_dataexplorer_prj(
            form.project.data.slug, form.slug.data
        )
        if exists:
            raise ValidationError(
                f'Slug "{form.slug.data}" is already used, please select a new one'
            )


class DataExplorerView(ModelView):
    column_display_all_relations = True
    column_list = (
        "project",
        "title",
        "slug",
        "created_at",
        "updated_at",
    )

    form_widget_args = {
        "created_at": {"disabled": True},
        "updated_at": {"disabled": True},
    }

    def is_accessible(self):
        return flask_login.current_user.is_authenticated

    def get_query(self):
        if is_admin():
            return self.session.query(self.model)
        return self.session.query(self.model).filter(
            DataExplorer.project_id == flask_login.current_user.project_id
        )

    def get_count_query(self):
        if is_admin():
            return self.session.query(func.count("*"))
        return self.session.query(func.count("*")).filter(
            DataExplorer.project_id == flask_login.current_user.project_id
        )

    def on_model_change(self, form, model, is_created):
        # We're updating a DE, check if the slug has already been used in the project for a Page
        exists = db_utils().slug_exists_in_page_prj(
            form.project.data.slug, form.slug.data
        )
        if exists:
            raise ValidationError(
                f'Slug "{form.slug.data}" is already used, please select a new one'
            )


class UserView(ModelView):
    column_display_all_relations = True
    column_list = (
        "id",
        "name",
        "email",
        # "password",
        "project",
        "is_admin",
        "is_user_active",
        "created_at",
        "updated_at",
    )

    form_widget_args = {
        "created_at": {"disabled": True},
        "updated_at": {"disabled": True},
    }

    def on_model_change(self, form, instance, is_created):
        if is_created:
            instance.set_password(form.password.data)
        else:
            old_pwd = form.password.object_data
            if old_pwd != instance.password:
                instance.set_password(form.password.data)

    def is_accessible(self):
        return is_admin()


class ExtFileAdmin(FileAdmin):
    def is_accessible(self):
        return is_admin()


# production storage will be an Azure blob storage
path = op.join(op.dirname(__file__), "static")

# admin.add_view(FileAdmin(path, "/static/", name="Static Files"))
admin.add_view(ExtFileAdmin(path, "/static/", name="Static Files"))
