from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('holiday', __name__, url_prefix='/holiday')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_holiday():
    if request.method == 'POST':
        is_away = request.form['is_away']
        days = request.form['days']

        if not days:
            return jsonify({'status': 'Days value is required.'}), 403
        if not is_away:
            return jsonify({'status': 'Is_away is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO holiday (value)'
            ' VALUES (?)',
            (is_away, days)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, timestamp, is_away, days'
        ' FROM holiday'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    return jsonify({
        'status': 'Holiday successfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'timestamp': check['timestamp'],
            'is_away': check['is_away'],
            'days': check['days'],
        }
    }), 200
