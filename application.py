import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session,url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///cnmc.db")


@app.route("/")
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/slide", methods=["GET", "POST"])
def slide():
    if request.method == "GET":
        allinfos = db.execute("select distinct date from slide")
        return render_template("slide.html",allinfos=allinfos)
    if request.method == "POST":
        allinfos = db.execute("select distinct date from slide")
        infos = db.execute("select * from slide where date=:date",date=request.values['slide'])
        return render_template("slide.html",infos=infos,allinfos=allinfos)

@app.route("/others")
def others():
    if request.method == "GET":
        return render_template("others.html")
        
@app.route("/back")
def back():
    if request.method == "GET":
        return render_template("back.html")