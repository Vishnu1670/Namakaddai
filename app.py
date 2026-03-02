from flask import Flask
from models import db,create_tables,Company
from flask_migrate import Migrate

app = Flask(__name__) 


#To connect the python and Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1122@localhost/namma_kadai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#To connect database object to the flask app
db.init_app(app) 
migrate = Migrate(app,db)#To reflect the table package everytime to the sql we use migrate


def create_company():
    existing = Company.query.filter_by(company_name="Namma Kadai").first() 
    cash_balance = 1000
    if not existing:
        company = Company(company_name="Namma Kadai", cash_balance=cash_balance)
        db.session.add(company)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():   
        create_tables() 
        create_company()   
    app.run(debug=True)