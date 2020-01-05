import os
import re

dir = '_posts'
pattern = re.compile(r'thumb:\s*(.*)\n')
for filename in os.listdir(dir):
    if filename.startswith('.'):
        continue
    with open(dir + os.sep + filename) as f:
        conent = f.read()
        pass
    matches = pattern.findall(conent)
    if len(matches) == 0:
        continue
    img = matches[0][1:]
    print(img)
    outimg = img + '_360.jpg'
    if os.path.isfile(outimg):
        continue
    cmd = 'convert "' + img + '" -resize 360x360\\> "' + outimg + '"'
    os.system(cmd)
    pass