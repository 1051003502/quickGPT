from flask import Flask, request, jsonify,render_template
#import openai_secret_manager
import openai
import os

# 初始化 Flask 应用
app = Flask(__name__)

# 设置 OpenAI API 密钥
#secrets = openai_secret_manager.get_secrets()
#openai.api_key = secrets["openai"]["api_key"]
openai.api_key = "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"

# 设置 Flask 应用的根路径
@app.route('/chat')
def index():
    return render_template("chat.html")
    # return app.send_static_file('chat.html')

# 接收前端发送的聊天请求
@app.route('/api/chat', methods=['POST'])
def chat():
    # 获取前端发送的文本
    text = request.form['text']
    # 调用 OpenAI API 进行聊天
    #text-davinci-002

    # response = openai.Completion.create(
    #     engine="gpt-3.5-turbo",
    #     prompt=(f"Conversation with GPT3.5 Turbo:\nUser: {text}\nGPT:"),
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )


    rsp = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "一个霸道总裁"},
            {"role": "user", "content": text}
        ]
    )
    print(rsp)
    message = rsp.get("choices")[0]["message"]["content"]

    # 获取聊天结果
    #message = response.choices[0].text.strip()
    # 返回聊天结果给前端
    return jsonify({'text': message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))