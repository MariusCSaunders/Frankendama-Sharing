#Imports app from the application folder
from application import app

#Sets app.py as the main program file
if __name__ == "__main__":
    app.run(debug="True", host="0.0.0.0")