from flask import Flask, render_template, url_for, request, jsonify
import random as rand
import string
import googlemaps

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


@app.route('/')  # What happens when the user visits the site
def base_page():

	random_num = rand.randint(1, 100000)  # Sets the random number
	return render_template(
		'base.html',  # Template file path, starting from the templates folder. 
		  # Sets the variable random_number in the template
	)


def add_location(locations, bathroom_name, r_clean, r_smell, r_acess, r_over):
  # extends locations list
  locations.extend(bathroom_name, r_clean, r_smell, r_acess, r_over)


@app.route('/2', methods = ['GET', 'POST'])
def page_report():
  rand_ammnt = rand.randint(10, 100)
  if request.method == 'POST':
    bathroom_name = request.form["fname"]
    r_clean = request.form['fclean']
    r_smell = request.form['fsmell']
    r_acess = request.form['facess']
    r_over = request.form['fover']
    print(bathroom_name)
    add_location(locations, bathroom_name, r_clean, r_smell, r_acess, r_over)
  return render_template('site_2.html')
  
@app.route('/3')
def page_find() :
  if request.method == "POST":
    positiondata = request.get_json()
    print(positiondata)
  return render_template('site_3.html')

@app.route('/4')
def page_new() :
  return render_template('site_4.html')


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=rand.randint(2000, 9000)  # Randomly select the port the machine hosts on.  
	)