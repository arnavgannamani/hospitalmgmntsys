# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_app():
    app = Flask(__name__)
    
    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'someCrazyS3cR3T!Key.!'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_root_password.txt').readline().strip()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'northwind'  # Change this to your DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)
    
    # Add the default route
    # Can be accessed from a web browser
    # http://ip_address:port/
    # Example: localhost:8001
    @app.route("/")
    def welcome():
        return "<h1>Welcome to the 3200 boilerplate app</h1>"

    # Import the various Beluprint Objects
    from src.products.products  import products
    from src.faculty.faculty import faculty
    from src.exam.exam import exam
    from src.meetings.meetings import meetings
    from src.patient.patient import patient
    from src.payment.payment import payment
    from src.department.department import department

    # Register the routes from each Blueprint with the app object
    # and give a url prefix to each
    app.register_blueprint(products, url_prefix='/p')
    app.register_blueprint(department, url_prefix = '/department')
    app.register_blueprint(exam, url_prefix = '/exam')
    app.register_blueprint(faculty, url_prefix='/faculty')
    app.register_blueprint(exam, url_prefix='/exam')
    app.register_blueprint(meetings, url_prefix='/meetings')
    app.register_blueprint(patient, url_prefix='/patient')
    app.register_blueprint(payment, url_prefix='/payment')


    # Don't forget to return the app object
    return app