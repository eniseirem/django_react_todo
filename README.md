# django_react_todo
Django backend / React frontend Todo Project 

Local Setup
Python 3 and Pipenv need to already be installed.

Clone the repo to your computer. For example, to place it on your Desktop.

$ cd ~/Desktop
$ git clone https://github.com/eniseirem/django_react_todo.git
$ cd django_react_todo
Backend
Install the Pipenv packages and start a new shell. Then cd into the backend directory and run the local server.

$ cd backend
$ pipenv install
$ pipenv shell
(backend) $ ./manage.py runserver
You can see the API now at http://127.0.0.1:8000/api.
#user registration located at http://127.0.0.1:8000/api/users/create

Frontend
Open up a new command line console so there are now two open. Navigate to the frontend directory.

$ cd ~/Desktop
$ cd django_react_todo
$ cd frontend
Make sure React is already installed globally. If not $ npm install -g create-react-app.

Then install necessary packages and start the React server:

$ yarn install
$ yarn start
Navigate to http://localhost:3000/ to see a list of our DRF backend content outputted using React.
