# webfortune

## Final for DevOps

To install, type these commands starting in your home directory (if you are in Windows, type source env/Scripts/activate in place of the fourth line below):

```
git clone https://github.com/maddyelwood/webfortune webfortune
cd webfortune
python3 -m venv env
source env/bin/activate 
pip install -r requirements.txt
```

To create the docker container and run the program through the docker container, type these commands (with specified port before the colon in the second line):

```
docker build -t webfortune .
docker run -dp 8006:5000 webfortune
```

To run the application locally, type this command (again with specified port):

```
flask run --host=0.0.0.0 -port=8006
```

To test the app.py program

```
coverage run -m pytest
coverage report -m
```
