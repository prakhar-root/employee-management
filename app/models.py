from app import db

class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    phone = db.Column(db.String(20))

    department = db.Column(db.String(100))

    designation = db.Column(db.String(100))

    salary = db.Column(db.Float)

    joining_date = db.Column(db.Date)

    status = db.Column(db.String(20), default="Active")

    def __repr__(self):
        return f"<Employee {self.first_name}>"
