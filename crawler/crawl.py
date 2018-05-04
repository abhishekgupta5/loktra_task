#!/usr/bin/python3

#Standard library import
import sys

#Third party imports
import requests
from bs4 import BeautifulSoup as bs

class CrawlIt(object):
    #For 1st query(total number of results for a given keyword). Argument- kw:keyword
    def query_one(self, kw):

        #URL construction
        kw = '+'.join(kw.split('_'))
        baseurl = "http://www.shopping.com/products?KW={}"
        url = baseurl.format(kw)

        print("Crawling into www.shopping.com for query one...")

        #Getting result of page request
        page = requests.get(url)
        #Check if request is successful
        if (page.status_code != 200):
            print("Invalid page request")
            sys.exit()

        #Creating BeautifulSoup parse tree
        soup = bs(page.text, 'html.parser')

        #Extracting number of results from CSS class selector
        get_results = soup.find_all(class_="numTotalResults")[0].text

        #Parsing actual result from raw data
        return int(get_results.split()[-1])


    #For 2nd query(to find all results for a given keywords on a specified page). Arguments- kw:keyword, pn:page_number
    def query_two(self, kw, pn):

        #URL construction
        kw = '+'.join(kw.split('_'))
        baseurl = "http://www.shopping.com/products~PG-{}?KW={}"
        url = baseurl.format(pn, kw)

        print("Crawling into www.shopping.com for query two...")

        #Getting result of page request
        page = requests.get(url)
        #Check if request is successful
        if (page.status_code != 200):
            print("Invalid url")
            sys.exit()

        #Creating BeautifulSoup parse tree
        soup = bs(page.text, 'html.parser')

        #Local variables
        id_=1
        dic = {}

        #Parsing products data from id tags inside span tags. Storing in dic.
        while True:
            product_title = soup.find('span', id='nameQA'+str(id_))
            if product_title is not None:
                dic[id_] = product_title.text[:-6]
                id_ += 1
            else:
                break

        #Check for no results on page
        if id_ == 1:
            return 0

        #Return data in dictionary
        return dic


    #Method to parse arguments and invoking respective method
    def parse_arguments(self):
        try:
            #Query two
            if len(sys.argv) == 3:
                keyword = str(sys.argv[1])
                page_number = int(sys.argv[2])
                get_dic = self.query_two(keyword, page_number)
                print()
                if get_dic != 0:
                    print(get_dic)
                else:
                    print('No results on Page', page_number)
                print()

            #Query one
            elif len(sys.argv) == 2:
                keyword = str(sys.argv[1])
                print("Number of results -", self.query_one(keyword))

            else:
                print("Incorrect number of arguments")
                sys.exit()

        except ValueError:
            print("Incorrect order/type of arguments")


if __name__ == '__main__':
    obj = CrawlIt()
    obj.parse_arguments()
