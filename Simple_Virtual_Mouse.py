from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import cv2
from pyautogui import *
import threading
import wmi
from tkinter.font import  Font

def image_filter_Blue(cropped_image):
    blur = cv2.GaussianBlur(cropped_image, (3, 3), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(hsv, np.array([94, 80, 2]), np.array([126, 255, 255]))
    kernel = np.ones((5, 5))
    dilation = cv2.dilate(mask2, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=1)
    filtered = cv2.GaussianBlur(erosion, (3, 3), 0)
    ret, thresh = cv2.threshold(filtered, 127, 255, 0)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours, hierarchy, thresh


def image_shape_s(contours, crop_image):
    contour = max(contours, key=lambda x: cv2.contourArea(x))
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)

    hull = cv2.convexHull(contour)
    drawing = np.zeros(crop_image.shape, np.uint8)
    cv2.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
    cv2.drawContours(drawing, [hull], -1, (0, 0, 255), 0)

    '''hull = cv2.convexHull(contour, returnPoints=False)
    defects = cv2.convexityDefects(contour, hull)

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(contour[s][0])
        end = tuple(contour[e][0])

        cv2.line(crop_image, start, end, [0, 255, 0], 2)'''
    return x, y


def image_filter_g(cropped_image):
    blur = cv2.GaussianBlur(cropped_image, (3, 3), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    mask2 = cv2.inRange(hsv, np.array([40, 40, 40]), np.array([70, 255, 255]))  # green
    # mask2 = cv2.inRange(hsv, np.array([25, 52, 72]), np.array([102, 255, 255]))
    # mask2 = cv2.inRange(hsv, np.array([31,0,255]), np.array([176,255,255]))

    kernel = np.ones((5, 5))
    dilation = cv2.dilate(mask2, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=1)
    filtered = cv2.GaussianBlur(erosion, (3, 3), 0)
    ret, thresh = cv2.threshold(filtered, 127, 255, 0)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours, hierarchy, thresh


def thread(x1=0, y1=0, x2=0, y2=0):
    try:
        pi = x2 - x1
        qi = y2 - y1
        p, q = position()
        if (p==0 and q==0):
            moveTo(945, 525)
        else:
            if pi > 15 and pi < 40 and qi < -10:
                click(p, q)
            else:
                if x2 == 0 or y2 == 0:
                    if x1 > 25 and x1 < 120 and y1 < 75:
                        if y1 <= 15:
                            q = q - 20
                            moveTo(p, q)                        # upq
                        else:
                            q = q - 6
                            moveTo(p, q)
                    elif x1 < 55 and y1 > 40 and y1 < 120:
                        if x1 <=20:
                            p = p - 20
                            moveTo(p, q)
                        else:
                            p = p - 6
                            moveTo(p, q)                         # left
                    elif x1 > 120 and y1 > 40 and y1 < 120:
                        if x1 > 160:
                            p = p + 20
                            moveTo(p, q)
                        else:
                            p = p + 6
                            moveTo(p, q)                        # right
                    elif x1 > 30 and x1 < 120 and y1 > 100:
                        if y1 > 150:
                            q = q + 20
                            moveTo(p, q)
                        else:
                            q = q + 6
                            moveTo(p, q)                        # down
                    elif x1 <= 20 and y1 <= 30:
                        q = q - 15 * 1.4142
                        p = p - 15 * 1.4142
                        moveTo(p, q)
                        # left up
                    elif x1 > 135 and y1 <= 30:
                        q = q - 15 * 1.4142
                        p = p + 15 * 1.4142
                        moveTo(p, q)                        # right up
                    elif x1 <= 20 and y1 > 130:
                        q = q + 15 * 1.4142
                        p = p - 15 * 1.4142
                        moveTo(p, q)                        # left down
                    elif x1 > 135 and y1 > 120:
                        q = q + 15 * 1.4142
                        p = p + 15 * 1.4142
                        moveTo(p, q)                        # rightdown'''
                else:
                    pass
    except:
        pass
root_=Tk()
root_.geometry("1000x600+100+100")
f1 = Font(family="Time New Roman", size=12, weight="bold", underline=1)
f2 = Font(family="Time New Roman", size=12, weight="bold")
f3 = Font(family="Time New Roman", size=10, weight="bold")
img1 = ImageTk.PhotoImage(Image.open("mouse.png"))
panel = Label(root_, image=img1).place(x=400 ,y=1)
def abc():
    u = ss1.get()
    p = ss2.get()
    if u == 'Kundan' and p == '       Singh':
        root_.destroy()
        root = Tk()
        root.geometry("210x210+1200+830")
        app = Frame(root, bg="white")
        app.place(x=1, y=1)
        lmain = Label(app)
        lmain.grid()
        camera = cv2.VideoCapture(1)
        def video_stream():
            p,q=position()
            try:
                ret, image = camera.read()
                image = cv2.flip(image, 1)
                cv2.rectangle(image, (400, 120), (600, 300), (0, 0, 255), 1)
                img_frame_right = image[120:320, 420:620]
                contours_fing, hierarchy_fing, thresh_fing = image_filter_Blue(img_frame_right)
                contours_fing_r, hierarchy_fing_r, thresh_fing_r = image_filter_g(img_frame_right)
                try:
                    p1, q1 = image_shape_s(contours_fing, img_frame_right)
                    if (p > 1890 and q > 1050) or (p > 1890 and q < 30) or (p < 15 and q > 1050) or (p in range(0,25) and q in range(0,30)):
                        moveTo(945, 525)
                    try:
                        p2, q2 = image_shape_s(contours_fing_r, img_frame_right)
                        t = threading.Thread(name='child', target=thread, args=(p1, q1, p2, q2,))
                        if not t.is_alive():
                            t.start()
                    except:
                        t = threading.Thread(name='child', target=thread, args=(p1, q1,))
                        if not t.is_alive():
                            t.start()
                except:
                    pass
                img = Image.fromarray(thresh_fing)
                imgtk = ImageTk.PhotoImage(image=img)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                lmain.after(1, video_stream)
            except:
                pass

        video_stream()
        # camera.release()
        root.attributes("-topmost", True)
        root.mainloop()
    elif u=='' and p=='':
        l4 = Label(root_, text="Please Enter the UserName and Passward         ", fg='brown', font=f3).place(x=1, y=470)
    else:
        l4 = Label(root_, text="Please Enter the Correct UserName and Passward", fg='brown', font=f3).place(x=1, y=470)
root_.title('Virtual Mouse')
l3 = Label(root_, text="Machine Learning ", fg='brown', font=f1).place(x=110, y=30)
l3 = Label(root_, text=" Virtual World Application: Virtual Mouse", fg='green', font=f1).place(x=1, y=80)
l3 = Label(root_, text="Enter Username and Password", fg='brown', font=f1).place(x=50, y=140)
l3 = Label(root_, text="Copyright @ Kundan Kumar ", fg='skyblue').place(x=750, y=550)
l1 = Label(root_, text='Username', fg='brown', font=f1).place(x=10, y=200)
l2 = Label(root_, text='Password', fg='brown', font=f1).place(x=10, y=260)
ss1 = StringVar()
ss2 = StringVar()
e1 = Entry(root_, textvariable=ss1,font=f2).place(x=135, y=200)
e2 = Entry(root_, textvariable=ss2, show='*',font=f2).place(x=135, y=260)
b=Button(root_,text='Login to Continue',command=abc,width=30,height=1,bg='green',font=f1,fg='white').place(x=10,y=330)
l4 = Label(root_, text="Message ", fg='brown', font=f1).place(x=150, y=390)
root_.mainloop()