"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template, jsonify

# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake
from forms import AddCupcakeForm

app = Flask(__name__)


app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# toolbar = DebugToolbarExtension(app)

@app.get("/")
def show_home_page():
    """ Show home page with list of cupcakes and form for adding more. """

    form = AddCupcakeForm()

    if form.validate_on_submit():
        # what does this need to be, since we're using axios?
        return
    else:
        return render_template("index.html", form=form)

@app.get("/api/cupcakes")
def list_cupcakes():
    """Returns JSON for all cupcakes currently in the database."""
    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """Returns JSON for the requested cupcake."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """Adds a new cupcake; returns JSON of newly-created cupcake."""

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json.get("image") or None

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """Updates a specified cupcake; returns JSON of updated cupcake."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get("flavor", cupcake.flavor)
    cupcake.size = request.json.get("size", cupcake.size)
    cupcake.rating = request.json.get("rating", cupcake.rating)
    cupcake.image = request.json.get("image",cupcake.image)

    db.session.add(cupcake)
    db.session.commit()

    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """Deletes a specified cupcake; returns JSON with ID of deleted cupcake."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted=cupcake_id)