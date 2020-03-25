from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import Blueprint
from ..models import OrganizationModel, User, db

goals_slicer_api = Blueprint('goals_slicer_api', __name__)

@goals_slicer_api.route('/organizations', methods=['POST', 'GET'])
def handle_organizations():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_organization = OrganizationModel(name=data['name'])
            db.session.add(new_organization)
            db.session.commit()
            return {"message": f"organization {new_organization.name} has been created successfully."}, 201
        else:
            return {"error": "The request payload is not in JSON format"}, 400

    elif request.method == 'GET':
        organizations = OrganizationModel.query.all()
        results = [
            {
                "name": org.name
            } for org in organizations]

        return {"count": len(results), "organizatios": results}, 200

    return None

@goals_slicer_api.route('/users', methods=['POST', 'GET'])
def handle_user():
    if request.method == 'POST':
        """Create a user."""
        username = request.args.get('user')
        email = request.args.get('email')
        new_user = User(username=username,
                        email=email,
                        created=dt.now(),
                        bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                        admin=False)  # Create an instance of the User class
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return render_template('users.html',
                            users=User.query.all(),
                            title="Show Users")
    elif request.method == 'GET':
        if username and email:
            existing_user = User.query.filter(User.username == username or User.email == email).first()
            if existing_user:
                return make_response(f'{username} ({email}) already created!')
            new_user = User(username=username,
                            email=email,
                            created=dt.now(),
                            bio="In West Philadelphia born and raised, on the playground is where I spent most of my days",
                            admin=False)  # Create an instance of the User class
            db.session.add(new_user)  # Adds new User record to database
            db.session.commit()  # Commits all changes
        return render_template('users.html',
                            users=User.query.all(),
                            title="Show Users")
