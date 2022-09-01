from slugify import slugify

from .extensions import db


class Page(db.Model):
    __tablename__ = "pages"

    id = db.Column(db.Integer, primary_key=True)
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
