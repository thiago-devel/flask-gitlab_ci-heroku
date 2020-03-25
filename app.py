from application.shared import create_app
from application.views import app_views
from application.apis.GoalsSlicerAPI import goals_slicer_api

app = create_app()
app.register_blueprint(app_views)
app.register_blueprint(goals_slicer_api, url_prefix='/api')

if __name__ == '__main__':
    app.run()