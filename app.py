from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')
@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    if audio_file:
        audio_file.save("received_audio.wav")  # 保存音訊文件到伺服器
        return jsonify({'message': '音訊文件上傳成功'})
    return jsonify({'error': '沒有接收到音訊文件'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0',)
