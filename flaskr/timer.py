from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('timer', __name__, url_prefix='/timer')


@bp.route('/', methods=('GET', 'POST'))
def set_timer():
    if request.method == 'POST':
        is_closed = request.form['is_closed']
        time = request.form['time']

        if not time:
            return jsonify({'status': 'Time value is required.'}), 403
        if not is_closed:
            return jsonify({'status': 'Is_closed is required.'}), 403

        db = get_db()
        db.execute(
            'INSERT INTO timer (is_closed, time) VALUES (?,?)',
            (is_closed, time),
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, timestamp, is_closed, time'
        ' FROM timer'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    return jsonify({
        'status': 'Timer successfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'timestamp': check['timestamp'],
            'is_closed': check['is_closed'],
            'time': check['time'],
        }
    }), 200
