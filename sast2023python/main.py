import argparse
import json
import random
import streamlit

# def parser_data():
#     """
#     从命令行读取用户参数
#     做出如下约定：
#     1. -f 为必选参数，表示输入题库文件
#     ...

#     :return: 参数
#     """
#     parser = argparse.ArgumentParser(
#         prog="Word filling game",
#         description="A simple game",
#         allow_abbrev=True
#     )

#     parser.add_argument("-f", "--file", help="题库文件", required=True)
#     parser.add_argument("--title", help="文章标题", default="" )
#     # TODO: 添加更多参数
    
#     args = parser.parse_args()
#     return args



def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
        # TODO: 用 json 解析文件 f 里面的内容，存储到 data 中
    f.close()
    
    return data



def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """

    keys = []
    for hint in hints:
        keys.append(streamlit.text_input(f"请输入{hint}:"))
        # TODO: 读取一个用户输入并且存储到 keys 当中

    return keys


def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for i in range(len(keys)):
        tmpstr = "{{"+str(i+1)+"}}"
        article = article.replace(tmpstr,keys[i])
        # TODO: 将 article 中的 {{i}} 替换为 keys[i]
        # hint: 你可以用 str.replace() 函数，也可以尝试学习 re 库，用正则表达式替换

    return article


if __name__ == "__main__":
    streamlit.title("Word Filling Game")
    filename = streamlit.text_input("文件名","example.json")
    title = streamlit.text_input("文章名","")
    streamlit.write("filename:",filename)
    streamlit.write("article:",title)
    data = read_articles(filename)
    articles = data["articles"]
    num = 0
    streamlit.write('文章标题:',articles[0]["title"])
    if(title == ""):
        num = random.randint(0,len(articles)-1)
    else:
        for article in articles:
            if(article["title"] == title):
                break
            else:
                num+=1
    if(num >= len(articles)):
        num = random.randint(0,len(articles)-1)
    article = articles[num]
    keys = get_inputs(article["hints"])
    streamlit.write(article["article"])
    article_words = replace(article["article"],keys)
    streamlit.write('您得到的结果是:',article_words)    
    # TODO: 根据参数或随机从 articles 中选择一篇文章
    # TODO: 给出合适的输出，提示用户输入
    # TODO: 获取用户输入并进行替换
    # TODO: 给出结果