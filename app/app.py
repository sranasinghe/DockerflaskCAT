from flask import Flask, render_template
import random

app = Flask(__name__)
images = ["images/1.jpeg","images/2.jpg"]
@app.route("/")
# def index():
#   myimage = random.choice(images)
#   return render_template('/usr/src/app/templates/index.html', myimage=myimage)
def index():
  myimage = random.choice(images)
  return """
  <h1>Python Flask in Docker!</h1>
  <p>A sample web-app for running Flask inside Docker.</p>
  <img src="{{myimage}}" />
  """


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')