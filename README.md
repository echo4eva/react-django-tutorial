# react-django-tutorial

# Django and React Tutorial

class: Django, JS, Python, React, STEM Related
created on: July 6, 2022 2:44 PM

# Setup

### Make a venv

[https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

<aside>
💗 Use commands to install venv and make one

- `pip install virtualenv`
    - install virtualenv
- `python3 -m venv env`
    - create a virtualenv called env
- ``source env/bin/activate``
    - to activate the virtualenv
</aside>

### Install django and rest framework

- `pip install django djangorestframework`

### Create a django project

- `django-admin startproject music_controller`
    
    <aside>
    💗 **Inner music_controller**
    
    - The inner folder is basically the project folder, or settings.
    </aside>
    

### Create an app inside the project

- `django-admin startapp api`

<aside>
💗 **In settings.py**

- go to INSTALLED_APPS and add `api.apps.ApiConfig`
    - go into the api folder, then apps.py, then the ApiConfig class
    - reference the app into the project
- add `rest_framework`
    - another app that we need for our project
</aside>

### Create first view

- go to `views`
- to get a url to the views, create `url` file in api, copy paste from settings folder (inner music_controller)
    - website address paths are sent to project folder’s `url` then it will know where to go from there to the correct app
    - these urls will be specific for that app that we put the `[urls.py](http://urls.py)` in

<aside>
💗 in /api/urls

```python
from django.urls import path
from .views import main

urlpatterns = [
    path('', main)
]
```

- if we get a url with nothing, go to main function
    - `main` is a function within .views
    - and do whatever is in `view.main`
</aside>

### Running website

<aside>
💗 Before running the website (first time)

- `python ./manager.py makemirgrations`
- to update the database to store the current changes that we made to the app
- whenever we have a change to the models/database, run this.
- need to do this because first time running the app
- `python [manager.py](http://manager.py) runserver`
</aside>

- Now run the website using `python [manage.py](http://manage.py) runserver`

# Django REST Framework

<aside>
💗 What is a model?

- Creating a table == model
</aside>

<aside>
💗 Creating a model

```python
class Room(models.Model):
    code = models.Charfield(max_length=8, default='', unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    vote_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
```

- a class named `Room` that takes in a model
    - in the code, basically setting what attributes that Room should have

```python
def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))

        if Room.objects.filter(code=code).count() == 0:
            break

    return code
```

- Interacts with the data base
    - `Room.objects.filter(code=code)`
        - gives us a list of how many objects with that filter
    - `Room.objects.filter(code=code).count() == 0:`
        - if the list has a length of 0, then it’s a good code that we can use, since it’s not unique
- make sure to `python [manage.py](http://manage.py) makemigrations`
    - then to python [manage.py](http://manage.py) migrate
</aside>

### How do we see the Models in our database?

<aside>
💗 Make a [serializers.py](http://serializers.py) file!

- will translate models into json responses

```python
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause',
         'votes_to_skip', 'created_at')
```

- need to import above
- create a class for the model to serialize with that given argument
    - created a nested class that has the model name and fields of that model
</aside>

### So how do we actually see it?

<aside>
💗 Make it into a view in view.py!

```python
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# Where we are going to write all of our endpoints of the website
# Create your views here.

class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
```

- add these imports for the [serializer.py](http://serializer.py) and class Room within [models.py](http://models.py) and for rest_framework
- then simply create a class with the with name of model view
    - add query set to include all the rooms in the database
    - and serializer class

```python
# in urls.py of api

from .views import RoomView

urlpatterns = [
    path('home', RoomView.as_view()),
]
```

- import the view
    - and set the Roomview as a view

![Untitled](Django%20and%20React%20Tutorial%20d3aad62e644348d2a914cc28c135173a/Untitled.png)

- will see once post a new room
</aside>

### Note

<aside>
💗 Listing API View instead of creating

```python
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
```

![Untitled](Django%20and%20React%20Tutorial%20d3aad62e644348d2a914cc28c135173a/Untitled%201.png)

- will see this once RoomView is set to `ListAPIView` as argument instead of `CreateAPIView`
- WE WONT BE SEEING THIS FROM NOW ON, IT WILL JUST BE THE JSON DATA IN THE FUTURE WITH REACT!
</aside>

# React Integration Using Webpack and Babel

<aside>
💗 Create a new app

```python
django-admin startapp frontend
```

- make sure it’s within the original django project folder (outer folder)
- this will focus on the React side of the project
</aside>

<aside>
💗 Create 2 new folders

- templates
- static
    - will hold anythipng site will cache
    - within the static folder create:
        - frontend → will hold main javascript bundles
        - css → for css
- src
    - components → for react

</aside>

### Installing libraries

<aside>
💗 Run this command to get started

- `npm init -y` → create a node module, things we need for our front end project
- `npm i webpack webpack-cli` → will transpile all of our javascript into one single javascript file
- `npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev` → used to make website compatible with all types and transpile
- `npm i react react-dom --save-dev` → for react, duh
- `npm install @material-ui/core` → built in components so we dont have to style ourselves
    - ran into an error → [https://stackoverflow.com/questions/72596908/could-not-resolve-dependency-error-peer-react16-8-0-17-0-0-from-materia](https://stackoverflow.com/questions/72596908/could-not-resolve-dependency-error-peer-react16-8-0-17-0-0-from-materia)
    - solved this by going through the answer and reinstalling it again.
- `npm install @babel/plugin-proposal-class-properties` → can use async and await in javascript code
- `npm install react-router-dom` → allow us to reroute pages with react app
- `npm install @material-ui/icons` → to get icons from material-ui
</aside>

### Configuration Scripts

They run and handle our webpacks, bable, etc.

```python
babel.config.js: https://github.com/techwithtim/Music-...
package.json: https://github.com/techwithtim/Music-...\
webpack.config.json: https://github.com/techwithtim/Music-...
```

- [https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial 1 - 4/frontend/babel.config.json](https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial%201%20-%204/frontend/babel.config.json)
- [https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial 1 - 4/frontend/package.json](https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial%201%20-%204/frontend/package.json)
    - “dev” in scripts → we want to run webpack in dev mode and watch mode
        - recompile when we save and stuff like regular
    - “build”
- [https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial 1 - 4/frontend/webpack.config.js](https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial%201%20-%204/frontend/webpack.config.js)
    - gets entry
    - and outputs to the path
    - module excludes bundling module folder, and uses babel folder to load
    - minimizes optimization just minimizes and deletes all white spaces and info from file dont need
    - plugins, optimizes stuff

### React + Django

Use django render a template, react will takeover that template and fill it in. So we will use django render, but react will manage it.

<aside>
💗 index.html

- create folder within templates, then folder called front end within templates
    - within new folder, create `index.html`
    
    ```python
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Music Controller</title>
        {% load static %}
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link
          rel="stylesheet"
          href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
        />
        <link rel="stylesheet" type="text/css" href="{% static "css/index.css" %}"
        />
      </head>
      <body>
        <div id="main">
          <div id="app"></div>
        </div>
    
        <script src="{% static "frontend/main.js" %}"></script>
      </body>
    </html>
    ```
    
    - load static → basically load everything from static
    - styling above body
    - div with app → what react will take care of.
    - frontend/main.js → will be our main bundle
</aside>

<aside>
💗 Views in front end + Urls

- will render, then let react take care of it

```python
from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')
```

- will return the html to whatever is requesting it
</aside>

<aside>
💗 Making URL for front end

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('frontend.urls')),
]
```

- in settings folder, make URL, so if blank will head onto frontend urls.

```python
from django.urls import path
from .views import index

urlpatterns = [
    path('', index)
]
```

- in front end folder of URL, import index from views, so it will render stuff from the front end views
</aside>

### Making first React component

<aside>
💗 App.js within src components

```python
import React, { Component } from "react";
import { render } from "react-dom";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render () {
        return (
            <h1>Testing React Code</h1>
        )
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv)
```

- need to render component within div within `index.html`

```python
# in index.js
import App from ".components/App";
```

</aside>

<aside>
💗 Make the frontend an app in the settings.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    'rest_framework',
    'frontend.apps.FrontendConfig',
]
```

</aside>

### How it works

- App.js → index.html (app div) →
- Looks at index.js → see what its importing (App.js) → bundles whatever App renders → outputs to main.js

### How to run the webapp

- run the server `npm [manage.py](http://manage.py)` runserver (make sure just in project folder)
- `npm run dev` (make sure in frontend folder)
    - will have an error, but its just a warning and is okay
    - [https://stackoverflow.com/questions/66772358/webpack-warning-warning-in-defineplugin-conflicting-values-for-process-env-no](https://stackoverflow.com/questions/66772358/webpack-warning-warning-in-defineplugin-conflicting-values-for-process-env-no)
