from app import app
from flask_bootstrap import Bootstrap
app.config['SECRET_KEY'] = 'Life is short,You need Taffy!'
bootstrap = Bootstrap(app)
# app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
