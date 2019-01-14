from flask import Flask, render_template
application = app = Flask(__name__)

posts = [
    {
        'author':'Ivan',
        'title':'Blog Post 1',
        'contenct':'First post contect',
        'date_posted':'Today',
    },
    {
        'author':'Ivan2',
        'title':'Blog Post 2',
        'contenct':'2 post contect',
        'date_posted':'Tomorrow',
    },
    {
        'author':'Ivan3',
        'title':'Blog Post 3',
        'contenct':'3 post contect',
        'date_posted':'Yesterday',
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts= posts)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
