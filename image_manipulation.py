from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk, ImageEnhance, ImageFilter, ImageOps
from tkinter import filedialog, messagebox

root = CTk()
root.geometry("1366x768")
space = " " * 205
root.title(f"{space}Image Manipulation")
set_appearance_mode("dark")

def showbuttons():
    # BUTTONS

    save_btn = CTkButton(root, text='Save', width=25, command=save)
    save_btn.place(x=1320, y=675)

    blur_btn = CTkButton(root, text="Blur", command=blur_slide)
    blur_btn.place(x=3, y=10)

    contrast_btn = CTkButton(root, text="Contrast", command=contrast_slide)
    contrast_btn.place(x=3, y=40)

    bright_btn = CTkButton(root, text="Brightness", command=bright_slide)
    bright_btn.place(x=3, y=70)

    resize_btn = CTkButton(root, text="Resize", command=lambda: resize(0))
    resize_btn.place(x=3, y=100)

    invert_btn = CTkButton(root, text="Invert", command=lambda: invert(20))
    invert_btn.place(x=3, y=130)

    palette_btn = CTkButton(root, text="Palette", command=pallete)
    palette_btn.place(x=3, y=160)

    sharp_btn = CTkButton(root, text="Sharpness", command=sharp_slide)
    sharp_btn.place(x=3, y=190)

    rotate_btn = CTkButton(root, text="Rotate", command=lambda: rotate(0))
    rotate_btn.place(x=3, y=220)

    enhance_btn = CTkButton(root, text="Color Enhance", command=enhance_slide)
    enhance_btn.place(x=3, y=250)

    cenhance_btn = CTkButton(root, text="Contrast Enhancer", command=cenhance_slide)
    cenhance_btn.place(x=3, y=280)

    contour_btn = CTkButton(root, text="Contour", command=image_contour)
    contour_btn.place(x=3, y=310)

    emboss_btn = CTkButton(root, text="Emboss", command=image_emboss)
    emboss_btn.place(x=3, y=340)

    smooth_btn = CTkButton(root, text="Smooth", command=image_smooth)
    smooth_btn.place(x=3, y=370)

    red_btn = CTkButton(root, text="Red Channel", command=red_channel)
    red_btn.place(x=3, y=400)

    blue_btn = CTkButton(root, text="Blue Channel", command=blue_channel)
    blue_btn.place(x=3, y=430)

    green_btn = CTkButton(root, text="Green Channel", command=green_channel)
    green_btn.place(x=3, y=460)

    solarize_btn = CTkButton(root, text="Solarize", command=solarize_slide)
    solarize_btn.place(x=3, y=490)

    flip_btn = CTkButton(root, text="Flip", command=flip)
    flip_btn.place(x=3, y=520)

    colorize_btn = CTkButton(root, text="Colorize", command=colorize)
    colorize_btn.place(x=3, y=550)

    border_btn = CTkButton(root, text="Border", command=lambda: border(0))
    border_btn.place(x=3, y=580)

    pad_btn = CTkButton(root, text="Pad", command=lambda: pad(0))
    pad_btn.place(x=3, y=610)

    unsharp_btn = CTkButton(root, text="Unsharp", command=unsharp_slide)
    unsharp_btn.place(x=3, y=640)

    mirror_btn = CTkButton(root, text="Mirror", command=mirror)
    mirror_btn.place(x=3, y=670)

    apply_btn = CTkButton(root, text="Apply", command=apply)
    apply_btn.place(x=1170, y=675)

def open_image():
    global image, panel
    root.filename = filedialog.askopenfilename(title="Select a file", filetypes=(("JPG", "*.jpg"), ("PNG", "*.png")))
    image = Image.open(root.filename)
    panel = Label(root, bd=0)
    panel.place(relx=0.5, rely=0.5, anchor=CENTER)
    showimage(image)
    l_logo.place_forget()
    open_img.place_forget()
    showbuttons()

l_logo = CTkLabel(root, text="Image Manipulation", font=("Lucida Console", 40))
l_logo.place(x=680, y=250, anchor=N)

