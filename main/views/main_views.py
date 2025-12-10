from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.get("/")
def ping():
    return {"message":"pong"}
