def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")

    db.init_app(app)

    from app import models

    with app.app_context():
        db.create_all()

    from app.routes import main
    app.register_blueprint(main)

    return app
