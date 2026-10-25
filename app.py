from flask import Flask
import requests
app=Flask(__name__)

@app.route('/')
def locate():
    response=requests.get("https://ipapi.co/json/", timeout=10)
    print("STATUS CODE:", response.status_code)
    print("API RESPONSE:", response.json())
    data=response.json()
    latitude=data.get('latitude')
    longitude=data.get('longitude')
    city=data.get('city')
    if latitude is None or longitude is None:
        return{
            "error":"Could not retrieve location data.",
            "api_response":data
        },502

if __name__ == '__main__':
    app.run(debug=True)