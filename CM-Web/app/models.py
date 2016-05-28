from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Department(db.Model):
    __tablename__ = 'info_department'
    dept_id = db.Column(db.Integer, primary_key=True)
    dept_name = db.Column(db.String(64), unique=True)
    employee = db.relationship('Employee', backref='dept', lazy='dynamic')
    cost = db.relationship('Cost', backref='dept', lazy='dynamic')


class Role(db.Model):
    __tablename__ = 'info_role'
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(64), unique=True)
    permission = db.Column(db.Integer)
    default = db.Column(db.Boolean, default=False, index=True)
    employee = db.relationship('Employee', backref='role', lazy='dynamic')


class Employee(UserMixin, db.Model):
    # UserMixin 解决登陆的一些问题。
    __tablename__ = 'info_employee'
    employee_id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(64), unique=True, index=True)
    employee_name = db.Column(db.String(64))
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('info_role.role_id'))
    dept_id = db.Column(db.Integer, db.ForeignKey('info_department.dept_id'))
    cost = db.relationship('Cost', backref='employee', lazy='dynamic')

    @property
    def password(self):
        # @property 将方法变成属性
        raise ArithmeticError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(empl_id):
    # login_manager的回调函数，主要用于用户方法的get_id()
    # 回调函数接收以 Unicode 字符串形式表示的用户标识符。如果能找到用户，这个函数必须返回用户对象；否则应该返回 None。
    # get_id()返回用户的唯一标识符，使用 Unicode 编码字符串
    return Employee.query.get(int(empl_id))



class Cost(db.Model):
    __tablename__ = 'thing_cost'
    cost_id = db.Column(db.Integer, primary_key=True)
    event_time = db.Column(db.DateTime(), default=datetime.utcnow)
    record_time = db.Column(db.DateTime(), default=datetime.utcnow)
    cost_label = db.Column(db.String(64))      # 后期准备键一个cost标签表
    cost_detail = db.Column(db.Text)
    cost_money = db.Column(db.Float)
    dept_id = db.Column(db.Integer, db.ForeignKey('info_department.dept_id'))
    party_employee_id = db.Column(db.Integer, db.ForeignKey('info_employee.employee_id'))