file_image = CTkImage(
    Image.open("openfile.png").resize((20, 20), Image.LANCZOS))

open_img = CTkButton(root, text="Open Image", image=file_image, compound="left", command=open_image)
open_img.place(relx=0.5, rely=0.5, anchor=CENTER)

def showimage(img):
    dispimage = ImageTk.PhotoImage(img)
    panel.configure(image=dispimage)
    panel.image = dispimage

def save():
    file = filedialog.asksaveasfile(defaultextension=".png", filetypes=(("JPG", "*.jpg"), ("PNG", "*.png")))
    if file:
        outputImage.save(file)
        messagebox.showinfo("Image Manipulation", "Your image has been saved!")

def apply():
    global image, outputImage
    image = outputImage.copy()
    showimage(image)

def resize(x):
    global outputImage, resize_btn
    sizes = [(780, 700), (950, 500), (800, 500), (900, 800), (500, 600), (500, 300), (800, 500), (874, 1240)]
    size_index = x % len(sizes)
    outputImage = image.resize(sizes[size_index])
    resize_btn = CTkButton(root, text="Resize", command=lambda: resize(x + 1)).place(x=3, y=100)
    showimage(outputImage)

def contrast_enhancer(x):
    global outputImage
    contrast_enhance = ImageEnhance.Contrast(image)
    outputImage = contrast_enhance.enhance(x)
    showimage(outputImage)


# SLIDERS

bright_click = 0
sharp_click = 0
blur_click = 0
contrast_click = 0
enhance_click = 0
cenhance_click = 0
unsharp_click = 0
solarize_click = 0
pad_click = 0
gauss_click = 0


def bright_slide():
    global brightslide, bright_click
    bright_click += 1
    if bright_click % 2 == 0:
        brightslide.place_forget()
    else:
        brightslide = CTkSlider(root, from_=0, to=5, command=brightness)
        brightslide.place(x=150, y=75)


def sharp_slide():
    global sharpslide, sharp_click
    sharp_click += 1
    if sharp_click % 2 == 0:
        sharpslide.place_forget()
    else:
        sharpslide = CTkSlider(root, from_=0, to=20, command=sharpness)
        sharpslide.place(x=150, y=195)


def blur_slide():
    global blurslide, blur_click
    blur_click += 1
    if blur_click % 2 == 0:
        blurslide.place_forget()
    else:
        blurslide = CTkSlider(root, from_=0, to=20, command=image_blur)
        blurslide.place(x=150, y=15)


def contrast_slide():
    global contrastslide, contrast_click
    contrast_click += 1
    if contrast_click % 2 == 0:
        contrastslide.place_forget()
    else:
        contrastslide = CTkSlider(root, from_=0, to=5, command=contrast)
        contrastslide.place(x=150, y=45)


def enhance_slide():
    global enhanceslide, enhance_click
    enhance_click += 1
    if enhance_click % 2 == 0:
        enhanceslide.place_forget()
    else:
        enhanceslide = CTkSlider(root, from_=0, to=20, command=color_enhance)
        enhanceslide.place(x=150, y=255)


def cenhance_slide():
    global cenhanceslide, cenhance_click
    cenhance_click += 1
    if cenhance_click % 2 == 0:
        cenhanceslide.place_forget()
    else:
        cenhanceslide = CTkSlider(root, from_=0, to=20, command=contrast_enhancer)
        cenhanceslide.place(x=150, y=285)


def unsharp_slide():
    global unsharpslide, unsharp_click
    unsharp_click += 1
    if unsharp_click % 2 == 0:
        unsharpslide.place_forget()
    else:
        unsharpslide = CTkSlider(root, from_=0, to=70, command=image_unsharp)
        unsharpslide.place(x=150, y=645)


def solarize_slide():
    global solarizeslide, solarize_click
    solarize_click += 1
    if solarize_click % 2 == 0:
        solarizeslide.place_forget()
    else:
        solarizeslide = CTkSlider(root, from_=30, to=90, command=solarize)
        solarizeslide.place(x=150, y=495)


# FUNCTIONS

mirror_click = 0
flip_click = 0


