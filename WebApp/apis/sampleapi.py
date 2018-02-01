from flask import Blueprint, request, jsonify
from flask_mongoengine.wtf import model_form

testapi = Blueprint('testapi', __name__, url_prefix='/api/test')

@testapi.route('/', methods=['GET', 'POST'])
def testroute():
    '''
    Route specifically for testing.
    '''
    if request.method == 'GET':
        return jsonify({'status' : 'success GET'})
    else:
        return jsonify({'status' : 'success POST'})