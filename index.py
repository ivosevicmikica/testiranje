from flask import Flask, flash, jsonify, render_template 

app = Flask(__name__)

@app.route('/<prikazi>/')
def hello_world(prikazi):
    return prikazi


if __name__ == '__main__':
    app.run()
    
    
