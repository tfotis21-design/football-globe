
# Football Globe

This is a web app where the user can interact with a 3d earth globe, zoom into countries & regions and see valuable information about the local football team.
Administrator is able to football teams to appear in the globe via the administrator panel.




## Tech Stack

**Client:** React

**Server:** Python (3.12.2), Django


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`





## Run Locally

Clone the project

```bash
  git clone git@github.com:tfotis21-design/football-globe.git
```

Go to the project directory

```bash
  cd football-globe
```

### Run backend

Create python virtual environment (Linux)

```bash
  python -m venv venv
  source venv/bin/activate
```

Create python virtual environment (Windows)

```bash
  python -m venv venv
  venv\Scripts\activate.bat
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run development server

```bash
  python manage.py runserver
```

Run db migration (to be done after alteration to models)

```bash
  python manage.py migrate
```

### Run frontend

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Roadmap

- Additional browser support

- Add more integrations

