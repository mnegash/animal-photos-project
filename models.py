from app import app, db

class AnimalPicture(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    animal_type = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<AnimalPicture {self.animal_type}, {self.url}>"

# Create the database schema
with app.app_context():
   db.create_all()
   app.run(debug=True)
