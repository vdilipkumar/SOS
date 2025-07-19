from flask import Flask, render_template

app = Flask(__name__)

# Sample grocery list
products = [
    {"name": "PROTEIN 1", "price": "$1.50 / lb"},
    {"name": "PROTEIN 2", "price": "$0.60 / lb"},
    {"name": "CREATIEN 1", "price": "$0.80 / lb"},
    {"name": "Multi VITs", "price": "$2.00 / box"},
    {"name": "PEANUT BUTTER", "price": "$1.20 / lb"},
    {"name": "OATS", "price": "$3.00 / pack"}
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)
