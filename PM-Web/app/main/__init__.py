from flask import Blueprint, current_app

main = Blueprint('main', __name__)

from . import views, errors


@main.app_context_processor
def title_processor():
    return dict(WEB_TITLE=current_app.config['WEB_TITLE'])