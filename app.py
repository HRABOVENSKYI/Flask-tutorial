from enum import Enum, auto

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask-user:flask-user@localhost/flask-tutorial-db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class OriginCountry(Enum):
    UKRAINE = auto()
    GERMANY = auto()
    USA = auto()
    CHINA = auto()


class Status(Enum):
    FUNCTIONAL = auto()
    INEFFECTIVE = auto()


class HandLoom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin_country: OriginCountry = db.Column(db.Enum(OriginCountry), nullable=False)
    price: float = db.Column(db.Float(10), nullable=False)
    power_in_watts: float = db.Column(db.Float(10), nullable=True)
    width_of_the_formed_tissue: int = db.Column(db.Integer(), nullable=False)
    material_of_the_produced_fabric: str = db.Column(db.String(20), nullable=False)
    manufacture_century: int = db.Column(db.String(2), nullable=False)
    status: Status = db.Column(db.Enum(Status), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Loom %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        origin_country = request.form['origin_country']
        price = request.form['price']
        power_in_watts = request.form['power_in_watts']
        width_of_the_formed_tissue = request.form['width_of_the_formed_tissue']
        material_of_the_produced_fabric = request.form['material_of_the_produced_fabric']
        manufacture_century = request.form['manufacture_century']
        status = request.form['status']
        new_loom = HandLoom(origin_country=origin_country,
                            price=price,
                            power_in_watts=power_in_watts,
                            width_of_the_formed_tissue=width_of_the_formed_tissue,
                            material_of_the_produced_fabric=material_of_the_produced_fabric,
                            manufacture_century=manufacture_century,
                            status=status)

        try:
            db.session.add(new_loom)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your loom'

    else:
        looms = HandLoom.query.order_by(HandLoom.date_created).all()
        return render_template('index.html', looms=looms)


@app.route('/delete/<int:id>')
def delete(id):
    loom_to_delete = HandLoom.query.get_or_404(id)

    try:
        db.session.delete(loom_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting a that loom'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    loom = HandLoom.query.get_or_404(id)

    if request.method == 'POST':
        loom.origin_country = request.form['origin_country']
        loom.price = request.form['price']
        loom.power_in_watts = request.form['power_in_watts']
        loom.width_of_the_formed_tissue = request.form['width_of_the_formed_tissue']
        loom.material_of_the_produced_fabric = request.form['material_of_the_produced_fabric']
        loom.manufacture_century = request.form['manufacture_century']
        loom.status = request.form['status']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your loom'

    else:
        return render_template('update.html', loom=loom)


if __name__ == '__main__':
    app.run(debug=True)
