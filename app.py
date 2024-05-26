from flask import Flask, request, jsonify, render_template
import io
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

class NamedBytesIO(io.BytesIO):
    name = 'transcript.wav'
    
@app.route('/')
def index():
    return render_template('test.html')
    
@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    audio_file = request.files['audio']
    if audio_file:
       # 讀取音訊文件到記憶體
        audio_stream = NamedBytesIO(audio_file.read())
        audio_stream.name = 'transcript.wav'  # 確保文件有一個名稱

        # 使用OpenAI的Whisper模型進行語音識別
        transcript = openai.Audio.transcribe(
            model="whisper-1",
            file=audio_stream
        )
        text = transcript['text']  # 根據實際的API返回調整取值方式

        print(text)
        return jsonify({'message': '音頻已處理', 'transcript': text})
    return jsonify({'error': '沒有接收到音訊文件'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000), host='0.0.0.0',)
