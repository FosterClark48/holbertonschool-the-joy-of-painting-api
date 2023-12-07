# Script that runs the Flask App

from api.app import app

if __name__ == '__main__':
    app.run(debug=True)
