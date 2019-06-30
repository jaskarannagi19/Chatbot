# Importing flask module in the project is mandatory 
# An object of Flask class is our WSGI application. 
from flask import Flask, render_template,request,jsonify,make_response
from flask_cors import CORS
from watson import  chatbot
import json

# Flask constructor takes the name of 
# current module (__name__) as argument. 
app = Flask(__name__) 
CORS(app)
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/') 
# ‘/’ URL is bound with hello_world() function. 
def hello_world():
	return render_template('html_file.html')

    
@app.route('/app', methods=['POST'])
def hello():
	#print("______________________")
	#data = request.json['query']
	#print(data)
	#print("______________________")
	query= str(request.data)
	
	result = c.submit(query)
	resp = make_response( result['b'] )
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp
# main driver function 
if __name__ == '__main__': 
	c = chatbot()
	# run() method of Flask class runs the application 
	# on the local development server. 
	app.run() 
