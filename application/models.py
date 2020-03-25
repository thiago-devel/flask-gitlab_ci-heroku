from .shared import app, db
from .extra import get_ma

ma = get_ma(app)

class OrganizationModel(db.Model):
    __tablename__ = 'organization'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Organization {self.name}>"

class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = 'users'
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    bio = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


    def __repr__(self):
        return '<User {}>'.format(self.username)

class Member(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(100))
    firstname = db.Column(db.String(50), unique=False)
    lastname = db.Column(db.String(50), unique=False)
    registered_on = db.Column(db.DateTime, nullable=False)

class MemberSchema(ma.ModelSchema):
    class Meta:
        model = Member
        fields = ('id', 'username', 'email')

member_schema = MemberSchema(strict=True, only=('id', 'username'))
members_schema = MemberSchema(strict=True, many=True)