from flask import Flask, request, jsonify, render_template
import io
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')
@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    if audio_file:
        audio_bytes = audio_file.read()

        # 使用OpenAI的Whisper模型進行語音識別
        transcript = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_bytes  # 直接傳遞bytes數據
        )
        text = transcript['text']  # 根據實際的API返回調整取值方式
        
        print(text)
        return jsonify({'message': '音訊文件上傳成功'})
    return jsonify({'error': '沒有接收到音訊文件'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0',)
