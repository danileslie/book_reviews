# taken from finance.db

# https://openlibrary.org/developers/api

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)

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
    """Show portfolio of stocks"""
    # this section was very hard, i had to look it up: https://www.youtube.com/watch?v=l7wELOgKqLM

    # displays an HTML table summarizing, for the user currently logged in, which stocks the user owns, the numbers of shares owned,

    # Odds are you’ll want to execute multiple SELECTs. Depending on how you implement your table(s), you might find GROUP BY HAVING SUM and/or WHERE of interest.

    # the current price of each stock, and the total value of each holding (i.e., shares times price).
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
        user_id=session["user_id"],
    )

    # Also display the user’s current cash balance along with a grand total (i.e., stocks’ total value plus cash).
    available_cash = db.execute(
        "SELECT cash FROM users WHERE id = :user_id", user_id=session["user_id"]
    )[0]["cash"]
    total_cash = available_cash

    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["value"] = stock["price"] * stock["total_shares"]
        total_cash += stock["value"]

    return render_template(
        "index.html",
        stocks=stocks,
        available_cash=available_cash,
        total_cash=total_cash,
    )

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # # User reached route via POST (as by submitting a form via POST)
    # if request.method == "POST":
    #     # Ensure username was submitted
    #     if not request.form.get("username"):
    #         return apology("must provide username", 403)

    #     # Ensure password was submitted
    #     elif not request.form.get("password"):
    #         return apology("must provide password", 403)

    #     # Query database for username
    #     rows = db.execute(
    #         "SELECT * FROM users WHERE username = ?", request.form.get("username")
    #     )

    #     # Ensure username exists and password is correct
    #     if len(rows) != 1 or not check_password_hash(
    #         rows[0]["hash"], request.form.get("password")
    #     ):
    #         return apology("invalid username and/or password", 403)

    #     # Remember which user has logged in
    #     session["user_id"] = rows[0]["id"]

    #     # Redirect user to home page
    #     return redirect("/")

    # # User reached route via GET (as by clicking a link or via redirect)
    # else:
    return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")