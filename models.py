from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://tinyurl.com/demo-cupcake"

db = SQLAlchemy()

"""Models for Cupcake app."""

def connect_db(app):
    """Connects this database to provided flask app."""

    app.app_context().push()
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """A cupcake."""

    __tablename__ ="cupcakes"

    id = db.Column(
        db.Integer,
        primary_key = True,
        autoincrement = True
    )
    flavor = db.Column(
        db.Text,
        nullable=False
    )
    size = db.Column(
        db.Text,
        nullable=False
    )
    rating = db.Column(
        db.Integer,
        nullable=False
    )
    image = db.Column(
        db.Text,
        default=DEFAULT_IMAGE
    )

    def serialize(self):
        """Serialize to dictionary."""

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image,
        }