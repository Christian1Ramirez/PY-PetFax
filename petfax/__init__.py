from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "This is index"

    from . import pet
    app.register_blueprint(pet.bp)

    from . import facts
    app.register_blueprint(facts.bp_facts)

    return app