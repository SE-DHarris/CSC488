
# Import Flask library
from flask import Flask

flask_app = Flask(__name__)

def get_data():
    return [ {'id': 0, 'year': 1990, 'degrees': 5818},{'id': 1, 'year': 1991, 'degrees': 5725}, {'id': 2, 'year': 1992, 'degrees': 6005}, {'id': 3, 'year': 1993, 'degrees': 6123}, {'id': 4, 'year': 1994, 'degrees': 6096}]

@app.route('/degrees',methods=['GET'])
def main():
    str(get_data())



if(__name__ == "__main__"):
    # Launch development server
    flask_app.run(debug=True,host='127.0.0.1')

