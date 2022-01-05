from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('temperature', __name__, url_prefix='/temperature')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_temperature():
    if request.method == 'POST':
        value = request.form['value']

        if not value:
            return jsonify({'status': 'The temperature is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO temperature (value)'
            ' VALUES (?)',
            (value,)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, timestamp, value'
        ' FROM temperature'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    return jsonify({
        'status': 'Temperature successfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'timestamp': check['timestamp'],
            'value': check['value'],
        }
    }), 200
