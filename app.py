from flask import Flask, render_template, Response, jsonify
from bs import get_info

app = Flask(__name__)

items = []

bus_stops = [16086, 16085, 877, 16183, 49881, 16111]

for n in bus_stops:
    items.append(get_info(n))

@app.route('/update_dep', methods=['POST'])
def updatedep():
    items = []
    for n in bus_stops:
        items.append(get_info(n))
    return jsonify('', render_template('dep_info_model.html', items=items))

@app.route('/')
def main():
    return render_template('index.html', items=items)

if __name__ == "__main__":
    app.run(host='10.0.0.107')