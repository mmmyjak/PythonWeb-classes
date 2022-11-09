from flask_restx import reqparse

new_user_parser = reqparse.RequestParser()
new_user_parser.add_argument("name", required=True)
new_user_parser.add_argument("email", required=True)

new_post_parser = reqparse.RequestParser()
new_post_parser.add_argument("title", required=True)
new_post_parser.add_argument("text", required=True)
