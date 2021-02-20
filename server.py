
from flask import Flask, render_template, request, redirect 

import csv

app = Flask(__name__)
# # app.debug =True 
# # notice the new "Flask" class that is used to instantiate the app variable. 
# #let's test this new class with a print function
# print(__name__)

#the folllwing is a decorator: the @app decorator says that everytime there is a '/' returrn "hello world"

#different routes:

@app.route('/')
def my_home():
    return render_template('index.html')

#instead of repeating the routes code as below, here is an example of a "dynamic code" that will 
#reference the existing html files and only require one set of code going forward. 
#the < > arrows allow us to faciliate this dynamic code.

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)
	
def write_to_file(data):
	with open('./Web_development/database.txt', mode = 'a') as database:
		email =data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
	with open('./Web_Development/database.csv', newline= '', mode= 'a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message]) 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		write_to_file(data)
    		return redirect('/Thank_you.html')
    	except:
    		return 'did not save to database'
    else:
    	return "something went wrong."
#created folder names "templates" and then moved index.html file into this new folder. 
#now it should be able to find index.html

# @app.route('/index.html')
# def my_index():
#     return render_template('index.html')

# # @app.route('/favicon')
# # def about_frank():
# #     return render_template('index.html')

# @app.route('/about.html')
# def about_frank():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

#the following route is a new set of code which I copied and pasted directly from 
#flask framework under the "request object" section.  This new route will allow
#visitors of my website to send an email to me directly.


	#I don't need any of this part of the code, but I'll leave it here for future reference.
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
