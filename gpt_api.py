import os
import openai
openai_api_key = os.getenv("openai_api_key")
openai.api_key=openai_api_key
def example1():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "今天天气真好"}
        ]
    )
    print(response)
    print(response.get("choices")[0]["message"]["content"])

def example2():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "你好"}
        ],
        temperature=1.5, # 0-2之间，越大越随机，越小越确定
        top_p=1, #随机取前多少概率的token，0.1意味着取前10%，越小越确定。top_p temperature两个参数推荐只使用一个
        n=2,#生成几个回答，默认是1个，我这里让它生成2个
        stream=False,#是否流式获得结果，流式就是chatgpt官网那种，结果是一点一点蹦出来的，用于长句子先得到部分结果
        stop="我",#停止词，生成出来“我”就停止生成
        max_tokens=100,#最多生成的token数量
        presence_penalty=0,#(-2.0,2.0) 越大模型就趋向于生成更新的话题，惩罚已经出现过的文本
        frequency_penalty=0,#(-2.0,2.0) 惩罚出现频率高的文本
        #logit_bias=None,#设置token的先验偏置
        user="会写代码的孙悟空"#一个表示您的终端用户的唯一标识符，可帮助OpenAI监控和检测滥用行为
    )
    print(response)
    print(response.get("choices")[0]["message"]["content"])
    print(response.get("choices")[1]["message"]["content"])

def chat_once(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.get("choices")[0]["message"]["content"]
    except:
        return ""

def chat_once_with_prompt(prompt,message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
                {"role": "user", "content": message}
            ]
        )
        return response.get("choices")[0]["message"]["content"]
    except:
        return ""

def chat_once_with_sb(prompt,sb): #sb:some body 不是骂人
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": sb},
                {"role": "user", "content": prompt}
            ]
        )
        return response.get("choices")[0]["message"]["content"]
    except:
        return ""

class ChatGPT:
    def __init__(self,sb="You are a helpful assistant."):
        self.sb=sb
        self.messages=[
            {"role":"system","content":sb}
        ]
    def send(self,prompt):
        try:
            self.messages.append({"role":"user","content":prompt})
            response=openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages
            )
            response_txt=response.get("choices")[0]["message"]["content"]
            self.messages.append({"role": "assistant", "content": response_txt})
            return response_txt
        except:
            return ""

def test_chat_once():
    res=chat_once("你好")
    print(res)

def test_chat_once_with_sb():
    prompt="请问你擅长什么？"
    sb="医生"
    res=chat_once_with_sb(prompt,sb)
    print(res)

def test_ChatGPT():
    chatgpt=ChatGPT()
    while True:
        text=input()
        if(text==""):break
        res=chatgpt.send(text)
        print(res)


if __name__ == '__main__':
    test_chat_once_with_sb()