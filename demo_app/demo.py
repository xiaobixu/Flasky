from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from demo_app.auth import login_required
from demo_app.db import get_db

bp = Blueprint('demo', __name__)


@bp.route('/')
def index():
    """Show all the posts, most recent first."""
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('demo/index.html', posts=posts)

@bp.route('/user')
def user_page():
    return render_template('auth/user.html')
