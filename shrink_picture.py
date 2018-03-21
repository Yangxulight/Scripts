from PIL import Image

path = '/Users/xyang/Downloads/'
file_name = 'profile{}.jpg'
size = (180, 240)

for i in range(1,2):
    im = Image.open(path+ file_name.format(i))
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
