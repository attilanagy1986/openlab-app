app created with Python using the Dash framework and Plotly library\
deployed at http://openlab.herokuapp.com

**Structure**\
Configurations folder:\
well configurations in .json

Data folder:\
.csv files holding well data

Python scripts:\
app.py initiates the Dash.app\
index.py defines the layout of the app\
openlab_app.py is a single bundle of all the scripts\
the other .py files define the layout and the content of the separate pages


requirements.txt:\
contains the Python dependencies

**Starting the app**\
run index.py to start the app\
alternatively run openlab_app.py, which contains all the scripts in a single bundle\
the app runs at http://127.0.0.1:8050 (local server)
