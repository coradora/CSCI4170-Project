from flask import jsonify, request
from google.cloud import firestore

db = firestore.Client(project='cloud-functions-419021', database='example')

def change_color(request):
    request_json = request.get_json(silent=True)
    
    colors_ref = db.collection('colors').document('colors')
    if request_json and 'color' in request_json:
        color = request_json['color']
        colors_ref.set({'color': color})
    else:
        # Attempt to fetch the current color; default to 'black' if not set
        current_color = colors_ref.get()
        if current_color.exists:
            color = current_color.to_dict().get('color', 'black')
        else:
            color = 'black'
    
    return jsonify({'color': color, 'message': f'The color is now {color}'})

