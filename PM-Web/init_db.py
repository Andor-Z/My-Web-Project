from app.models import Role, Employee, Department, Cost
from app import db
from random import seed, randint, uniform
import forgery_py


# def dept_fake(count=10):
#     seed()
#     for i in range(count):
#         d = Department(
#             dept_name = forgery_py.name.company_name())
#         db.session.add(d)
#         db.session.commit()


# def employee_fake(count=20):
#     seed()
#     d_count = Department.query.count()
#     for i in range(count):
#         d = Department.query.offset(randint(0, d_count-1)).first()
#         e = Employee(
#             password=forgery_py.lorem_ipsum.word(),
#             employee_name=forgery_py.name.full_name(),
#             login_name=forgery_py.name.first_name(),
#             member_since=forgery_py.date.date(True),
#             dept=d)
#         db.session.add(e)
#         db.session.commit()


# def cost_fake(count=100):
#     seed()
#     d_count = Department.query.count()
#     for i in range(count):
#         d = Department.query.offset(randint(0, d_count-1)).first()
#         e = Employee.query.offset(randint(0, 20-1)).first()
#         c = Cost(
#             record_time=forgery_py.date.date(),
#             event_time=forgery_py.date.date(True),
#             cost_label=forgery_py.name.company_name(),
#             cost_detail=forgery_py.lorem_ipsum.sentence(),
#             cost_money=float(uniform(7, 2)),
#             dept=d,
#             employee=e
#         )
#         # cost_money 暂时有问题
#         db.session.add(c)
#         db.session.commit()


def init_db():
    db.drop_all()
    db.create_all()
    # dept_fake()
    # employee_fake()
    # cost_fake()
