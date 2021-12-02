from flask import Flask, render_template

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/request/')
def request():
    return render_template('request.html', categorie_film = "Films")



if __name__ == "__main__":
    app.run()
