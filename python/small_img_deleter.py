from PIL import Image
import os
import sys

allowed_ext = ['.jpg', '.jpeg', '.png']

def build_filenames(folder, allowed_ext):
    data = os.walk(folder)
    filenames = []
    for glob in data:
        for item in glob[2]:
            if os.path.splitext(item)[1] in allowed_ext:
                filenames.append(glob[0] + '/' + item)
                #filenames.append(item)
    return filenames

def split(fullpath):
    pieces = {}
    pieces['dir'] = os.path.split(fullpath)[0]
    pieces['name'] = os.path.split(fullpath)[1]
    pieces['ext'] = os.path.splitext(fullpath)[1]
    return pieces

def extract_image_details(filename):
    data = {}
    pic = Image.open(filename)
    w, h= pic.size
    if w >= h:
        orient = 'landscape'
    else:
        orient = 'portrait'
    if orient == 'landscape':
        aspect = w / float(h)
    else:
        aspect = h / float(w)
    data['width'] = w
    data['height'] = h
    data['orient'] = orient
    data['aspect'] = aspect
    return data

def delete_tinyimgs(filenames):
    for item in filenames:
        if (extract_image_details(item)['width'] < 450) or (extract_image_details(item)['height'] < 450):
            print "removing filename: %s with dimensions %s x %s" % (item, extract_image_details(item)['width'], extract_image_details(item)['height'])
            os.remove(item)


def main():
    folder = sys.argv[1]
    filenames = build_filenames(folder, allowed_ext)
    delete_tinyimgs(filenames)

if __name__ == "__main__":
    main()    
