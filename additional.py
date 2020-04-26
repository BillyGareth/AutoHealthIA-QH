from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import jsonify

AutoHealthIA = Flask(__name__)
@AutoHealthIA.route('/', methods=['POST','GET'])
def signup():
    return render_template('AutoHealthIA.html')

if __name__ == '__main__' :
    AutoHealthIA.run(debug=True)