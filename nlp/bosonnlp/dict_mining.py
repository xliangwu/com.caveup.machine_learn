from bosonnlp import BosonNLP


def data_clean(input_path):
    with open(input_path, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line)


def dict_mining():
    nlp = BosonNLP('6cfIzKI1.27567.fLaZOvRXwl8f')

    s = ['整流级逆变级滤波器负载三相检测abcdq双SVM控制dqabcADRCADRCaubucu*du*quotωotωinvTrecTuqud图3基于ADRC的TSMC闭环控制系统框图Fig.3Closed-loopcontroldiagramofTSMCbasedonADRCADRC采用图1结构。',
         '但励磁绕组时间常数较大，闭环控制系统的截止频率较低，影响发电机输出端电压的响应速度。']
    data = nlp.depparser(s)
    nouns = extract_noun(data)
    print(nouns)


def extract_noun(data_list):
    nouns = []
    for data in data_list:
        tags = data['tag']
        words = data['word']
        for i in range(len(tags)):
            if tags[i] == 'NN':
                nouns.append(words[i])

    return nouns


if __name__ == '__main__':
    data_clean(r'C:\tmp\电力语料.txt')
