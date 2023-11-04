import requests, sys
import json
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

def main():
    create_ui()

## function to scrap data from the google books api. language always eng in the search
def scraping(term):
    try:
        api_key = "AIzaSyB8ddUrlCLZtrkaXcw60902ijbG3ZDMG5A"
        r = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=intitle:{term}&maxResults=4&langRestrict=en&projection=lite&key={api_key}")
        json_file = r.json()
        # json_formatted = json.dumps(json_file, indent=4)
        # print(json_formatted)
        return json_file
    except requests.RequestException:
        sys.exit("Connection Failure")

##function to get the correct data like title, author year
def clean_info(json):
    books = []
    try:
        for items in json["items"]:
            try:
                title = items["volumeInfo"]["title"]
            except KeyError:
                title = "Title not avaliable"
            try:
                authors_list = items["volumeInfo"]["authors"]
                authors = ', '.join(authors_list)
            except KeyError:
                authors = "Authors not avaliable"
            try:
                publish_date = items["volumeInfo"]["publishedDate"]
            except KeyError:
                publish_date = "Date not avaliable"
            try:
                description_list = items["volumeInfo"]["description"].split(".")
                if len(description_list) >= 2:
                    description = ". ".join(description_list[:2]) + "."
                else:
                    description = f"{description_list[0]}"

            except KeyError:
                description = "Description not avaliable"
            try:
                imagelink = items["volumeInfo"]["imageLinks"]["smallThumbnail"]
            except KeyError:
                imagelink = "Not avaliable"
            books.append({
                        "title": title,
                        "authors": authors, 
                        "date": publish_date, 
                        "description": description, 
                        "imagelink": imagelink
                        })  
        return books
    except KeyError:
        return None
  
##function to download the image
def download_image(url):
    if url == "Not avaliable":
        return None, False
    response = requests.get(url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        return image, True
    return None, False

## function to create tkinter windows and start the search
def create_ui():
    def create_book_widget(book, row):
        frame = tk.Frame(canvas, bd=2, relief=tk.RAISED, bg="#FFDAB9", width=1000)
        frame.grid(row=row, sticky="nsew", padx=10, pady=10)

        #here image load
        image, check = download_image(book['imagelink'])
        if image:
            image.thumbnail((50, 150))
            image_tk = ImageTk.PhotoImage(image)
            image_label = tk.Label(frame, image=image_tk)
            image_label.image = image_tk
            image_label.grid(row=0, column=0, padx=10, pady=10, rowspan=4)

        #other elements in column next to the image
        title_label = tk.Label(frame, text=f"Title: {book['title']}", bg="#FFDAB9", fg="#333333")
        title_label.grid(row=0, column=1, sticky="w")
        
        author_label = tk.Label(frame, text=f"Author: {book['authors']}", bg="#FFDAB9", fg="#333333")
        author_label.grid(row=1, column=1, sticky="w")

        date_label = tk.Label(frame, text=f"Publish Date: {book['date']}", bg="#FFDAB9", fg="#333333")
        date_label.grid(row=2, column=1, sticky="w")

        description_label = tk.Label(frame, text=f"Description: {book['description']}", bg="#FFDAB9", fg="#333333", wraplength=950)
        description_label.grid(row=3, column=1, sticky="w")

    def create_no_results_label():
        for widget in canvas.winfo_children():
            widget.destroy()
        no_results_label = tk.Label(canvas, text="No results found.", bg=background_color, fg=text_color, font=("Arial", 16))
        no_results_label.pack()

## function to deploy the search results
    def display_books():
        search_term = search_bar.get()
        if not search_term:
            for widget in canvas.winfo_children():
                widget.destroy()

            canvas.delete("all")
            create_no_results_label()
        else:
            canvas.delete("all")
            for widget in canvas.winfo_children():
                widget.pack_forget()
            infos = scraping(search_term)
            # print(infos)
            if infos:
                books_info = clean_info(infos)
                # print(books_info)
                if not books_info:
                    create_no_results_label()
                else:
                    for i, book in enumerate(books_info):
                        create_book_widget(book, i)
            else:
                create_no_results_label()

    #create root window
    root = tk.Tk()
    root.title("BookFinder")
    root.geometry("1080x720")
    root.resizable(False, False)

    #colors and fonts
    background_color = "#FFDAB9"
    text_color = "#333333"

    #create elements in the window
    root.configure(bg=background_color)
    title = tk.Label(root, text="BookFinder", bg=background_color, font=("Arial", 24, "bold"), fg=text_color)
    title.pack(pady=10)
    frame = tk.Frame(root, bg=background_color)
    frame.pack(pady=10)
    search_label = tk.Label(frame, text="Insert book info:",bg=background_color, fg=text_color)
    search_label.pack(side=tk.LEFT, padx=5)
    search_bar = tk.Entry(frame, font=("Arial", 12), width=30)
    search_bar.pack(side=tk.LEFT, padx=5)
    search_button = tk.Button(frame, text="Search", bg="#6495ED", fg="white", font=("Arial", 12, "bold"), command=display_books)
    search_button.pack(side=tk.LEFT, padx=5)
    canvas = tk.Canvas(root, width=1037, height=520, bg=background_color)
    canvas.pack()

    root.mainloop()


if __name__ == "__main__":
    main()