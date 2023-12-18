# taken from finance.db

import csv
import datetime
import pytz
import requests
import subprocess
import urllib
import uuid
import json

from flask import redirect, render_template, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def book_lookup(title):
    """Look up entry for book."""

    try:
          # Open Library API
        url = "https://openlibrary.org/search.json"
        query = {
        "q": title,
        }

        response = requests.get(url, query)
        if response.status_code == 200:
            data = json.loads(response.text)
            book_data = data['docs']
            for book in book_data:
                base_url = "https://openlibrary.org"
                work_details = book['key']
                url = base_url + work_details + '.json'
                response = requests.get(url)
                if response.status_code == 200:
                    data = json.loads(response.text)
                    return {
                        "title": data['title'],
                        "cover-small": "https://covers.openlibrary.org/b/id/" + str(data['covers'][0]) + "-S.jpg",
                        "cover-medium": "https://covers.openlibrary.org/b/id/" + str(data['covers'][0]) + "-M.jpg",
                        "key": data['key']
                    }
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None