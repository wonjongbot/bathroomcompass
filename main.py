from flask import Flask, render_template, url_for, request, jsonify
import random as rand
import string

locations = {}

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


def add_location(locations,bathroom_name, r_clean, r_smell, r_acess):
  # extends locations list
  if not(bathroom_name in locations) :
    
    locations[bathroom_name] = [r_clean, r_smell, r_acess, 0]

def edit_location(locations,bathroom_name, r_clean, r_smell, r_acess) :
  if bathroom_name in locations :
    count = locations[bathroom_name][3] + 1
    locations[bathroom_name][3] = count
    clean = (r_clean +   locations[bathroom_name][0])/count
    smell = (r_smell +   locations[bathroom_name][1])/count
    acess = (r_acess +   locations[bathroom_name][2])/count
    locations[bathroom_name] = [clean,   smell, acess, count]
  else :
    #return to review bathroom site and add a boolean variable syaing that the bathroom does not exist then edit the code on site_2 with a script tag saying that if the variable equals true print like the bathroom does not exist in databse
    dne = true
  

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
    edit_location(locations,bathroom_name, r_clean, r_smell, r_acess)
  return render_template('site_2.html')
  
@app.route('/3', methods=['GET', 'POST'])
def page_find() :
  return render_template('site_3.html')


@app.route('/position_data', methods=['GET', 'POST'])
def get_position() :
  if request.method == "POST":
    position_data = request.get_json()
    print(position_data)
  results = {'processed': 'true'}
  return jsonify(results)

@app.route('/4', methods = ['GET','POST'])
def page_new() :
  if request.method == 'POST':
    bathroom_name = request.form["fname"]
    r_clean = request.form['fclean']
    r_smell = request.form['fsmell']
    r_acess = request.form['facess']
    add_location(locations,bathroom_name, r_clean, r_smell, r_acess)
    print(locations[bathroom_name])
  return render_template('site_4.html')

@app.route('/debugging')
def page_debug() :
  
  return render_template('site_5.html', locations = locations)
  #Might have to make locations into two lists and iterate through both lists instead on site_5
  
if __name__ == "__main__":  # Makes sure this is the main process
  
  app.run( # Starts the site
    
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=rand.randint(2000, 9000)  # Randomly select the port the machine hosts on.  
	)