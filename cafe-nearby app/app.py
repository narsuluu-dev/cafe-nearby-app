from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')  
def home():
    cafes = [ 
        {
            "name": "Miss Cafe",
            "image": "images/miss-cafe.jpg",
            "rating": "⭐ 4.5",
            "address": "800 East Thomas Street",
            "distance": "0.5 km away"      
        }, 
        {
            "name": "Cozy Corner",
            "address": "742 North Pine Street",
            "rating": 4.2,
            "image": "cosy-corner.jpg",
            "distance": "0.8 km away"
        }
    ] 
    return render_template("index.html", cafes=cafes)

@app.route('/favourites')
def favourites():
    return render_template("favourites.html") 

@app.route('/random')
def random():   # renamed to avoid conflict with Python's random module
    return render_template("random.html") 

@app.route('/filters') 
def filters():
    return render_template("filters.html") 

@app.route('/filters-results')
def filters_results():
    return render_template("filters-results.html") 

@app.route('/search-results')
def search_results():
    return render_template("search-results.html")  

@app.route('/settings')
def settings():
    return render_template("settings.html") 

@app.route('/cafe-detailes')  # keeping custom spelling
def cafe_detailes():
    return render_template("cafe-detailes.html") 

if __name__ == '__main__': 
    app.run(debug=True, use_reloader=False)



    
     
