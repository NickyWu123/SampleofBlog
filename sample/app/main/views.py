#coding:utf-8
from os import path
from flask import render_template, redirect, make_response, flash,request,url_for
from .import main
from flask.ext.login import login_required,current_user
from ..import db
from ..models import Post,Comment,User
from .forms import PostForm,CommentForm
from datetime import datetime
from  flask_babel import gettext as _
#import flask.ext.pagedown
@main.route("/")
def index():
    page_index = request.args.get('page', 1, type=int)
    print page_index
    query = Post.query.order_by(Post.created.desc())
    pagination = query.paginate(page_index, per_page=20, error_out=False)
    posts = pagination.items
    #posts=Post.query.order_by(Post.created.desc())
    return  render_template('home.html',title=_(u"Nicky的博客"),posts=posts,pagination=pagination)
    #response.set_cookie('username','1234')
@main.route("/about")
def about():
    return render_template('about.html',title=_(u'关于本博客'))
# @main.route("/index")
# def index():
#     return  render_template('home.html',title=u'这是进入博客后的主页')
@main.route('/post/<int:id>',methods=['GET','POST'])
#@login_required
def post(id):
    post=Post.query.get_or_404(id)
    form=CommentForm()
    print dir(current_user)
    #user = User.query.filter_by(id=current_user.id).first()
    if form.validate_on_submit():
        comment=Comment(author=current_user,
                          body=form.body.data,
                          post=post)
        db.session.add(comment)
        db.session.commit()
    return render_template('posts/detail.html',title=post.title,form=form,post=post)
@main.route('/edit', methods=['GET', 'POST'])
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id=0):
    form = PostForm()

    if id == 0:
        user = User.query.filter_by(id=current_user.id).first()
        post = Post()
        #post.author=user
        #主要考虑到Post建立的问题如果直接用backref去指定,数据库会默认添加一个对象，这显然不利于体验
        post.author_id=user.id
    else:
        post = Post.query.get_or_404(id)
        post.created=datetime.now().strftime('%y-%m-%d %I:%M:%S %p')
        print post
    if form.validate_on_submit():
        post.body = form.body.data
        post.title = form.title.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.post', id=post.id))

    form.title.data = post.title
    form.body.data = post.body

    title = _(u'添加新文章')
    if id > 0:
        title = _(u'编辑')

    return render_template('posts/edit.html',
                           title=title,
                           form=form,
                           post=post)
@main.route('/delete_post/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    post=Post.query.filter_by(id=id).first()
    comment=Comment.query.filter_by(post_id=post.id)
    db.session.query(Comment).filter(Comment.post_id==post.id).delete()
    db.session.query(Post).filter(Post.id==post.id).delete()
    return redirect(url_for('.index'))
@main.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html')
@main.app_template_test('current_link')
def is_current_test(link):
    return link == request.path