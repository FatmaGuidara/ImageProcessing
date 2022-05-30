import ctypes
import os
from tkinter import *
from tkinter import filedialog, ttk
import numpy as np
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
from read_write_file import *
from histograms import *
from contrast import *
from filter import *
from thresholding import *
from binary_images_filters import *

ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = Tk()
ttk.Style().configure("TButton", justify=CENTER)
p1 = PhotoImage(file = 'icon.png')
root.iconphoto(False, p1)

# Global variables
gui_width = 1385
gui_height = 700
ip_file = ""
op_file = ""
original_img = None
modified_img = None
user_arg = None
popup = None
popup_input = None
density_global = 0
mean = 0
stdev = 0

root.title("Image processing")
root.minsize(gui_width, gui_height)


def set_user_arg():
    global user_arg
    user_arg = popup_input.get()
    popup.destroy()
    popup.quit()


def open_popup_input(text):
    global popup, popup_input
    popup = Toplevel(root)
    popup.resizable(False, False)
    popup.title("User Input")
    text_label = ttk.Label(popup, text=text, justify=LEFT)
    text_label.pack(side=TOP, anchor=W, padx=15, pady=10)
    popup_input = ttk.Entry(popup)
    popup_input.pack(side=TOP, anchor=NW, fill=X, padx=15)
    popup_btn = ttk.Button(popup, text="OK", command=set_user_arg).pack(pady=10)
    popup.geometry(f"400x{104+text_label.winfo_reqheight()}")
    popup_input.focus()
    popup.mainloop()


def draw_before_canvas():
    global original_img, ip_file, density_global, mean, stdev
    original_img, density = readImagePgm(ip_file)
    density_global = density
    original_img = np.matrix(original_img)
    img = ImageTk.PhotoImage(image=Image.fromarray(original_img))
    before_canvas.create_image(
        256,
        256,
        image=img,
        anchor="center",
    )
    before_canvas.img = img
    mean, stdev = mean_stdev(original_img)


def draw_after_canvas(mimg):
    global modified_img

    modified_img = Image.fromarray(mimg)
    img = ImageTk.PhotoImage(modified_img)
    after_canvas.create_image(
        256,
        256,
        image=img,
        anchor="center",
    )
    after_canvas.img = img


def load_file():
    global ip_file, mean, stdev
    ip_file = filedialog.askopenfilename(
        title="Open an image file",
        initialdir=".",
        filetypes=[("All Image Files", "*.*")],
    )
    draw_before_canvas()


def save_file():
    global ip_file, original_img, modified_img
    file_ext = os.path.splitext(ip_file)[1][1:]
    op_file = filedialog.asksaveasfilename(
        filetypes=[
            (
                f"{file_ext.upper()}",
                f"*.{file_ext}",
            )
        ],
        defaultextension=[
            (
                f"{file_ext.upper()}",
                f"*.{file_ext}",
            )
        ],
    )
    shape = np.shape(modified_img)
    writeImagePgm(modified_img, shape[1], shape[0], density_global, op_file)



# Pop up
def input_popup_satured():
    open_popup_input("Enter min,max\n(Separate inputs with a comma)")  # user input
    arg_list = user_arg.replace(" ", "").split(",")
    min, max = int(arg_list[0]), int(arg_list[1])
    return min, max

def input_popup_thres():
    global user_arg
    open_popup_input("Enter threshold\n")  # user input
    user_arg = int(user_arg)
    return user_arg

def open_popup_mean():
   top= Toplevel(root)
   top.geometry("500x200")
   top.title("Mean")
   Label(top, text= f'{mean}', font=('Arial 18 bold')).place(x=100,y=80)

def open_popup_stdev():
   top= Toplevel(root)
   top.geometry("500x200")
   top.title("Standard Deviation")
   Label(top, text= f'{stdev}', font=('Arial 18 bold')).place(x=100,y=80)

def open_popup_snr_median():
    output = filer_median(original_img)
    snr = signal_to_Noise_Ratio(original_img, output)
    top= Toplevel(root)
    top.geometry("500x200")
    top.title("SNR / Median Filter")
    Label(top, text= f'{snr}', font=('Arial 18 bold')).place(x=100,y=80)

    
def open_popup_snr_avg():
    output = filer_moy(original_img)
    snr = signal_to_Noise_Ratio(original_img, output)
    top= Toplevel(root)
    top.geometry("500x200")
    top.title("SNR / Average Filter")
    Label(top, text= f'{snr}', font=('Arial 18 bold')).place(x=100,y=80)
    


# frames
left_frame = ttk.LabelFrame(root, text="Original Image", labelanchor=N)
left_frame.pack(fill=BOTH, side=LEFT, padx=10, pady=10, expand=1)

middle_frame = ttk.LabelFrame(root, text="Algorithms", labelanchor=N)
middle_frame.pack(fill=BOTH, side=LEFT, padx=5, pady=10)

right_frame = ttk.LabelFrame(root, text="Modified Image", labelanchor=N)
right_frame.pack(fill=BOTH, side=LEFT, padx=10, pady=10, expand=1)

