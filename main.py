from flask import Flask,jsonify,render_template
from models import db,create_tables,Company,Item,Purchase,Sales
from flask_migrate import Migrate

@app.route('/home',methods = ['GET'])
def home():
    existing = Company.query.filter_by(company_name="Namma Kadai").first()
    items = Item.query.order_by(Item.item_id).all()

    result = []

    for item in items: 
        item_dict = {}
        item_dict["id"]= item.item_id
        item_dict["name"] = item.item_name
        result.append(item_dict)

        result.sort(key=lambda x: x["id"])
    return render_template('index.html', name=existing.company_name, balance=existing.cash_balance, items=result)