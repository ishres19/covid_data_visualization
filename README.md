# Covid Data visualization Website

## How to run the code on Windows:
1. Go to the data_visualization_project directory
`cd data_visualization_project`

2. Install pip
(copy paste the following in the terminal)
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
then:
`py get-pip.py`

3. Install virtual environment (only if you have python2, python3 comes with virtual environment pre- installed)
`py -2 -m pip install virtualenv`

4. activate the environment
`<name of environment>Scriptsactivate`
(data_viz_project is the name of the environment)

5. install flask
`pip install Flask`

6. install bokeh
`pip install bokeh`

7. install pandas
`pip install pandas`

8. Set the FLASK_APP environment variable.
`setx FLASK_APP “website_data_viz.py"`

6. run the application:
`flask run`
    
# Covid Data visualization on MacOS and Python3

1. Go to the data_visualization_project directory
`cd data_visualization_project`

2. Install pip
(copy paste the following in the terminal)
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
then:
`py get-pip.py`

3. activate the environment
`. <data_viz_project>/bin/activate`

4. install flask
`pip install Flask`

5. install bokeh
`pip install bokeh`

6. install pandas
`pip install pandas`

8. Set the FLASK_APP environment variable.
`export FLASK_APP=website_data_viz.py`

6. run the application:
`flask run`
