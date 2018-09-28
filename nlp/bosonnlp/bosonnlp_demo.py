from bosonnlp import BosonNLP

nlp = BosonNLP('6cfIzKI1.27567.fLaZOvRXwl8f')


def sentiment():
    # sentiment
    print(nlp.sentiment('大众深陷断轴门事件'))


def ner_test():
    # ner
    s = ['对于该小孩是不是郑尚金的孩子，目前已做亲子鉴定，结果还没出来，'
         '纪检部门仍在调查之中。成都商报记者 姚永忠']
    result = nlp.ner(s)[0]
    words = result['word']
    entities = result['entity']
    for entity in entities:
        print(''.join(words[entity[0]:entity[1]]), entity[2])


def suggest_test():
    # suggest
    term = '粉丝'
    result = nlp.suggest(term, top_k=10)
    for score, word in result:
        print(score, word)


def depparser_test():
    s = ['与普通双馈发电机相比，由于存在永磁磁场，可以减小励磁电流和转子励磁容量']
    result = nlp.depparser(s)
    print(result)
    print(' '.join(result[0]['word']))
    print(' '.join(result[0]['tag']))
    print(result[0]['head'])
    print(' '.join(result[0]['role']))


if __name__ == '__main__':
    depparser_test()
