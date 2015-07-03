from flask import Flask
from tasks import add, greeting

app = Flask(__name__)

@app.route('/')
def test_status():
    return "It's working"

@app.route('/add')
def celery_add():
    add.delay(1,2)
    return "Add task complete"

@app.route('/greet')
def celery_greet():
    greeting.delay('doing stuff!!!')
    return "Greeting task complete"

if __name__ == "__main__":
    app.run(debug=True)


