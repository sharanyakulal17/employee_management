from flask import Flask, render_template
import json 

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Employee Management Web Application"

@app.route("/employee")
def employee():
    with open("employees.json", "r") as file:
        employees = json.load(file)
        return render_template("employees.html", employees = employees)

@app.route("/employee/<int:employee_id>")
def employee_id(employee_id):
    return f"Employee ID: {employee_id}"

@app.route("/employee/<string:employee_name>")
def employee_name(employee_name):
    return f"Welcome {employee_name}"