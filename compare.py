import tkinter as tk
from tkinter import ttk
import time

# 创建主窗口
root = tk.Tk()
root.title("数据对比工具 - wsTel hj")
root.geometry('800x600')

# 设置主题风格
style = ttk.Style()
style.theme_use('clam')

# 颜色配置
bg_color = "#f0f0f0"
text_bg = "#ffffff"
button_bg = "#4CAF50"
button_fg = "white"

# 配置主窗口背景
root.configure(bg=bg_color)

# 创建主框架
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill=tk.BOTH, expand=True)

# 文本框 - 只用于数据输入和结果展示
text_font = ('Microsoft YaHei', 10)
enHj = tk.Text(main_frame, width=80, height=20, 
               font=text_font, bg=text_bg, 
               wrap=tk.WORD, padx=5, pady=5)
enHj.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

# 控制面板框架（包含按钮和提示）
control_panel = ttk.Frame(main_frame)
control_panel.pack(fill=tk.X, pady=5)

# 按钮框架
button_frame = ttk.Frame(control_panel)
button_frame.pack(side=tk.LEFT)

# 导入按钮
btn_import = ttk.Button(button_frame, text="导入数据", 
                       command=lambda: getData(), 
                       style='Accent.TButton')
btn_import.pack(side=tk.LEFT, padx=5, ipadx=20)

# 对比按钮
btn_compare = ttk.Button(button_frame, text="开始对比", 
                        command=lambda: compDate())
btn_compare.pack(side=tk.LEFT, padx=5, ipadx=20)

# 提示信息标签（放在按钮右侧）
info_label = ttk.Label(control_panel, text="就绪", 
                      foreground="#666666", 
                      font=('Microsoft YaHei', 9))
info_label.pack(side=tk.LEFT, padx=20)

# 全局变量 (从第二个文件移植)
text_contentall = []
str_arr = []
str_arr2 = ""
str_arr3 = []
str_arr4 = []
str_arr5 = ""
dictionary = {}

def show_info(message, color="#666666"):
    """显示提示信息到标签"""
    info_label.config(text=message, foreground=color)
    root.after(3000, lambda: info_label.config(text="就绪", foreground="#666666"))

def clear_text():
    """清空编辑框"""
    enHj.delete("0.0", "end")

# 从第二个文件移植的getData函数 (保持逻辑不变)
def getData():
    global text_contentall, str_arr, str_arr2, dictionary
    
    content = enHj.get("0.0", "end").strip()
    if not content:
        show_info("错误: 没有输入数据", "red")
        return
        
    # 处理数据 (保持第二个文件的处理逻辑)
    text_contentall = content.split("\n")
    # 删除最后一行（空行）
    if text_contentall and text_contentall[-1] == "":
        text_contentall.pop()
    
    # 去除每行的空格
    text_contentall = [line.replace(" ", "") for line in text_contentall]
    
    str_arr = [str(element) for element in text_contentall]
    
    # 创建字典 (关键逻辑)
    dictionary = {}
    for element in str_arr:
        # 使用第一个制表符分割的部分作为键
        key = element.split('\t')[0]
        dictionary[key] = element
    
    str_arr2 = '\n'.join(str_arr)
    
    # 显示提示信息 (使用第一个文件的UI功能)
    show_info(f"成功导入 {len(text_contentall)} 行数据", "green")
    # 清空编辑框，准备新输入
    clear_text()

# 从第二个文件移植的compDate函数 (保持逻辑不变)
def compDate():
    global str_arr3, str_arr4, str_arr5
    
    if not dictionary:
        show_info("错误: 请先导入数据", "red")
        return
        
    content = enHj.get("0.0", "end").strip()
    if not content:
        show_info("错误: 没有输入对比数据", "red")
        return
        
    # 处理对比数据 (保持第二个文件的处理逻辑)
    str_arr3 = content.split("\n")
    # 删除最后一行（空行）
    if str_arr3 and str_arr3[-1] == "":
        str_arr3.pop()
    
    # 去除每行的空格
    str_arr3 = [line.replace(" ", "") for line in str_arr3]
    
    str_arr4 = [] 
    for element in str_arr3:
        if element in dictionary:
            str_arr4.append(dictionary[element])
        else:
            str_arr4.append(element)
    
    str_arr5 = '\n'.join(str_arr4)
    
    # 显示对比结果
    clear_text()
    enHj.insert('0.0', str_arr5)
    
    # 计算匹配数量
    match_count = sum(1 for element in str_arr3 if element in dictionary)
    show_info(f"处理完成: 共处理 {len(str_arr3)} 行, 匹配 {match_count} 行", "green")

# 运行主循环aiss
root.mainloop()