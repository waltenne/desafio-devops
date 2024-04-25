from src import app
from src.db import DB
from flask import jsonify, request
from datetime import datetime

@app.route('/api/comment/new', methods=['POST'])
def api_comment_new():
    request_data = request.get_json()
    email = request_data['email']
    comment = request_data['comment']
    content_id = request_data['content_id']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with DB() as db:
        db.add_comment(email, timestamp, comment, content_id)
    
    message = f'Comment created and associated with content_id {content_id}'
    response = {
        'status': 'SUCCESS',
        'message': message,
    }
    return jsonify(response)

@app.route('/api/comment/list/<content_id>')
def api_comment_list(content_id):
    with DB() as db:
        comments = db.get_comments_by_id(content_id)
    
    if comments:
        return jsonify(comments)
    else:
        message = f'Content_id {content_id} not found'
        response = {
            'status': 'NOT-FOUND',
            'message': message,
        }
        return jsonify(response), 404
