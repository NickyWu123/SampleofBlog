#coding:utf-8
from os import path

from flask import Flask
from werkzeug.routing import BaseConverter
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,current_user
from flask_gravatar import Gravatar
from flask_babel import Babel,gettext as _
basedir=path.abspath(path.dirname(__file__))
# class RegexConverter(BaseConverter):
#     def __init__(self,url_map,*items):
#         super(RegexConverter,self).__init__(url_map)
#         self.regex=items[0]
babel=Babel()
pagedown = PageDown()
bootstrap=Bootstrap()
nav=Nav()
db=SQLAlchemy()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'


def create_app():
    app=Flask(__name__)
    #app.url_map.converters['regex']=RegexConverter
    app.secret_key='hard to guess string'
    #app.config.from_pyfile('babel.cfg')
    app.config['BABLE_DEFAULT_LOCALE']='zh'
    #print app.config
    #app.config['SECRET_KEY']='\xf9\xd0\xfa\x9d0\x14\x87"\x8fB)dG\x86%\xf9#\xbd\x92!\xed\xa15\x91'
    app.config['SQLALCHEMY_DATABASE_URI']=\
    'sqlite:///'+path.join(basedir,'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True
    # nav.register_element('top',Navbar(u'Flask入门'
    #                               ))
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    Gravatar(app, size=64)
    babel.init_app(app)
    #nav.init_app(app)
    from auth import auth as auth_bluepirnt
    from main import main as main_bluepirnt
    app.register_blueprint(auth_bluepirnt,url_prefix='/auth')
    app.register_blueprint(main_bluepirnt,static_folder='static')
    @babel.localeselector
    def get_locale():
        return current_user.locale
    return app