# left frame contents
before_canvas = Canvas(left_frame, bg="white", width=512, height=512)
before_canvas.pack(expand=1)


# mean, stdev = mean_stdev(original_img)


browse_btn = ttk.Button(left_frame, text="Browse", command=load_file)
browse_btn.pack(expand=1, anchor=SW, pady=(5, 0))

# middle frame contents
algo_canvas = Canvas(middle_frame, width=260, highlightthickness=0)
scrollable_algo_frame = Frame(algo_canvas)
scrollbar = Scrollbar(
    middle_frame, orient="vertical", command=algo_canvas.yview, width=15
)
scrollbar.pack(side="right", fill="y")
algo_canvas.pack(fill=BOTH, expand=1)
algo_canvas.configure(yscrollcommand=scrollbar.set)
algo_canvas.create_window((0, 0), window=scrollable_algo_frame, anchor="nw")
scrollable_algo_frame.bind(
    "<Configure>", lambda _: algo_canvas.configure(scrollregion=algo_canvas.bbox("all"))
)


# right frame contents
after_canvas = Canvas(right_frame, bg="white", width=512, height=512)
after_canvas.pack(expand=1)

save_btn = ttk.Button(right_frame, text="Save", command=save_file)
save_btn.pack(expand=1, anchor=SE, pady=(5, 0))


def plot_histograms():
    hist = histogram(original_img)
    hist_c = histogram_cummulated(hist)
    plt.figure(figsize=(10,5)) 
    plt.subplot(1,2,1)
   
    plt.bar(range(256), hist)
    plt.xlabel('Graylevel / intensity')
    plt.ylabel('Frequency')   
   
    plt.title('Histogram')
    # plt.tight_layout()

    plt.subplot(1,2,2)
    
    plt.bar(range(256), hist_c)
    plt.xlabel('Graylevel / intensity')

    
    plt.title('Histogram Cumulative')
    # plt.tight_layout()
    
    plt.show()

def plot_histograms_eq():
    hist = histogram(original_img)
    matrix_eq = histogram_equalization(original_img)
    hist_2 = histogram(matrix_eq)

    plt.figure(figsize=(10,5)) 
    plt.subplot(1,2,1)
   
    plt.bar(range(256), hist)
    plt.xlabel('Graylevel / intensity')
    plt.ylabel('Frequency')   
   
    plt.title('Histogram')
    # plt.tight_layout()

    plt.subplot(1,2,2)
    
    plt.bar(range(256), hist_2)
    plt.xlabel('Graylevel / intensity')

    
    plt.title('Histogram Equalization')
    # plt.tight_layout()
    draw_after_canvas(matrix_eq)
    plt.show()

def linear_transformations():
    output = linear_transformation(original_img)
    draw_after_canvas(output)

def saturated_transformations():
    min, max = input_popup_satured()
    output = saturated_transformation(original_img, min, max)
    draw_after_canvas(output)
    
def noising():
    output = noise(original_img)
    draw_after_canvas(output)
    
def mean_filter():
    output = filer_moy(original_img)
    draw_after_canvas(output)
    
def median_filter():
    output = filer_median(original_img)
    draw_after_canvas(output)  

def thresholdings():
    thres = input_popup_thres()
    output = thresholding(original_img, thres)
    draw_after_canvas(output)  
    
def otsu_thres():
    output = otsu(original_img)
    draw_after_canvas(output) 
    
def dilatations():
    output = dilatation(original_img)
    draw_after_canvas(output) 
    
def erosions():
    output = erosion(original_img)
    draw_after_canvas(output)    
  
def ouverture():
    output = opening(original_img)
    draw_after_canvas(output) 
    
def fermeture():
    output = closing(original_img)
    draw_after_canvas(output)    
      
    
# algorithm btns
ttk.Button(
    scrollable_algo_frame, text="Show Histograms", width=30, command=plot_histograms
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Show Histograms Equalization", width=30, command=plot_histograms_eq
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Linear Transformation", width=30, command=linear_transformations
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Satured Transformation", width=30, command=saturated_transformations
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Noise", width=30, command=noising
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Mean Filer", width=30, command=mean_filter
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Median Filter", width=30, command=median_filter
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Thresholing", width=30, command=thresholdings
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Otsu", width=30, command=otsu_thres
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Dilatation", width=30, command=dilatations
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Erosion", width=30, command=erosions
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Ouverture", width=30, command=ouverture
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Fermeture", width=30, command=fermeture
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Mean", width=30, command=open_popup_mean
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="Standard Deviation", width=30, command=open_popup_stdev
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="SNR / Median Filter", width=30, command=open_popup_snr_median
).pack(expand=1, padx=5, pady=2, ipady=2)

ttk.Button(
    scrollable_algo_frame, text="SNR / Average Filter", width=30, command=open_popup_snr_avg
).pack(expand=1, padx=5, pady=2, ipady=2)

root.mainloop()
