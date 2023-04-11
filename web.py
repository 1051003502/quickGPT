from flask import Flask, request, jsonify,render_template
import openai
import os
app = Flask(__name__)
from mysql import get_app_data_from_dataset, insert_app_data_to_dataset


@app.route("/quickgpt/index", methods=['GET'])
def get_quickgpt_index():
    app_data = get_app_data_from_dataset()
    print(app_data)
    return render_template("quickgpt.html", app_data=app_data)


@app.route("/quickgpt/createAPP")
def createAPP():
    return render_template("createAPP.html")


@app.route("/quickgpt/db/addAPPtoDB", methods=['POST'])
def addAPPtoDB():
    app_name = request.form.get("app_name")
    app_introduction = request.form.get("app_introduction")
    prompt = request.form.get("prompt")
    example = request.form.get("example")
    isSuccess = insert_app_data_to_dataset(app_name, app_introduction, prompt, example)
    print(isSuccess)
    return "成功"
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
    text = request.form['user_message']
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
    return {
        'bot_message': message
    }



if __name__ == '__main__':
    app.run(host='0.0.0.0')
