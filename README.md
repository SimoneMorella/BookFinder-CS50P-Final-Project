# BookFinder-CS50P-Final-Project
    #### Video Demo:  <https://youtu.be/EVpPzOVMqfU>
    #### Description:
    This is my final project for CS50P. It is a Windows app that uses Google Books API
    to find information about any book based on the user input. The front-end is made with
    the Tkinter Python library. About bugs and testing I created enough exceptions to make the
    code run smoothly without any of the biggest problems (like if some jsons don't have some dict keys).
    There are other exceptions that I have considered: like the one about the connection error for the requests,
    the query of an input that does not return any books, and the consequent response of a creation of a
    "No results founded" box.
    The tkinter front-end part was especially challenging because it is such a non-intuitive way of doing front-end.
    I would have prefered to do a webpage with html, css and js but I wanted to implent a full python program for the
    sake of the course.
    Although the front-end is especially poorly made from an aesthetic point of view, I learnt a lot about new Python
    functionalities.
    In the other test_books.py file there are 3 pytest tests to check the integrity of the code.
    Like the test of the download image function, of the scraping function and of the clean scraped info data.
    Cleaning the json indeed, was not easy as the resulting json from the scraping was a dictionary with nested inside it
    other dictionaries and lists. It was pretty messy but I managed to make it as much readable as possible.
    I hope you like my project even though it has many limitations especially on the front-end part!
    
    Check the code for info and further explanations.
    Thanks again for this amazing course!
