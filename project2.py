## SI 206 W19 - Project 2

## COMMENT HERE WITH:
## Your name:
###########

## Import statements
import unittest
import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import os

## PART 1  - Complete grab_headlines
## INPUT: soup - the soup object to process
## Grab the headlines from the "Most Read" section
## and return them in a list
def grab_headlines(soup):

    # get the most read div

    # get the ordered list from that div

    # get the links from the ordered list div
    
    # return the headlines
    
    pass

## PART 2 Complete a function called get_headline_dict. It will take a soup object and return a dictionary
## with each story headline as a key and each story url as the value
## INPUT: soup - the soup object
## OUTPUT: Return - a dictionary with each story headline as the key and the story url as the value
def get_headline_dict(soup):

    # create the empty dictionary

    # get the story wrap divs

        # get the short headline

        # find the link

        # set the dictionary key to the headline and the url as the value

    # return the dictionary

    pass

## PART 3 Define a function called get_page_info. It will take a soup object for a story
## and return a tuple with the title, author, date, and the number of paragraphs
## in the body of the story
## INPUT: soup - the soup object
## OUTPUT: Return - a tuple with the title, author, date, and number of paragraphs
def get_page_info(soup):

    # get the title

    # get the date
    
    # get the author
    
    # get the number of paragraphs
    
    # return the tuple
    
    pass

## Part 4 - Find all of the U of M and Ann Arbor related content on the webpage
## INPUT: the dictionary that was returned from part 2
## OUTPUT: a new dictionary with just items that contain the word 'U-M' or 'Ann Arbor'
def find_mich_stuff(dict):
    pass

## Extra Credit
## INPUT: soup - the soup object
## OUTPUT: Return - a list containing all of the img element 'alt' attributes on the page
def find_img_alt(soup):
    pass

########### TESTS; DO NOT CHANGE ANY CODE BELOW THIS LINE ! ###########
########### You may, however, test code in the main function###########

# Utility functions
def getSoupObjFromURL(url):
    """ return a soup object from the url """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup

def getSoupObjFromFile(fileName):
    """ return a soup object from the file with the passed fileName"""
    source_dir = os.path.dirname(__file__) #<-- directory name
    full_path = os.path.join(source_dir, fileName)
    file = open(full_path,'r')
    text = file.read().strip()
    file.close()
    soup = BeautifulSoup(text, "html.parser")
    return soup

# Test using unittests and saved pages
class TestP2(unittest.TestCase):

    def setUp(self):
        self.soup = getSoupObjFromFile("news1.html")
        self.soup2 = getSoupObjFromFile("newsStory1.html")
        self.dict = get_headline_dict(self.soup)

    def test_grab_headlines(self):
        self.assertEqual(grab_headlines(self.soup),['Students sell Ben Shapiro tickets for as much as $200 ', 'To the white men who told me that they “prefer” white women', 'Students reflect on campus climate following sell-out of Shapiro tickets', 'Ben Shapiro discusses government compulsion, conservative values in talk at Rackham', 'Michigan, Michigan State and the mechanics of attacking a switch'])

    def test_get_headline_dict(self):
        dict = get_headline_dict(self.soup)
        url = dict[' Engineering school eliminates printing supplement ']
        self.assertEqual(len(dict.items()), 18)
        self.assertEqual(url,'https://www.michigandaily.com/section/academics/students-discuss-differences-printing-allocations-across-schools-0')

    def test_get_page_info(self):
        self.assertEqual(get_page_info(self.soup2), ('Students sell Ben Shapiro tickets for as much as $200 ', '\n    Monday, March 11, 2019 - 10:21pm  ', 'Amara Shaikh', 16))

    
    def test_find_mich_stuff(self):
        dict = find_mich_stuff(self.dict)
        url1 = dict[' U-M announces speakers for Spring Commencement  ']
        url2 = dict[' U-M’s allies in carbon neutrality effort have cloudy record on clean energy ']
        self.assertEqual(len(dict), 2)
        self.assertEqual(url1,'https://www.michigandaily.com/section/news-briefs/university-announces-speakers-spring-commencement-and-rackham-graduation')
        self.assertEqual(url2,'https://www.michigandaily.com/section/administration/u-m%E2%80%99s-allies-carbon-neutrality-effort-have-cloudy-record-clean-energy')
    
    '''Uncomment for extra credit test case
    def test_img_alt(self):
        my_list = find_img_alt(self.soup)
        my_list2 = find_img_alt(self.soup2)
        self.assertEqual(my_list,['Home', 'click for search', "The Michigan Daily's Facebook", "The Michigan Daily's Twitter", "The Michigan Daily's Instagram", "The Michigan Daily's YouTube channel"])
        self.assertEqual(my_list2,['Home', 'click for search', "Ticket prices for Ben Shapiro's talk at Rackham Auditorium Tuesday have increased due to high demand. ", "The Michigan Daily's Facebook", "The Michigan Daily's Twitter", "The Michigan Daily's Instagram", "The Michigan Daily's YouTube channel"])
    '''

def main():
    unittest.main(verbosity=2)
    #Uncomment this code to test your functions on live urls
    '''
    # testing on live urls
    soup = getSoupObjFromURL("https://www.michigandaily.com/section/news")
    print("GRAB_HEADLINES")
    print(grab_headlines(soup))
    print("-----------------------")
    print("GET_HEADLINE_DICT")
    hDict = get_headline_dict(soup)
    print(hDict)
    print("-----------------------")
    print("GET_PAGE_INFO")
    # get page info for each story in hDict
    for key, value in hDict.items():
        tuple = get_page_info(getSoupObjFromURL(value))
        print(tuple)
    print("-----------------------")
    print("EXTRA CREDIT")
    nDict = find_mich_stuff(hDict) # for extra credit
    print(nDict)
    print("-----------------------")
    '''

if __name__ == "__main__":
    main()
