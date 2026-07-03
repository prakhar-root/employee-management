class Config:
    SECRET_KEY = "dev-secret-key"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://employee_user:employee123@employee-mysql:3306/employee_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
