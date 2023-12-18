# taken from finance.db

# https://openlibrary.org/developers/api

# flask --app app.py --debug run
# fuser -k 5000/tcp

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from helpers import apology, login_required, book_lookup

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

db = SQL("sqlite:///reviews.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    """Show list of books"""
    return apology("TODO", 403)

@app.route("/lookup", methods=["GET", "POST"])
@login_required
def lookup():
    # Require that a user input a stock’s symbol, implemented as a text field whose name is symbol.
    # Submit the user’s input via POST to /quote.
    """Look up entry for book."""
    if request.method == "POST":
        title = request.form.get("book_title")
        bookTitle = book_lookup(title)
        
        return render_template("lookup.html", book=bookTitle)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("lookup.html")
  

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # throw error if the username field is blank
        if not request.form.get("username"):
            return apology("must provide username", 400)
        # or if the name already exists in the db
        elif len(rows) == 1:
            return apology("username is taken", 400)
        # throw error if password field is blank
        elif not request.form.get("password"):
            return apology("must provide password", 400)
        # or if password fields do not match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 400)

        # if the username is valid, accept it
        username = request.form.get("username")
        # if password is valid, hash it
        password = generate_password_hash(request.form.get("password"))

        # submit username and *hashed password* into database
        db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)", username, password
        )

        return redirect("/")

    else:
        return render_template("register.html")