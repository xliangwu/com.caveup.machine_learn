import os


def convert_mysql_to_h2():
    path = r'D:\workspace\CMB-TBDOC\docs-core\sql'
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.sql' in file:
                files.append(os.path.join(r, file))

    for f in files:
        db_dml_convert(f)


def db_dml_convert(file):
    base = os.path.basename(file)
    with open(file) as fin, open('output/' + base, "w") as fout:
        for line in fin:
            print(line)
            if line.startswith("/*") or line.startswith(" SET NAMES utf8") or line.startswith(" SET character_set_client"):
                continue

            line = line.replace("CHARACTER SET utf8 COLLATE utf8_general_ci ", "")
            line = line.replace("CHARACTER SET utf8 COLLATE utf8_general_ci", "")
            fout.write(line)


def parse_table_name(file):
    base = os.path.basename(file)
    with open(file) as fin:
        for line in fin:
            if line.startswith("CREATE TABLE"):
                line = line.replace("CREATE TABLE", "").replace("(","").replace("\\'",'')
                print(line)


def parse_table():
    path = r'D:\workspace\CMB-TBDOC\docs-core\sql\db-000'
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.sql' in file:
                files.append(os.path.join(r, file))

    for f in files:
        parse_table_name(f)


if __name__ == '__main__':
    parse_table()
