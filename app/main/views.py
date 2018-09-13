from flask import render_template, request, redirect, url_for, abort, flash
from . import main
# from .. import db
from ..models import User
from app import login_manager
from .forms import PostForm
@main.route('/',methods=['GET','POST'])
def index():
    '''
    View page function that returns the pitch titles on the index page
    '''
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(actual_post=form.post.data,category=form.category.data, user_id=current_user.id)
        new_post.save_post()
        flash('Post has been created successfully')
    Post = Post.query.filter_by(id)

    return render_template('index.html',title = 'new_post')


