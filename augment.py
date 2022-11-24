import imutils
import cv2
import os
import re
import random

anglelist = [0,90,180,270]

def blur(image):
    return cv2.blur(image, (2,2))

def adjust_contrast_brightness(image, contrast:float=3, brightness:int=1):
    brightness += int(round(255*(1-contrast)/2))
    return cv2.addWeighted(image, contrast, image, 0, brightness)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    

def random_augmentation(image, number):
    if number == 0:
        return blur(image)
    elif number == 1:
        return adjust_contrast_brightness(image)
    elif number == 2:
        return grayscale(image)
    else:
        return image

def imagedrehen(pathtoimage, name):
    image = cv2.imread(pathtoimage)
    for angle in anglelist:
        rotated = imutils.rotate_bound(image, angle)
        random_num = random.randint(0,5)
        rotated = random_augmentation(rotated, random_num)
        cv2.waitKey(0)
        if file.endswith('.jpeg'):
            cv2.imwrite('output/'+name[:-5] + '-' + str(angle) + '.jpeg', rotated)
        if file.endswith('.jpg'):
            cv2.imwrite('output/'+name[:-4] + '-' + str(angle) + '.jpg', rotated)
        print('image',name,'rotated',angle,'°')

def xmldrehen(pathtoxml, xmlname):
    extension = ""
    len = 0
    if file.endswith('.jpeg'):
        extension = ".jpeg"
    if file.endswith('.jpg'):
        extension = ".jpg"
    old = open(pathtoxml, "r").readlines()
    for angle in anglelist:
        newxmlname = xmlname[:-4] + '-' + str(angle) + '.xml'
        print('XMLfile ' + xmlname + ' rotated ' + str(angle) + '°')
        new = open('output/'+newxmlname, 'w')
        # no rotation
        if angle == 0:
            for line in old:
                if '<folder>' in line:
                    pass
                elif '<path>' in line:
                    pass
                elif '<filename>' in line:
                    
                    oldfilenametag = xmlname[:-4] + extension
                    newfilenametag = newxmlname[:-4] + extension
                    line = line.replace(oldfilenametag, newfilenametag)
                    new.write(line)
                else:
                    new.write(line)
        # rotate 90
        elif angle == 90:
            # scan
            xmin0 = []
            ymin0 = []
            xmax0 = []
            ymax0 = []
            for line in old:
                if '<xmin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    xmin0.append(i)
                if '<ymax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    ymax0.append(i)
                if '<xmax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    xmax0.append(i)
                if '<ymin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    ymin0.append(i)
                if '<height>' in line:
                    w = int(re.search(r'\d+', line).group())
            # write
            yminn = 0
            xminn = 0
            ymaxn = 0
            xmaxn = 0
            for line in old:
                if '<folder>' in line:
                    pass
                elif '<path>' in line:
                    pass
                elif '<filename>' in line:
                    oldfilenametag = xmlname[:-4] + extension
                    newfilenametag = newxmlname[:-4] + extension
                    line = line.replace(oldfilenametag, newfilenametag)
                    new.write(line)
                elif '<width>' in line:
                    line = line.replace('width','height')
                    new.write(line)
                elif '<height>' in line:
                    line = line.replace('height','width')
                    new.write(line)
                elif '<ymax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((xmax0[ymaxn])))
                    ymaxn += 1
                    new.write(line)
                elif '<xmin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((w - ymax0[xmaxn])))
                    xmaxn += 1
                    new.write(line)
                elif '<ymin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str(xmin0[yminn]))
                    yminn += 1
                    new.write(line)
                elif '<xmax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((w - ymin0[xminn])))
                    xminn += 1
                    new.write(line)
                else:
                    new.write(line)
        # rotate 180
        elif angle == 180:
            # scan
            xmin0 = []
            ymin0 = []
            xmax0 = []
            ymax0 = []
            for line in old:
                if '<xmin>' in line :
                    i = int(re.search(r'\d+', line).group())
                    xmin0.append(i)
                if '<ymax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    ymax0.append(i)
                if '<xmax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    xmax0.append(i)
                if '<ymin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    ymin0.append(i)
                if '<height>' in line:
                    h = int(re.search(r'\d+', line).group())
                if '<width>' in line:
                    w = int(re.search(r'\d+', line).group())
            # write
            yminn = 0
            xminn = 0
            ymaxn = 0
            xmaxn = 0
            for line in old:
                if '<folder>' in line:
                    pass
                elif '<path>' in line:
                    pass
                elif '<filename>' in line:
                    oldfilenametag = xmlname[:-4] + extension
                    newfilenametag = newxmlname[:-4] + extension
                    line = line.replace(oldfilenametag, newfilenametag)
                    new.write(line)
                elif '<ymax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((h-ymin0[yminn])))
                    yminn += 1
                    new.write(line)
                elif '<xmax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((w - xmin0[xminn])))
                    xminn += 1
                    new.write(line)
                elif '<ymin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((h-ymax0[ymaxn])))
                    ymaxn += 1
                    new.write(line)
                elif '<xmin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((w - xmax0[xmaxn])))
                    xmaxn += 1
                    new.write(line)
                else:
                    new.write(line)
        # rotate 270
        elif angle == 270:
            # scan
            xmin0 = []
            ymin0 = []
            xmax0 = []
            ymax0 = []
            for line in old:
                if '<xmin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    xmin0.append(i)
                if '<ymax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    ymax0.append(i)
                if '<xmax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    xmax0.append(i)
                if '<ymin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    ymin0.append(i)
                if '<width>' in line:
                    h = int(re.search(r'\d+', line).group())
            # write
            yminn = 0
            xminn = 0
            ymaxn = 0
            xmaxn = 0
            for line in old:
                if '<folder>' in line:
                    pass
                elif '<path>' in line:
                    pass
                elif '<filename>' in line:
                    oldfilenametag = xmlname[:-4] + extension
                    newfilenametag = newxmlname[:-4] + extension
                    line = line.replace(oldfilenametag, newfilenametag)
                    new.write(line)
                elif '<ymax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((h - xmin0[yminn])))
                    yminn += 1
                    new.write(line)
                elif '<xmin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((ymin0[xminn])))
                    xminn += 1
                    new.write(line)
                elif '<ymin>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((h - xmax0[ymaxn])))
                    ymaxn += 1
                    new.write(line)
                elif '<xmax>' in line:
                    i = int(re.search(r'\d+', line).group())
                    line = line.replace(str(i), str((ymax0[xmaxn])))
                    xmaxn += 1
                    new.write(line)
                else:
                    new.write(line)
        else:
            print('Unexpected angle in list: ' +  str(angle))

