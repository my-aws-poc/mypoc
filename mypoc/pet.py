import time

from flask import request, jsonify, Blueprint

from mypoc import db
from mypoc.models import Pet

bp = Blueprint("pets", __name__)


@bp.route('/pets', methods=['GET', 'POST'])
def pet_manage():
    if request.method == 'GET':
        pets = Pet.query.order_by(Pet.id.asc())
        return jsonify([p.to_dict() for p in pets])

    elif request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            data = request.json
            name = data.get('name')
            age = data.get('age')

            count = Pet.query.filter(Pet.name == name).count()
            if count:
                return jsonify(error=f'Pet `{name}` already exist.'), 400

            pet = Pet(name=name, age=age, created=time.localtime())
            db.session.add(pet)
            db.session.commit()
            return jsonify(pet.to_dict())

        return jsonify(error='Content-Type not supported.'), 400
