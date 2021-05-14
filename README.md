## Projects marketplace

I wrote the code on Python, and I chose Flask framework because is minimalistic, flexible and suitable for the scope of this backend app. Also I used Mashmallow to make the schemas of the classes, deserialize and serialize json objects from and to requests.

Regarding to the code I tried to organize it to be maintainable and readable.

Inside ./marketplace/model are the two models I've created for this app, offers and projects. Inside them are all the attributes and methods needed to meet requirements.

Inside ./marketplace/tests are the two tests I've created and I left commented two more that would be useful to test almost all the functionalities.

Inside the root folder I created to two files: offers_client.py and projects_client.py that I was using to test the application and populate the in memory list of project.

Each file has the related comments explaining what I've done.

## How to run the project

Requirements:

- Python
- pipenv

Inside root folder run the following commands:

```
pipenv shell
pipenv install -r requirements.txt
./start_app.sh
```

The app will be listening on port 5000.

Tests can be run in the virtual environment with

```
pytest
```

## Extra comments

About the bids algorithm, in the way I did it, I only need to store the best offer which is defined each time a new offers is created to the project. Further developments can include storing them in a list ordered by price in case some user cancel the current best offer, the previous one get the assigned state.
