import tkinter as tk
from tkinter import ttk, filedialog
import PIL
from PIL import Image, ImageFilter, ImageOps
import os

image_filetype = [('pngfile', '*.png'), ('jpegfile', '*.jpg *.jpeg')]

startwin = tk.Tk()
startwin.geometry("500x400")

style = ttk.Style()
style.configure("yomikomi.TButton", font = ("", 50))
style.configure("menu.TRadiobutton", font = ("", 20))

def yomikomi_def():
    global file
    filename = filedialog.askopenfilename(title = "画像ファイルを開く", filetype = image_filetype)
    file = Image.open(filename)
    startwin_canvas.place_forget()
    main_canvas = tk.Canvas(width = 500, height = 400)
    main_canvas.place(x = 0, y = 0)
    menu_dore = tk.IntVar()
    menu_akaruku = ttk.Radiobutton(main_canvas, value = 0, variable = menu_dore, text = "明るくする", style = "menu.TRadiobutton")
    menu_kuraku = ttk.Radiobutton(main_canvas, value = 1, variable = menu_dore, text = "暗くする", style = "menu.TRadiobutton")
    menu_mozaiku = ttk.Radiobutton(main_canvas, value = 2, variable = menu_dore, text = "モザイク", style = "menu.TRadiobutton")
    menu_jouge = ttk.Radiobutton(main_canvas, value = 3, variable = menu_dore, text = "上下反転", style = "menu.TRadiobutton")
    menu_sayuu = ttk.Radiobutton(main_canvas, value = 4, variable = menu_dore, text = "左右反転", style = "menu.TRadiobutton")
    menu_gray = ttk.Radiobutton(main_canvas, value = 5, variable = menu_dore, text = "モノクロ", style = "menu.TRadiobutton")
    menu_nichika = ttk.Radiobutton(main_canvas, value = 6, variable = menu_dore, text = "2値化", style = "menu.TRadiobutton")
    menu_heikinka = ttk.Radiobutton(main_canvas, value = 7, variable = menu_dore, text = "平均化", style = "menu.TRadiobutton")
    menu_90do = ttk.Radiobutton(main_canvas, value = 8, variable = menu_dore, text = "90度", style = "menu.TRadiobutton")
    menu_180do = ttk.Radiobutton(main_canvas, value = 9, variable = menu_dore, text = "180度", style = "menu.TRadiobutton")
    menu_270do = ttk.Radiobutton(main_canvas, value = 10, variable = menu_dore, text = "270度", style = "menu.TRadiobutton")
    menu_akaruku.place(x = 10, y = 10)
    menu_kuraku.place(x = 10, y = 50)
    menu_mozaiku.place(x = 10, y = 90)
    menu_jouge.place(x = 10, y = 130)
    menu_sayuu.place(x = 210, y = 10)
    menu_gray.place(x = 210, y = 50)
    menu_nichika.place(x = 210, y = 90)
    menu_heikinka.place(x = 210, y = 130)
    menu_90do.place(x = 10, y = 170)
    menu_180do.place(x = 210, y = 170)
    menu_270do.place(x = 10, y = 210)
    def kanryo():
        global file
        hozon_basho = tk.filedialog.asksaveasfilename(title = "画像を保存", filetype = image_filetype)
        if hozon_basho.endswith(".png"):
            file = file.convert("RGBA")
        elif hozon_basho.endswith(".jpg") or hozon_basho.endswith(".jpeg"):
            file = file.convert("RGB")
        else:
            hozon_basho = hozon_basho + os.path.splitext(filename)[1]
        kanse_dousa = menu_dore.get()
        if kanse_dousa == 0:
            file = file.point(lambda x: x * 1.5)
        if kanse_dousa == 1:
            file = file.point(lambda x: x * 0.5)
        if kanse_dousa == 2:
            file = file.filter(ImageFilter.GaussianBlur(4))
            file.resize([x // 8 for x in file.size]).resize(file.size)
        if kanse_dousa == 3:
            file = ImageOps.flip(file)
        if kanse_dousa == 4:
            file = ImageOps.flip(file)
        if kanse_dousa == 5:
            file = file.convert("LA")
        if kanse_dousa == 6:
            file = file.convert("L")
            file = file.point(lambda x: 0 if x < 230 else x)
        if kanse_dousa == 7:
            file = ImageOps.equalize(file)
        if kanse_dousa == 8:
            file = file.rotate(90, expand = True)
        if kanse_dousa == 9:
            file = file.rotate(180, expand = True)
        if kanse_dousa == 10:
            file = file.rotate(270, expand = True)
        file.save(hozon_basho)
        main_canvas.place_forget()
        saigo_canvas = tk.Canvas(width = 500, height = 400)
        saigo_canvas.place(x = 0, y = 0)
        saigo_label = ttk.Label(saigo_canvas, text = "できました")
        saigo_label.pack()
        saigo_show_button = ttk.Button(saigo_canvas, text = "画像を表示", command = file.show)
        saigo_show_button.pack()
        def yarinaosi():
            saigo_canvas.place_forget()
            startwin_canvas.place(x = 0, y = 0)
        saigo_owari_button = ttk.Button(saigo_canvas, text = "もう一度", command = yarinaosi)
        saigo_owari_button.pack()
    mainwin_button = ttk.Button(main_canvas, text = "完了", command = kanryo)
    mainwin_button.place(x = 210, y = 210)
    
startwin_canvas = tk.Canvas(width = 500, height = 400)
startwin_canvas.place(x = 0, y = 0)

startwin_button = ttk.Button(startwin_canvas, text = "読み込み", command = yomikomi_def, style = "yomikomi.TButton")
startwin_button.place(height = 300, width = 400, x = 50, y = 50)

startwin.mainloop()
