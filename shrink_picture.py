from PIL import Image
from os import path
import sys

# usage: python picture1.jepg 180 240
if __name__ == '__main__':
    file_name = path.basename(sys.argv[1])
    length = int(path.basename(sys.argv[2]))
    width = int(path.basename(sys.argv[3]))
    im = Image.open(file_name)
    size = (length, width)
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255-x)
            im = im.convert('RGB')
            # paste(color, box, mask)
            im.paste((255,255,255), None, bgmask)
        else:
            im = im.convert('RGB')
    thumb = im.resize(size, Image.ANTIALIAS)
    thumb.save(path+'shrinked_'+file_name.format(i),quality=100)
