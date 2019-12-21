import json
import timeit
import requests
import pandas as pd


def process_one(question, actual_answer):
    start = timeit.default_timer()
    request_path = "http://101.132.193.40/AskQuestion?"
    params = {"question": question, "selectedDocs": "全选"}
    url = request_path + json.dumps(params)
    print("Process request:", url)
    response = requests.get(url)
    end = timeit.default_timer()

    result = []
    if response.status_code != 200:
        print("error")
        result.append([0, question, actual_answer, '', response.status_code, end - start, '', '', ''])
    else:
        data = response.json()
        list = data['data']['list']
        print(list)
        for index, answer in enumerate(list):
            result.append([index, question, actual_answer, answer['answer'], response.status_code, end - start, answer['score'], answer['same_ques'], answer['discriminate']])
    print(result)
    return result


def validate_from_excel():
    excel_file = r'D:\Google云盘\交易银行知识库项目\模型相关的测试\训练语料.xlsx'
    xl = pd.ExcelFile(excel_file)
    df = xl.parse('训练语料')
    print(df.columns)
    result_list = []
    for index, row in df.iterrows():
        question = row['QUESTION']
        actual_answer = row['ANSWER']
        result = process_one(question, actual_answer)
        result_list.extend(result)

    # output data to excel
    writer = pd.ExcelWriter('result_0.xlsx', engine='xlsxwriter')
    result_df = pd.DataFrame(result_list, columns=['index', 'question', 'actual_answer', 'predict_answer', 'response_code', 'use_time', '分数', '相似问题', '判定'])
    # Write your DataFrame to a file
    result_df.to_excel(writer, 'Sheet1')
    writer.save()


if __name__ == '__main__':
    # process_one('境外注册的B企业，向某离岸持牌银行C申请开立OSA账户、NRA外币账户和NRA人民币账户，是否需要账户监管机关事前核准','ss')
    validate_from_excel()
