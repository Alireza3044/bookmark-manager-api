# About the project

This project is a bookmark management api featuring user authentication with bookmarks and categories built with Django and it's REST framework (DRF).

# Getting Started

1. Clone the project to your machine by following command:

    `git clone https://github.com/Alireza3044/bookmark-manager-api.git`

2. In the project's root directory, run the following command to install the required packages:

    `pip install -r requirements.py`

3. Create a `.env` file with variables `DEBUG` and `SECRET_KEY`. If you want to deploy the project, set the `DEBUG` to `False`, otherwise to `True`. For `SECRET_KEY` you can generate one by first entering to the Django shell via `python manage.py shell` and then importing  and running the function `get_random_secret_key` from `django.core.management.utils`.

4. Now you can run the dev server by `python manage.py runserver`.
