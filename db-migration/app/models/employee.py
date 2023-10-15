import uuid

from app.core.db import db
from app.core.guid import GUID
from datetime import datetime


class EmployeeModel(db.Model):

    __tablename__ = "employee"
    id = db.Column(GUID(), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    number_of_leaves = db.Column(db.Integer)
    benefits = db.Column(db.String)
    type = db.Column(db.String)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime())
    contract_end_date = db.Column(db.Date())
    project = db.Column(db.String)

