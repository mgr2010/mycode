from flask import Flask, render_template
app = Flask(__name__)

@app.route("/agetest/<int:age>")
def hello_name(age):
   return render_template("age.html", vy  = age)

if __name__ == "__main__":
   app.run(port=5006)
