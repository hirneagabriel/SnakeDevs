from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('stock', __name__, url_prefix='/stock')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_stock():
    if request.method == 'POST':
        product_name = request.form['product_name']
        quantity = request.form['quantity']
        product_expiration_date = request.form['product_expiration_date']
        shelf_number = request.form['shelf_number']

        if not product_name:
            return jsonify({'status': 'product_name value is required.'}), 403
        if not quantity:
            return jsonify({'status': 'quantity is required.'}), 403
        if not product_expiration_date:
            return jsonify({'status': 'product_expiration_date is required.'}), 403
        if not shelf_number:
            return jsonify({'status': 'shelf_number is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO stock (product_name, quantity, product_expiration_date, shelf_number) VALUES (?,?,?,?)',
            (product_name, quantity, product_expiration_date, shelf_number),
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, product_name, quantity, product_expiration_date, shelf_number'
        ' FROM stock'
        ' ORDER BY product_expiration_date DESC'
    ).fetchone()
    return jsonify({
        'status': 'Stock successfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'product_name': check['product_name'],
            'quantity': check['quantity'],
            'product_expiration_date': check['product_expiration_date'],
            'shelf_number': check['shelf_number'],
        }
    }), 200
