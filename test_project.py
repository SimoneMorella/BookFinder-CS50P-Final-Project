from project import scraping, clean_info, download_image

def test_scraping():
    first_scrap = scraping("harry potter")
    assert isinstance(first_scrap, dict)
    second_scrap = scraping("fdsdf")
    assert second_scrap["totalItems"] == 0
    third_scrap = scraping("tyson fury")
    assert third_scrap["totalItems"] == 71

def test_clean_info():
    json1 = {'kind': 'books#volumes', 'totalItems': 0}
    assert clean_info(json1) == None

def test_download_image():
    url1 = "https://books.google.com/books/content?id=mVeDBAAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    url2 = "https://books.google.com/books/content?id=f57uDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    url3 = "Not avaliable"
    image, check = download_image(url1)
    image1, check1 = download_image(url2)
    image2, check2 = download_image(url3)
    assert check == True
    assert check1 == True
    assert check2 == False