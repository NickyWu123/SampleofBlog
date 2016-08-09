from app.models import Role,Post,User
from flask.ext.login import login_required,current_user
from app import db

User.query.get()