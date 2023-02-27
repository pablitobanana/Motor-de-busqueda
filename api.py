from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.connection import serching
import json
app = Flask(__name__)
CORS(app)

@app.route("/",methods=["POST"])
def index():
    results = serching(request.json["request"])
    return {"data":results}
