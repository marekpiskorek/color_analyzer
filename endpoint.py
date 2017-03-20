from flask import json, Flask, request

from analyzer import get_colors_from_file
app = Flask('colors')


@app.route('/find_colors.json', methods=['POST'])
def get_dominant_colors(*args, **kwargs):
    filename = request.files['file']
    try:
        colors = get_colors_from_file(filename)
    except IOError:
        return json.dumps({'errors': 'This is not a valid image file'})
    else:
        return json.dumps({'colors': colors})
