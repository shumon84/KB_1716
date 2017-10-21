#coding:utf-8
import cv2

# @brief トリミングした画像の数
serial_number = 0


# @brief 画像を長方形にトリミングする
#
# @param[in] image      画像情報を扱うnumpy.ndarray
# @param[in] top        トリミングしたい長方形の左上の頂点のy座標
# @param[in] left       トリミングしたい長方形の左上の頂点のx座標
# @param[in] width      トリミングしたい長方形の幅
# @param[in] height     トリミングしたい長方形の高さ
#
# @return    image_name トリミング後の画像のファイル名
def trimming(image, top, left, width, height,number):
    image_name = str(number)+".png"
    trim = image[top:top+height, left:left+width]
    cv2.imwrite("../img/" + str(image_name),trim)
    return image_name
