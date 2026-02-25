from flask_sqlalchemy  import SQLAlchemy


db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = "company"
    company_name = db.Column(db.String(255),primary_key = True)
    cash_balance = db.Column(db.Integer)

class Item(db.Model):
    __tablename__ = "item"
    item_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    item_name = db.Column(db.String(100), unique=True, nullable=False)

  
class Purchase(db.Model):
    __tablename__ = "purchase"
    purchase_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    timestamp = db.Column(db.DateTime, nullable=False)
    #The Forign key is taken and the parent table is item so in case “If the parent row is deleted, automatically delete this row too."
    #The index is mention because when the ondelete happen the table item has found by the index id.
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id', ondelete='CASCADE'), nullable=False, index=True)                                                                                                                     
    qty = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer)

class Sales(db.Model):
    __tablename__ = "sales"
    sales_id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    timestamp = db.Column(db.DateTime)
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id', ondelete='CASCADE'), nullable=False, index=True)
    qty = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer)

#To create a table for the model
def create_tables():
    #create_all() used to create the table for all the models in the db
    db.create_all()
    print ("Successfully reated")