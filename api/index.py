from flask import Flask, render_template, jsonify, request
import requests
app = Flask(__name__)
class GetGambar():
    def __main__(self):
        pass
    def get_gambar(self, prompt):
        endpoint = f"https://open-source-backend.vercel.app/generate-image?prompt={prompt}"
        response = requests.get(endpoint)

        if response.status_code == 200:
            try:
                response = response.json()
                response = response['paylaod']['data']
                return response  # Mengembalikan JSON jika berhasil
            except ValueError:
                return {"error": "Response bukan JSON yang valid"}
        else:
            return {"error": f"Request gagal dengan status {response.status_code}"}




@app.route('/')
def home():
    return render_template('index.html')
@app.route('/generate')
def generate_image():
    return render_template('image.html')

@app.route('/get-gambar')
def get_images():
    config_image = GetGambar()
    
    prompt = request.args.get('prompt')
    image = config_image.get_gambar(prompt)
    data = {
        'payload':{
            'promt':prompt,
            'data':image
        }
    }
    return jsonify(data)
@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
