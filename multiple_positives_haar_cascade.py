import cv2
import numpy as np 
import os

data_dir = '/home/noman/neps_haar_playground/'

# The directory where all positive images are stored
pos_dir = data_dir + 'resized_pos/' 
# A temporary directory for containing the samples of the positive images 
temp_dir = data_dir + 'temp_mul_pos/'
# A destination directory where all positive images and associated .lst file will be saved
info_dir = data_dir+'info/'

for a in os.listdir(pos_dir):

    pos_img = pos_dir+a
    split_name = os.path.splitext(a)[0]
    sub_dir = temp_dir+split_name
    
    os.mkdir(sub_dir)
    # Please adjust the parameters such as h,w & angles in the following command to produce positive images as needed
    os.system('opencv_createsamples -img %s -bg %s/bg.txt -info %s/info.lst -pngoutput %s -maxxangle 0.2 -maxyangle 0.2 -maxzangle 0.2 -num 100 -h 5 -w 5'%(pos_img,data_dir,sub_dir,sub_dir))

info_file = open(info_dir+'info.lst','w+')

for b in os.listdir(temp_dir):
    
    sub_dir = temp_dir+b+'/'

    for c in os.listdir(sub_dir):

        if os.path.splitext(c)[1] == '.jpg':

            img = cv2.imread(sub_dir+c)

            count = len(os.listdir(info_dir))
            img_name = os.path.splitext(c)[0]
        
            coord1 = img_name[:4]
            coord2 = img_name[5:9]
            coord3 = img_name[10:14]
            coord4 = img_name[15:19]
            coord5 = img_name[20:24]

            int_coord2 = int(coord2)
            int_coord3 = int(coord3)
            int_coord4 = int(coord4)
            int_coord5 = int(coord5)

            new_img_name = '%04d_%s_%s_%s_%s.jpg'%(count,coord2,coord3,coord4,coord5)

            cv2.imwrite(info_dir+new_img_name,img)
            info_file.write('%s 1 %s %s %s %s\n'%(new_img_name,int_coord2,int_coord3,int_coord4,int_coord5))

info_file.close()
