from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample movies data
movies = [
    {"id": 1, "title": "Avengers: Endgame", "time": "6:00 PM", "seats": [0] * 10},
    {"id": 2, "title": "Inception", "time": "8:00 PM", "seats": [0] * 10},
]

@app.route('/')
def home():
    return render_template('index.html', movies=movies)

@app.route('/book/<int:movie_id>', methods=['GET', 'POST'])
def book(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    
    if request.method == "POST":
        seat_number = int(request.form["seat"])
        if movie and movie["seats"][seat_number] == 0:
            movie["seats"][seat_number] = 1  # Mark seat as booked
            return render_template("confirmation.html", movie=movie, seat=seat_number)
    
    return render_template("booking.html", movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
