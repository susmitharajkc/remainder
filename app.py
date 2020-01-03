from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


cursor.execute("CREATE TABLE USER(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),lastname VARCHAR(255),date DATE ,age INT)")S
