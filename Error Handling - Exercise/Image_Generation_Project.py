import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
import openai as openai
import tkinter as tk

openai.api_key = "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"


def display_image(image_url):
    with urllib.request.urlopen(image_url) as url:
        image_date = url.read()

    image_stream = BytesIO(image_date)

    image = ImageTk.PhotoImage(Image.open(image_stream))

    image_label.configure(image=image)
    image_label.image = image


def get_image_url():
    response = openai.Image.create(
        prompt=input_field.get(),
        n=1,
        size="256x256"
    )

    image_url = response['data'][0]['url']

    return image_url


def render_image():
    try:
        image_url = get_image_url()
        input_field.delete(0, tk.END)
    except openai.error.InvalidRequestError:
        error_label = tk.Label(window, text="Prompt cannot be empty!", fg="red")
        error_label.place(x=175, y=50)
    else:
        display_image(image_url)


window = tk.Tk()
window.title("Image generator")  # name of the window
window.geometry("500x350")  # width x height

image_label = tk.Label(window)
image_label.place(x=125, y=70)

input_field = tk.Entry(window)
input_field.place(x=175, y=20)

generate_button = tk.Button(window, text="Generate", height=1, command=render_image)
generate_button.place(x=300, y=15)

window.mainloop()
