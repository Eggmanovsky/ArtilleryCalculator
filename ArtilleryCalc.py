import tkinter as tk
from tkinter import simpledialog

from PIL import Image, ImageTk, ImageDraw

import pyautogui

from math import sqrt

class ScreenshotDrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screenshot Draw and Calculate Distance")

        # 获取用户输入的 Scale 和 pixle 值
        self.scale = simpledialog.askstring("Input Scale", "Enter the Scale value:")
        self.pixle = simpledialog.askstring("Input Pixle", "Enter the Pixle value:")
        
        # 确保输入的是有效的数字
        if not (self.scale and self.pixle and self.scale.isdigit() and self.pixle.isdigit()):
            self.root.destroy()  # 如果输入无效，关闭程序
            raise ValueError("Invalid input. Both Scale and Pixle should be numbers.")

        self.scale = float(self.scale)
        self.pixle = float(self.pixle)

        # 截取屏幕截图
        self.screenshot = pyautogui.screenshot()
        self.original_image = None  # 不再需要保存原始截图

        # 将截图转换为Tkinter可以显示的格式
        self.tk_image = ImageTk.PhotoImage(self.screenshot.resize((1366, 768), Image.LANCZOS))

        # 创建画布
        self.canvas = tk.Canvas(root, width=1366, height=768)
        self.canvas.pack()

        # 将截图放置在画布上（作为背景）
        self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        self.points = []
        self.is_drawing = False

        # 绑定鼠标事件
        self.canvas.bind("<Button-1>", self.on_click)

        # 添加重新截图按钮，并移动到窗口左上角
        self.retake_button = tk.Button(root, text="Retake Screenshot", command=self.retake_screenshot)
        self.retake_button.place(x=1200, y=10, width=150, height=30)  # 设定按钮的位置和大小

        # 用于显示距离的文本对象
        self.distance_text_id = None

    def on_click(self, event):
        # 将点击位置从画布坐标转换为截图坐标
        x_screenshot = int(event.x * self.screenshot.width / 1366)
        y_screenshot = int(event.y * self.screenshot.height / 768)

        if len(self.points) < 2:
            # 在截图上绘制点
            draw = ImageDraw.Draw(self.screenshot)
            draw.ellipse((x_screenshot-5, y_screenshot-5, x_screenshot+5, y_screenshot+5), fill='red')

            # 更新Tkinter显示的图像
            self.tk_image = ImageTk.PhotoImage(self.screenshot.resize((1366, 768), Image.LANCZOS))
            self.canvas.itemconfig(self.canvas_image, image=self.tk_image)

            self.points.append((x_screenshot, y_screenshot))

            self.update_distance()

    def update_distance(self):
        if len(self.points) == 2:
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            # 计算距离，这里使用用户输入的 Scale 和 pixle 值
            distance = sqrt((x2 - x1)**2 + (y2 - y1)**2) * (self.scale / self.pixle)
            distance_str = f"Distance: {distance:.2f} Meters"  # 假设单位为任意单位，根据实际需求修改

            # 更新或创建显示距离的文本对象，并设置字体颜色为红色
            if self.distance_text_id:
                self.canvas.delete(self.distance_text_id)  # 删除旧的文本对象
            self.distance_text_id = self.canvas.create_text(10, 10, anchor=tk.NW, text=distance_str, font=("Helvetica", 16), fill='red')

    def retake_screenshot(self):
        # 重新截取屏幕截图
        self.screenshot = pyautogui.screenshot()
        self.tk_image = ImageTk.PhotoImage(self.screenshot.resize((1366, 768), Image.LANCZOS))
        self.canvas.itemconfig(self.canvas_image, image=self.tk_image)

        # 清除所有绘制的点和距离文本对象
        self.points = []
        if self.distance_text_id:
            self.canvas.delete(self.distance_text_id)
            self.distance_text_id = None  # 重置文本对象ID

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotDrawApp(root)

    root.mainloop()