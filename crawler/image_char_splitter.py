from PIL import Image
import queue


class ImageCharSplitter:

    def __init__(self):
        pass

    def grey(self, image):
        # grey level
        lim = image.convert('L')
        return lim

    def threshold(self, image):
        threshold = 130
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        lim = image.point(table, '1')
        return lim

    def clean_noisy_point(self, image, areas, threshold=5):
        pix_data = image.load()

        for area in areas:
            if area.qsize() <= threshold:
                while not area.empty():
                    x_p, y_p = area.get()
                    pix_data[x_p, y_p] = 1

    def split_by_char(self, img, output_format, areas, threshold=5):
        area_map = {}
        for area in areas:
            if area.qsize() > threshold:
                min_x = 10000
                points = []
                while not area.empty():
                    x_p, y_p = area.get()
                    points.append((x_p, y_p))
                    min_x = min(min_x, x_p)
                area_map[min_x] = points

        keys = area_map.keys()
        sorted(keys)
        sorted_list = []
        for key in keys:
            sorted_list.append(area_map[key])

        size = len(sorted_list)
        for i in range(1, size):
            last_points = sorted_list[i - 1]
            points = sorted_list[i]
            if last_points and len(points) <= 24:
                last_points.extend(points)
                sorted_list[i] = None

        merged_list = [x for x in sorted_list if x]
        print("Merge size:", len(merged_list))

        # merge in vertical
        w, h = img.size
        for index in range(len(merged_list)):
            points = merged_list[index]
            min_x = 10000
            max_x = -1
            for p in points:
                min_x = min(min_x, p[0])
                max_x = max(max_x, p[0])

            for x in range(w):
                for y in range(h):
                    if (x, y) not in points:
                        img.putpixel((x, y), 1)
                    else:
                        img.putpixel((x, y), 0)

            box = (min_x, 0, max_x + 1, h)
            output = output_format.format(index)
            img.crop(box).save(output)

    # http://www.hi-roy.com/2017/09/20/Python%E9%AA%8C%E8%AF%81%E7%A0%81%E8%AF%86%E5%88%AB2/
    def cfs_area(self, image):
        pixdata = image.load()
        w, h = image.size
        visited = set()
        offset = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        cuts = []
        q = queue.Queue()
        for x in range(w):
            for y in range(h):

                if pixdata[x, y] == 0 and (x, y) not in visited:
                    q.put((x, y))
                    visited.add((x, y))

                area = queue.Queue()
                while not q.empty():
                    x_p, y_p = q.get()
                    area.put((x_p, y_p))
                    for x_offset, y_offset in offset:
                        x_c, y_c = x_p + x_offset, y_p + y_offset
                        if (x_c, y_c) in visited:
                            continue
                        visited.add((x_c, y_c))
                        try:
                            if pixdata[x_c, y_c] == 0:
                                q.put((x_c, y_c))
                        except:
                            pass

                cuts.append(area)

        return cuts

    def split(self, image_path, output_pattern, output_path=None):
        image = Image.open(image_path)
        image = self.grey(image)
        image = self.threshold(image)
        cuts = self.cfs_area(image)
        self.clean_noisy_point(image, cuts)
        if output_path:
            image.save(output_path)
        self.split_by_char(image, output_pattern, cuts)

    def print_pixel(self, image):
        pixel = image.load()
        size = image.size

        for h in range(size[1]):
            data = []
            for w in range(size[0]):
                data.append(pixel[w, h])
            print(data)


if __name__ == '__main__':
    imageSplitter = ImageCharSplitter()
    imageSplitter.split(r'322.jpg', 'cfs/{}.jpg', 'final.jpg')
