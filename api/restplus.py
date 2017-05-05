import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

# Create flask_restplus API object
api = Api(version="1.0", title="My Blog API",
          description="Exploring REST api creation using Flask restful")


@api.errorhandler
def default_error_handler(e):
    message = "Unhandled exception encountered"
    print(message)

    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    print(traceback.format_exc(e))
    return {'message': "Database result was required but not found"}, 404
