from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('rgb', __name__, url_prefix='/rgb')


@bp.route('/', methods=('GET', 'POST'))
@login_required
def set_rgb():
    if request.method == 'POST':
        red = request.form['red']
        green = request.form['green']
        blue = request.form['blue']

        if not red:
            return jsonify({'status': 'Red is required.'}), 403
        if not green:
            return jsonify({'status': 'Green is required.'}), 403
        if not blue:
            return jsonify({'status': 'Blue is required.'}), 403

        db = get_db()
        db.execute(
            "INSERT INTO rgb (red, green, blue) VALUES (?,?,?)",
            (red, green, blue)
        )
        db.commit()

    check = get_db().execute(
        'SELECT id, timestamp, red, green, blue'
        ' FROM rgb'
        ' ORDER BY timestamp DESC'
    ).fetchone()
    return jsonify({
        'status': 'RGB successfully recorded/retrieved',
        'data': {
            'id': check['id'],
            'timestamp': check['timestamp'],
            'red': check['red'],
            'green': check['green'],
            'blue': check['blue'],
        }
    }), 200
