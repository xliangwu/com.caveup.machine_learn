import os


def process():
    ids = set([])
    with open(r'C:\Users\wuxue\Desktop\test\a.csv', encoding='UTF-8') as fin:
        for line in fin:
            fields = line.split(",")
            key = fields[1] + "_" + fields[5]
            if key not in ids:
                ids.add(key)
            else:
                print(fields[0])


if __name__ == '__main__':
    process()
