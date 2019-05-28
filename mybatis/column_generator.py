def column_generator():
    with open('columns.csv', encoding='utf-8') as f:
        for line in f:
            keyword = line.strip('\n')
            # <columnOverride column="tid" property="tid"/>
            # print(r'<columnOverride column="{}" property="{}"/>'.format(keyword,keyword))
            print(r'<ignoreColumn column="{}"/>'.format(keyword, keyword))


if __name__ == '__main__':
    column_generator()
