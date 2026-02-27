from flask import Flask,jsonify,render_template,request,redirect,flash
from models import db,create_tables,Company,Item,Purchase,Sales
from flask_migrate import Migrate
#store the flask in a variable
app = Flask(__name__) 
#The secret key to that prevent the others from editing the flash message
app.secret_key = "namma_kadai_secret_key"

# ✅ DATABASE CONFIGURATION
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1122@localhost/namma_kadai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# REGISTER APP WITH DB
db.init_app(app)

@app.route('/home', methods=['GET'])
def home():
        existing = Company.query.filter_by(company_name="Namma Kadai").first()
        #to list the items in a order by the id
        items = Item.query.order_by(Item.item_id).all()

        return render_template(
            'index.html',
            name=existing.company_name if existing else "No Company",
            balance=existing.cash_balance if existing else 0,
            items=items
        )


@app.route('/home/add',methods=['POST'])
def add_item():
    item_name = request.form.get("item_input")
        #checking the item name is new to avoid the duplication
    if item_name:
        try:
            #saving the ui input to the item table item_name in a variable
            new_item = Item(item_name=item_name)
            #add is temporvery location 
            db.session.add(new_item)
            #commit saves the change
            db.session.commit()
            return redirect('/home')
        except Exception as e:
            db.session.rollback()
            flash("Sorry item alredy Exits..!", "error")
            return redirect('/home')


@app.route('/home/delete/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item deleted successfully"}), 200


@app.route('/home/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get(item_id)

    if request.method == "POST":
        new_name = request.form.get("item_input")

        if not new_name or new_name.strip() == "":
            flash("Item name cannot be empty!", "error")
            return redirect(f"/home/edit/{item_id}")

        item.item_name = new_name
        db.session.commit()

        flash("Item updated successfully!", "success")
        return redirect('/home')

    return render_template('edit.html', item=item)




@app.route('/purchase', methods=['GET'])
def get_purchase_page():
    purchases = Purchase.query.all() #fetch all purchase records
    return render_template('purchase.html', purchases=purchases)



if __name__ == "__main__":   
    app.run(debug=True)












































































# @app.route('/home',methods = ['GET'])
# def home():
#     existing = Company.query.filter_by(company_name="Namma Kadai").first()
#     items = Item.query.order_by(Item.item_id).all()

#     result = []

#     for item in items: 
#         item_dict = {}
#         item_dict["id"]= item.item_id
#         item_dict["name"] = item.item_name
#         result.append(item_dict)

#         result.sort(key=lambda x: x["id"])
#     return render_template('index.html', name=existing.company_name, balance=existing.cash_balance, items=result)