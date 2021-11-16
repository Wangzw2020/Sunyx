#!/usr/bin/python
# -*- coding: UTF-8 -*-

from PIL import Image
import cv2
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import scipy.io as sio

class bd():

   def re_img(self,path):
       img = cv2.imread(path)
       a=int(20) #x start
       b=int(700) #x end
       c=int(0) #y start
       d=int(510) #y end
       cropimg=img[c:d,a:b]
       imgresize=cv2.resize(cropimg,(640,480))
       return imgresize

   def H_use(self,fig1):
       name_1 = 'H11.mat'
       data = sio.loadmat(name_1)
       h1 = data['Homography_Mat_1']
       print(h1)
       im_out_1 = cv2.warpPerspective(fig1,h1,(640,480))
       return im_out_1

   def Htest(self,path1,path2):
       im_src_1 = cv2.imread(path1)
       img_dst = self.re_img(path2)
       im_out_1= self.H_use(im_src_1)
       pl.figure(),pl.imshow(img_dst[:, :, ::-1]), pl.title('dst'),
       pl.figure(),pl.imshow(im_out_1[:, :, ::-1]), pl.title('out1'),
       pl.show()
       return im_out_1, img_dst
       
   def Htest_dual(self,img_dual):
       img_dst = self.re_img(img_dual)
       return img_dst

   def Htest_rgb(self,img_rgb):
       im_out_1= self.H_use(img_rgb)
       return im_out_1
   
   def cal_H(self):
       num=0
       H=np.zeros((3,3))
       while int(num) < 10:
             print(num)
             name = 'h' + str(num) +'.mat'
             data=sio.loadmat(name)
             h = data['Homography_Mat_1']
             print("h:",h)
             num = num + 1
             H=H+h
       H=H/10
       H1_name = 'H.mat'
       print('H1:',H)
       sio.savemat(H1_name, {'Homography_Mat_1':H})

if __name__ == '__main__' :
    B=bd()
    num=0
    #B.cal_H()
    while int(num)<10:
          rgb_path="./rgb1/"+str(num)+".png"  
          dual_path="./rgb1/"+str(num)+"_dual.png"
          img_rgb,img_dual = B.Htest(rgb_path,dual_path)
          cv2.imwrite('./out/'+str(num)+'.png',img_rgb)
          cv2.imwrite('./out/'+str(num)+'_dual.png',img_dual)
          num=num+1
    