def brightness(x):
    global outputImage
    brightness_enhance = ImageEnhance.Brightness(image)
    outputImage = brightness_enhance.enhance(x)
    showimage(outputImage)


def sharpness(x):
    global outputImage
    sharp_enhance = ImageEnhance.Sharpness(image)
    outputImage = sharp_enhance.enhance(x)
    showimage(outputImage)


def image_blur(x):
    global outputImage
    outputImage = image.filter(ImageFilter.BoxBlur(radius=x))
    showimage(outputImage)


def image_contour():
    global outputImage
    outputImage = image.filter(ImageFilter.CONTOUR)
    showimage(outputImage)


def image_emboss():
    global outputImage
    outputImage = image.filter(ImageFilter.EMBOSS)
    showimage(outputImage)


def image_smooth():
    global outputImage
    outputImage = image.filter(ImageFilter.SMOOTH)
    showimage(outputImage)


def image_unsharp(x):
    global outputImage
    outputImage = image.filter(ImageFilter.UnsharpMask(radius=x))
    showimage(outputImage)


def red_channel():
    global outputImage
    outputImage = image.getchannel('R')
    showimage(outputImage)


def green_channel():
    global outputImage
    outputImage = image.getchannel('G')
    showimage(outputImage)


def blue_channel():
    global outputImage
    outputImage = image.getchannel('B')
    showimage(outputImage)


def pallete():
    global outputImage
    outputImage = image.convert('P')
    showimage(outputImage)


def contrast(x):
    global outputImage
    outputImage = ImageOps.autocontrast(image=image, cutoff=x)
    showimage(outputImage)


def invert(x):
    global outputImage
    outputImage = ImageOps.invert(image=image)
    showimage(outputImage)


def solarize(x):
    global outputImage
    outputImage = ImageOps.solarize(image=image, threshold=x)
    showimage(outputImage)


def posterize(x):
    global outputImage
    outputImage = ImageOps.posterize(image=image, bits=x)
    showimage(outputImage)


def mirror():
    global outputImage, mirror_click
    mirror_click += 1
    if mirror_click % 2 == 0:
        outputImage = ImageOps.mirror(outputImage)
        showimage(outputImage)
    else:
        outputImage = ImageOps.mirror(image)
        showimage(outputImage)


def flip():
    global outputImage, flip_click
    flip_click += 1
    if flip_click % 2 == 0:
        outputImage = ImageOps.flip(outputImage)
        showimage(outputImage)
    else:
        outputImage = ImageOps.flip(image)
        showimage(outputImage)


def colorize():
    global outputImage
    outputImage = ImageOps.colorize(image=image.convert('L'), black='white', white='blue')
    showimage(outputImage)


def border(x):
    global outputImage, border_btn
    borders = [(210, 105, 30), (72, 61, 139), (56, 89, 107), (32, 180, 170), (5, 145, 200), (100, 100, 100),
               (135, 206, 250), (0, 0, 0), (255, 255, 255), (245, 145, 145), (45, 50, 79), (89, 0, 0), (0, 80, 90),
               (0, 244, 0), (245, 0, 0), (145, 145, 145), (35, 35, 35)]
    outputImage = ImageOps.expand(image=image, border=200, fill=borders[x % len(borders)])
    border_btn = CTkButton(root, text="Border", command=lambda: border(x + 1)).place(x=3, y=580)
    showimage(outputImage)


def pad(x):
    pads = [(600, 600), (800, 600), (900, 600), (500, 500), (800, 400), (800, 300), (700, 700), (900, 600), (700, 500),
            (800, 500), (500, 500), (900, 900), (700, 700), (600, 600), (800, 600), (900, 600), (500, 500), (800, 400),
            (800, 300), (700, 700), (900, 600), (700, 500), (800, 500), (500, 500), (900, 900), (700, 700)]
    global outputImage, pad_btn
    outputImage = ImageOps.pad(image=image, size=pads[x % len(pads)])
    pad_btn = CTkButton(root, text="Pad", command=lambda: pad(x + 1)).place(x=3, y=610)
    showimage(outputImage)


root.mainloop()