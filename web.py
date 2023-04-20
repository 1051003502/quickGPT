import openai
import os
from flask import Flask, request, jsonify,render_template
from mysql import get_app_data_from_dataset, insert_app_data_to_dataset
from gpt_api import chat_once,chat_once_with_sb,ChatGPT,chat_once_with_prompt
app = Flask(__name__)



@app.route("/quickgpt/index", methods=['GET'])
def get_quickgpt_index():
    app_data = get_app_data_from_dataset()
    print(app_data)
    return render_template("quickgpt.html", app_data=app_data)

@app.route("/", methods=['GET'])
def get_quickgpt_index2():
    app_data = get_app_data_from_dataset()
    print(app_data)
    return render_template("quickgpt.html", app_data=app_data)

@app.route("/quickgpt/createAPP")
def createAPP():
    return render_template("createAPP.html")

@app.route("/quickgpt/chatGPT")
def chatGPT():
    return render_template("chatGPT_index.html")

@app.route("/quickgpt/db/addAPPtoDB", methods=['POST'])
def addAPPtoDB():
    app_name = request.form.get("app_name")
    app_introduction = request.form.get("app_introduction")
    prompt = request.form.get("prompt")
    example = request.form.get("example")
    if(len(app_name)>15 or len(app_introduction)>150 or len(prompt)>100 or len(example)>100):
        print("长度太长，app创建失败")
        return "1"
    else:
        isSuccess = insert_app_data_to_dataset(app_name, app_introduction, prompt, example)
        if(isSuccess):
            return ""
        else:
            return "2"
    # request.form
    pass


openai.api_key=os.getenv("openAI_API_key")
# 设置 Flask 应用的根路径
@app.route('/quickgpt/chat')
def index():
    return render_template("chat.html")
    # return app.send_static_file('chat.html')


# 接收前端发送的聊天请求
@app.route('/api/chat', methods=['POST'])
def chat():
    test_mark=False
    if test_mark:
        print(request.form['user_message'])
        return {"bot_message":request.form['user_message']}
        return {'bot_message':"我很快乐 我很快乐 我很快乐 我很快乐 我很快乐 我很快乐 我很快乐 我很快乐 我很快乐 我很快乐我很快乐 我很快乐 我很快乐 我很快乐 我很快乐我很快乐 我很快乐 我很快乐 我很快乐 我很快乐我很快乐 我很快乐 我很快乐 我很快乐 我很快乐我很快乐 我很快乐 我很快乐 我很快乐 我很快乐"}
    prompt=request.form['prompt']
    user_message = request.form['user_message']
    print("/api/chat")
    print("prompt:",prompt)
    print("user_message:", user_message)
    response=chat_once_with_prompt(prompt,user_message)

    # 获取聊天结果
    #message = response.choices[0].text.strip()
    # 返回聊天结果给前端
    return {
        'bot_message': response
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0')
