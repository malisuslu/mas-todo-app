<!-- Please update value in the {}  -->

<h1 align="center">ToDo App with Django</h1>


<div align="center">
  <h3>
    <a href="https://mas-todo-app.herokuapp.com/">
      Demo
    </a>
     | 
    <a href="https://github.com/malisuslu/mas-todo-app">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
  - [Built With](#built-with)
- [How To Use](#how-to-use)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

![screenshot](todo.PNG)

### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- HTML
- CSS
- JS
- Django

## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://git-scm.com) 
```bash
# Clone this repository
$ git clone git@github.com:malisuslu/mas-todo-app.git

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt
    
# open the file "../mas-todo-app/main/settings.py" and change the "SITE_ID" value from "2" to "1"
    
# Create ".env" file in the main directory "../mas-todo-app/"
# Add "SECRET_KEY" in .env file
# In order to use Google Authentication service you must also add some valid "GOOGLE_CLIENT_ID" and "GOOGLE_CLIENT_SECRET"

# Run the app
    $ python manage.py runserver
```

## Acknowledgements
- Information for your projects

## Contact

- GitHub [@malisuslu](https://github.com/malisuslu)
- Linkedin [@malisuslu](https://www.linkedin.com/in/muhammed-ali-s%C3%BCsl%C3%BC/)
