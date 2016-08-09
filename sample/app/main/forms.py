#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from flask.ext.pagedown.fields import PageDownField
from wtforms.validators import DataRequired
from  flask_babel import gettext as _
class PostForm(Form):
    title=StringField(label=_(u'标题'),validators=[DataRequired()])
    body=PageDownField(label=_(u'正文'),validators=[DataRequired()])
    submit=SubmitField(label=_(u'发表'))
class CommentForm(Form):
    body=StringField(label=_(u'评论'),validators=[DataRequired()])
    submit=SubmitField(label=_(u'发表'))
