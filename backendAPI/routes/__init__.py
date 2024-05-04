from routes import User
from configs.config import Config

def configure_routing(app):
    app.include_router(User.router, prefix=Config.URL_Prefix)
