# -*- coding: utf-8 -*-
"""
2017/06/26
RGB値それぞれの画像
python 2.7.13
opencv 3.XX
numpy  1.12.1
"""
import numpy as np
import cv2
import sys

if __name__ == "__main__":

	args = sys.argv

	# 画像の読み込み
	img_color = cv2.imread(args[1])
	print img_color
	print ('--------------------')
	print np.shape( img_color )
	print ('--------------------')


	# RGB値をそれぞれ抽出
	imgR = img_color[:,:,2]
	imgG = img_color[:,:,1]
	imgB = img_color[:,:,0]
	print np.shape(imgR),np.shape(imgG),np.shape(imgB)
	print('-----------------------')
	print(imgB)


	# 画像の表示
	cv2.imshow( 'color_R', imgR )
	cv2.imshow( 'color_G', imgG )
	cv2.imshow( 'color_B', imgB )

	average_color_per_row = np.average(img_color,axis=0)
	average_color = np.average(average_color_per_row, axis=0)
	average_color = np.uint8(average_color)
	print(average_color)
	average_sum = int(average_color[1])+int(average_color[0])+int(average_color[2])
	print((int(average_color[1])+int(average_color[0])) / float(average_color[2]))
	print(average_sum)
	if(int(average_color[1])+int(average_color[0])+int(average_color[2]) != 300):
		print(300 / float(average_sum) * average_color[2])
	average_color_img = np.array([[average_color]*500]*500, np.uint8)
	cv2.imwrite('avarage.png',average_color_img)

	cv2.imshow('average',average_color_img)
	# 何かしらのキーを押せばwindowを閉じる
	if cv2.waitKey(0):
		cv2.destroyAllWindows()


