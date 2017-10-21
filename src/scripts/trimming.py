#coding:utf-8
import cv2
import drunkjudge

# @brief 画像を長方形にトリミングする
#
# @param[in] image         画像情報を扱うnumpy.ndarray
# @param[in] top           トリミングしたい長方形の左上の頂点のy座標
# @param[in] left          トリミングしたい長方形の左上の頂点のx座標
# @param[in] width         トリミングしたい長方形の幅
# @param[in] height        トリミングしたい長方形の高さ
# @param[in] file_name     トリミングする画像の名前
# @param[in] serial_number トリミングする画像の通し番号
#
# @return    image_name トリミング後の画像のファイル名
def trimming(image, top, left, width, height, file_name, serial_number):
    image_name = "../img/"+file_name+str(serial_number)+".png"
    if(height > width):
        height -= (height - width) / 2
        top += (height - width) /2
    else:
        width -= (width - height) / 2
        left += (width - height) /2
        
    trim = image[top:top+height, left:left+width]
    size = (256, 256)
    trim = cv2.resize(trim, size)
    
    cv2.imwrite(image_name,trim)
    #Judge
    flag = drunkjudge.drunkjudge(image_name)
    if flag < 0 :
        print('Danger')
    elif flag == 0 :
        print("Risk")
    else :
        print('OK')

    return image_name
