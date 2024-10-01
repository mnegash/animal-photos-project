from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests

app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the model to store animal pictures
class AnimalPicture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_type = db.Column(db.String(50), nullable=False)
    picture_url = db.Column(db.String(200), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Function to fetch animal pictures (for simplicity, using placeholder API)
def fetch_pictures(animal, num_pics):
    pictures = []
    for i in range(num_pics):
        # Example: Replace with actual API call to fetch real images
        pictures.append(f"https://placekitten.com/400/300?image={i}")
    return pictures

# Route to save pictures based on animal type and number
@app.route('/save_pictures', methods=['POST'])
def save_pictures():
    data = request.form
    animal_type = data.get('animal_type')
    num_pictures = int(data.get('num_pictures'))

    pictures = fetch_pictures(animal_type, num_pictures)
    for pic_url in pictures:
        picture = AnimalPicture(animal_type=animal_type, picture_url=pic_url)
        db.session.add(picture)
    db.session.commit()

    return redirect(url_for('index'))

# Route to fetch the last picture of an animal
@app.route('/get_last_picture/<animal_type>')
def get_last_picture(animal_type):
    picture = AnimalPicture.query.filter_by(animal_type=animal_type).order_by(AnimalPicture.id.desc()).first()
    if picture:
        return jsonify({"animal_type": animal_type, "last_picture_url": picture.picture_url})
    return jsonify({"error": "No picture found for this animal type."})

# Home route to show the form and retrieve pictures
@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

