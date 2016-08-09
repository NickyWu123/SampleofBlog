#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
class LoginForm(Form):
    username=StringField(label=u'用户名',validators=[DataRequired()])
    password=PasswordField(label=u'密码',validators=[DataRequired()])
    submit=SubmitField(label=u'提交')
class RegistrationForm(Form):
    email=StringField(label=u'邮箱地址',validators=[DataRequired(),Length(1,64),Email()])
    username=StringField(label=u'用户名',validators=[DataRequired(),Length(1,64),
                                                  Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,u'用户名字母数字下划线组成')
                                                  ])
    password=PasswordField(label=u'密码',validators=[DataRequired(),EqualTo('password2',message=u'密码不一致')])
    password2=PasswordField(label=u'确认密码',validators=[DataRequired()])
    submit=SubmitField(label=u'提交')