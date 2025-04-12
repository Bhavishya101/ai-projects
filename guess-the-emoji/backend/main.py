import base64
import json
from google.cloud import vision
from flask_cors import cross_origin

client = vision.ImageAnnotatorClient()

EMOTION_TO_EMOJI = {
    'joy': '😂',
    'sorrow': '😢',
    'anger': '😠',
    'surprise': '😮',
    'neutral': '😐'
}

@cross_origin()
def analyze_face(request):
    if request.method != 'POST':
        return ("Method not allowed", 405)

    try:
        data = request.get_json()
        if 'image' not in data:
            return json.dumps({'error': 'Image not found'}), 400

        # Strip base64 header
        content = data['image'].split(',')[1]
        image = vision.Image(content=base64.b64decode(content))

        response = client.face_detection(image=image)
        faces = response.face_annotations

        if not faces:
            return json.dumps({"emoji": "❓", "message": "No face detected"}), 200

        face = faces[0]
        emotions = {
            'joy': face.joy_likelihood,
            'sorrow': face.sorrow_likelihood,
            'anger': face.anger_likelihood,
            'surprise': face.surprise_likelihood
        }

        # Get dominant emotion
        sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
        top_emotion, score = sorted_emotions[0]
        emoji = EMOTION_TO_EMOJI[top_emotion if score > 2 else 'neutral']

        return json.dumps({ "emoji": emoji }), 200

    except Exception as e:
        return json.dumps({ "error": str(e) }), 500
