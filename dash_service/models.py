from slugify import slugify
from sqlalchemy_mixins import AllFeaturesMixin

from .extensions import db


class Project(db.Model, AllFeaturesMixin):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    slug = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    pages = db.relationship("Page")

    def __init__(self, name, description):
        self.name = name
        self.slug = slugify(name)
        self.description = description

    def __repr__(self):
        return f"<Project {self.name}>"

    def __str__(self):
        return self.name


class Page(db.Model, AllFeaturesMixin):
    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    project = db.relationship("Project")
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.JSON, nullable=False)
    geography = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    def __repr__(self):
        return "<Page %r>" % self.title

    @staticmethod
    def slugify(target, new_value, old_value, initiator):
        if new_value and (not target.slug or new_value != old_value):
            new_slug = slugify(
                new_value,
                lowercase=True,
                max_length=20,
                word_boundary=True,
                save_order=True,
            )
            target.slug = new_slug


class DataExplorer(db.Model, AllFeaturesMixin):
    __tablename__ = "dataexplorers"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    project = db.relationship("Project")
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    def __repr__(self):
        return "<Data explorer %r>" % self.title


class User(db.Model, AllFeaturesMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    project = db.relationship("Project")
    is_admin = db.Column(db.Boolean, default=False)
    is_user_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    #Used by Flask-login
    def is_active(self):
        print("Is active called")
        print(self)
        return self.is_user_active

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return "<User %r>" % self.name
