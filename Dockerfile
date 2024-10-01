# Example Dockerfile
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages
RUN pip install --upgrade pip
#RUN pip install --no-cache-dir Flask==2.1.3 Werkzeug==2.1.2 SQLAlchemy=1.4.0 flask_sqlalchemy>=2.5 requests==2.27.1  # Specify compatible versions
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

CMD rm animals.db
CMD flask db init
CMD flask db migrate -m "Add picture_url column to AnimalPicture"
CMD flask db upgrade

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]

