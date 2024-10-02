
# MyCamundaProject
quick fetch save and animal python project.

## Description
This application offers a REST API to save and retrieve pictures of animals. It uses Flask and SQLite for simplicity.

## How to Run

1. Clone the repository.
2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. To containerize the app, run:

    ```bash
    docker build -t animal_pictures_app .
    docker run -p 5000:5000 animal_pictures_app
    ```

6. The app will be running at `http://localhost:5000`.

## Tests

Run automated tests with `pytest`:

```bash
pytest tests/

