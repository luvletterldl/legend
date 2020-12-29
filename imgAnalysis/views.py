import cv2
import os

from django.http import HttpResponse


def index(request):
    # 实现思路：传入一张图片，通过图像阀值处理将其二值化，此时答题卡被涂区域呈现为白色
    # 然后拿到每个题目四个选项形成矩形的四个顶点坐标，和每个选项间隔高度，通过这些参数确定每个选项的4个采样点
    # 获取到3个采样点的RGB,相加如果与3*3*255差值小于30即可确认为该选项为学生涂卡选项，如果与大于30即可认为是非涂卡选项
    img = cv2.imread(os.getcwd() + '/imgAnalysis/asserts/imgs/card.jpg')
    length, width, height = img.shape
    print(img.size, img.shape, length, width, height, img.dtype)
    ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    # 打印第一题的A的3个采样点和第二题A的3个采样点的RGB色值
    a11, a12, a13 = thresh[306, 82], thresh[308, 86], thresh[310, 91]
    a21, a22, a23 = thresh[306, 106], thresh[308, 113], thresh[310, 117]
    print(a11, a12, a13)
    print(a21, a22, a23)
    # 将处理后的图片展示出来，按ESC关闭
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return HttpResponse("Hello, world.")
