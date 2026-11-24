from flask import Flask,render_template,session,redirect,url_for

app = Flask(__name__)
app.secret_key = "student_wtf_1980_management_system"


@app.route('/')
def index():
  """Index Page: Execute the create account"""
  return render_template("RegistrationForm.html")




if __name__ == "__main__":
  app.run(debug=True)