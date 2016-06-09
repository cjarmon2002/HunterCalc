from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
import HC

app = Flask(__name__)

@app.route("/")
def index():
	Caster = request.args.get("Caster")
	Defense = (request.args.get("Defense"))
	if Defense:
		Defense = int(Defense)
	Armor = (request.args.get("Armor"))
	if Armor:
		Armor = int(Armor)
	Boxes = (request.args.get("Boxes"))
	if Boxes:
		Boxes = int(Boxes)	
	Focus = (request.args.get("Focus"))
	if Focus:
		Focus = int(Focus)
	if Caster and Defense and Armor and Boxes and Focus:
		percent = HC.survive_options(Caster, Defense, Armor, Boxes, Focus)
	else:
		percent = " "
	response = make_response(render_template("index.html", death=percent))
	return response

if __name__ == '__main__':
	app.run(debug=True)