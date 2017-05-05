from flask import request
from flask_restplus import Resource
from restapi.api.restplus import api
from restapi.api.business import (create_category, update_category,
                                  delete_category)
from restapi.database.models import Category
from restapi.api.api_model_view import category, category_with_posts

# initialize namespace
ns = api.namespace('blog/categories',
                   description='Operations related to blog categories')


# handle collections
@ns.route("/")
class CategoryCollection(Resource):

    @api.marshal_list_with(category)
    def get(self):
        categories = Category.query.all()
        return categories

    @api.respone(201, 'Category successfully created')
    @api.expect(category)
    def post(self):
        # create category
        data = request.json
        create_category(data)
        return None, 201


# handle individual categories
@ns.route("/<int:id>")
class CategoryItem(Resource):

    @api.marshal_with(category_with_posts)
    def get(self, id):
        return Category.query.filter(Category.id == id).one()

    @api.response(204, 'Category successfully update')
    @api.expect(category)
    def put(self, id):
        data = request.json
        update_category(id, data)
        return None, 204

    @api.response(204, 'Category successfully deleted')
    def delete(self, id):
        delete_category(id)
        return None, 204
