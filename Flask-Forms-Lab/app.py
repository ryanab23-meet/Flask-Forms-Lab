from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "ryan1ab"
password = "111"
facebook_friends=["Yasmeen","Mayyen","Ahmad", "Danial", "Sima", "Ebrahim","Maya","Loai"]



@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=='POST':
			if username == request.form['username'] and password == request.form['password']:
				return redirect (url_for('home'))
	return render_template('login.html')
		#else:
			#return render_template('login.html')


@app.route('/home', methods=['GET','POST'])
def home():  
		 return render_template('home.html',friends=facebook_friends)


@app.route('/friend_exists/<string:name>', methods=['GET','POST'])
def friend_exists(name):  
		 return render_template('friend_exists.html', n = name)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True)
