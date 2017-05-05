from flask_restplus import fields
from restapi.api.restplus import api

blog_post = api.model('Blog post', {
    'id': fields.Integer(
        readonly=True, description="The unique id for a blog post"),
    'title': fields.String(
        required=True, description="Title for blog post"),
    'body': fields.String(required=True, description="Blog content"),
    'pub_date': fields.Datetime,
    'category_id': fields.Integer(attribute='category.id'),
    # XXX -shouldnt this be category.name?
    'category': fields.String(attribute='category.id'),
})


category = api.model('Blog Category', {
    'id': fields.Integer(
        readOnly=True, description="The unique id for a blog category"),
    'name': fields.String(required=True, description="Category Name")
})

category_with_posts = api.inherit('Blog category with posts', category, {
    'posts': fields.List(fields.Nested(blog_post))
})
