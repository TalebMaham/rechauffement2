from flask import Flask, jsonify 
from logic import add_numbers, multiply_numbers, is_even 
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
    return jsonify({"message": "Welcome to the Flask app!"}) 
 
def add(a, b): 
    return jsonify({"result": add_numbers(a, b)}) 
 
def multiply(a, b): 
    return jsonify({"result": multiply_numbers(a, b)}) 
 
