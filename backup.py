app = Flask(__name__)
app.config['SECRET_KEY'] = "cross-path-alert"   #This is nothin but the flask backup

database = database()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/about")
def about():
    return render_template('about.html')
  
if __name__ == "__main__":
    app.run(debug=True)    # Remember to remove debug=True in production