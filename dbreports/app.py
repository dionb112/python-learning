from flask import Flask
import db
app = Flask(__name__)

@app.route('/orphans')
def display_orphan_count():
	n = db.get_orphan_count()
	return f"The number of orphans is:{n}."

app.run(debug=True)