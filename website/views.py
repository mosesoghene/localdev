from flask import Blueprint, render_template
from flask_login import current_user, login_required

from .models import Post

views = Blueprint('views', __name__)

@views.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', user=current_user, posts=posts)

@views.route('/post/<int:id>')
def view_post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html', post=post, user=current_user)
