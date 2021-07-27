from flask import Flask, render_template



application = Flask(__name__)

@application.route('/')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True) #turn debug off for prodcution deployment
