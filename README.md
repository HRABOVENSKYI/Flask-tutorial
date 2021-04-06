# Flask-tutorial
### Content
* Wev-page for application using HTML, CSS
* Database MySQL (using PyMySQL)
* POST, PUT, DELETE methods

### How to run (Windows)
1. Clone this repository with the help of ___git clone git@github.com:HRABOVENSKYI/Flask-tutorial.git___
2. Move in this project directory.
3. Create your virtual environment in command line and activate it:
   * ___python -m venv venv___
   * ___venv\scripts\activate.bat___
4. Create MySQL database named flask-tutorial-db:
   * ___mysql -u root -p___
   * ___CREATE USER IF NOT EXISTS 'flask-user'@'localhost' IDENTIFIED BY '\<password\>';___
   * ___exit___
   * ___mysql -u flask-user -p___
   * ___create database if not exists `flask-tutorial-db`;___
   * ___exit___
5. Install all project requirements ___pip install -r requirements.txt___
6. Create needed tables in the database:
   * Open python interpreter with the command ___python___
   * Import our database ___from app import db___
   * Create all needed tables with command ___db.create_all()___
   * ___exit()___
7. Run application ___python app.py___