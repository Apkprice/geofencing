from flask import Flask, request, jsonify
from geopy.distance import geodesic

app = Flask(__name__)

# Geofence center coordinates and radius
GEOFENCE_CENTER = (37.7749, -122.4194)  # San Francisco
GEOFENCE_RADIUS = 1.0  # 1 km radius

@app.route('/location', methods=['POST'])
def check_geofence():
    data = request.json
    user_coords = (data['latitude'], data['longitude'])

    # Calculate the distance between user location and geofence center
    distance = geodesic(GEOFENCE_CENTER, user_coords).km

    if distance <= GEOFENCE_RADIUS:
        return jsonify({'status': 'inside', 'message': 'User is inside the geofence!'})
    else:
        return jsonify({'status': 'outside', 'message': 'User is outside the geofence!'})

if __name__ == '__main__':
    app.run(debug=True)
