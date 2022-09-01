import json
import os.path as op

from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.contrib.sqla import ModelView
from jinja2.utils import markupsafe
from .extensions import admin


def json_formatter(view, context, model, name):
    value = getattr(model, name)
    json_value = json.dumps(value, ensure_ascii=False, indent=2)
    return markupsafe.Markup("<pre>{}</pre>".format(json_value))


class PageView(ModelView):
    column_formatters = {
        "content": json_formatter,
    }


# production storage will be an Azure blob storage
path = op.join(op.dirname(__file__), "static")
admin.add_view(FileAdmin(path, "/static/", name="Static Files"))
