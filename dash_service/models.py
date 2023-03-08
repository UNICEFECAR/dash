from slugify import slugify
from sqlalchemy_mixins import AllFeaturesMixin
from werkzeug.security import generate_password_hash, check_password_hash

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
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
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
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
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
    password = db.Column(db.String(255), nullable=False)
    project = db.relationship("Project")
    is_admin = db.Column(db.Boolean, default=False)
    is_user_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(
        db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(
        self,
        # project_id,
        name,
        email,
        password,
        is_admin,
        # is_user_active,
        # created_at,
        # updated_at,
        project_id=None,
        is_user_active=None,
        created_at=None,
        updated_at=None,
    ) -> None:
        self.project_id = project_id
        self.name = name
        self.email = email
        self.password = generate_password_hash(password,)
        self.is_admin = is_admin
        self.is_user_active = is_user_active
        self.created_at = created_at
        self.updated_at = updated_at

    # Used by Flask-login
    def is_active(self):
        return self.is_user_active

    def get_id(self):
        return str(self.id)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return f"<User {self.name}>"


    def set_password(self, password_plaintext:str):
        self.password = generate_password_hash(password_plaintext)

    def verify_password(self, password_plaintext:str):
        return check_password_hash(self.password, password_plaintext,)