def imagemirror(pathtoimage, name):
    image = cv2.imread(pathtoimage)
    rotated = cv2.flip(image, flipCode=1)
    cv2.waitKey(0)
    if file.endswith('.jpeg'):
        cv2.imwrite('output/' + name[:-5] + '-' + 'mirrored' + '.jpeg', rotated)
    if file.endswith('.jpg'):
        cv2.imwrite('output/' + name[:-4] + '-' + 'mirrored' + '.jpg', rotated)
    print('image', name, ' mirrored')

def xmlmirror(pathtoxml, xmlname):
    extension = ""
    len = 0
    if file.endswith('.jpeg'):
        extension = ".jpeg"
    if file.endswith('.jpg'):
        extension = ".jpg"
    old = open(pathtoxml, "r").readlines()
    newxmlname = xmlname[:-4] + '-' + 'mirrored' + '.xml'
    print('XMLfile ' + xmlname + ' mirrored')
    new = open('output/'+newxmlname, 'w')
    # scan
    xmin0 = []
    ymin0 = []
    xmax0 = []
    ymax0 = []
    for line in old:
        if '<xmin>' in line:
            i = int(re.search(r'\d+', line).group())
            xmin0.append(i)
        if '<ymax>' in line:
            i = int(re.search(r'\d+', line).group())
            ymax0.append(i)
        if '<xmax>' in line:
            i = int(re.search(r'\d+', line).group())
            xmax0.append(i)
        if '<ymin>' in line:
            i = int(re.search(r'\d+', line).group())
            ymin0.append(i)
        if '<width>' in line:
            if '-270' in xmlname:
                pass
            else:
                w = int(re.search(r'\d+', line).group())
        if '<height>' in line:
            if '-270' in xmlname:
                w = int(re.search(r'\d+', line).group())
            else:
                pass
    # write
    yminn = 0
    xminn = 0
    ymaxn = 0
    xmaxn = 0
    for line in old:
        if '<folder>' in line:
            pass
        elif '<path>' in line:
            pass
        elif '<filename>' in line:
            oldfilenametag = xmlname[:-4] + extension
            newfilenametag = newxmlname[:-4] + extension
            line = line.replace(oldfilenametag, newfilenametag)
            new.write(line)
        elif '<ymin>' in line:
            i = int(re.search(r'\d+', line).group())
            line = line.replace(str(i), str((ymin0[yminn])))
            yminn += 1
            new.write(line)
        elif '<xmax>' in line:
            i = int(re.search(r'\d+', line).group())
            line = line.replace(str(i), str((w - xmin0[xminn])))
            xminn += 1
            new.write(line)
        elif '<ymax>' in line:
            i = int(re.search(r'\d+', line).group())
            line = line.replace(str(i), str((ymax0[ymaxn])))
            ymaxn += 1
            new.write(line)
        elif '<xmin>' in line:
            i = int(re.search(r'\d+', line).group())
            line = line.replace(str(i), str((w - xmax0[xmaxn])))
            xmaxn += 1
            new.write(line)
        else:
            new.write(line)

# rotate images and xml
for file in os.listdir("dataset/"):
    if file.endswith('.jpeg'):
        imagedrehen('dataset/'+file, file)
    if file.endswith('.jpg'):
        imagedrehen('dataset/'+file, file)
    if file.endswith('.xml'):
        xmldrehen('dataset/'+file, file)

# mirror images and xml
for file in os.listdir("output/"):
    if file.endswith('.jpeg'):
        imagemirror('output/'+file, file)
    if file.endswith('.jpg'):
        imagemirror('output/'+file, file)
    if file.endswith('.xml'):
        xmlmirror('output/'+file, file)

print('The dataset from dataset/ is now augmented by rotating and mirroring it to output/, thus expanding the samplesize by a factor of 8.')
