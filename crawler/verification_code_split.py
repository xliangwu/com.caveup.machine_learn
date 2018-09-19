import glob
from os.path import basename
from crawler.image_char_splitter import ImageCharSplitter


def split(input_dir, output_dir):
    splitter = ImageCharSplitter()
    for pic in glob.glob(input_dir):
        base_name = basename(pic)
        file_name = base_name.split(".")[0]
        output_pattern = output_dir + "/" + file_name + "_{}.jpg"
        print("Split file: {}".format(base_name))
        splitter.split(pic, output_pattern)


if __name__ == '__main__':
    input = r'C:\Users\wuxue\Pictures\train\*.jpg'
    output = r'C:\Users\wuxue\Pictures\split'
    split(input, output)
