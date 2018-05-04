# Loktra task

----
## Hash task
[Question](https://github.com/Loktra/software-engineer/blob/master/Hash.md)

### For running, follow these steps-
**Dependencies** - python3

1) Clone the project

2) *cd* into the *hash/* directory

3) Run with `python reverse_hash.py`

4) Run test with `python test_reverse_hash.py`

*hash_to_str* method in *HashIt* class contains the logic of reversing the hash

## Web crawler
[Question](https://github.com/Loktra/fullstack-engineer/blob/master/Web%20Crawler.md)

### For running, follow these steps-
**Dependencies** - python3, BeautifulSoup, requests

**Note** - Make sure you have *pip* and *virtualenv* installed

1) Clone the project

2) *cd* into the project directory

3) Create virtual environment - `virtualenv -p /usr/bin/python3 venv`

4) Activate env - `source venv/bin/activate`

5) Install dependencies - `pip install -r requirements.txt`

#### Usage examples

* *cd* into *crawler/* directory
* For query 1- `python crawler.py <keyword>`
  * `python crawler.py abc`
  * `python crawler.py abc_def_ghi` (For multiple words keyword use underscores)
  * `python crawler.py subtle_art_of_not_giving_a`
  
  Expect total number of results for search keyword or relevant error message.

* For query 2- `python crawler.py <keyword> <page number>`
**Note** Arguments are expected to be in order as mentioned in question for desired results.
  * `python crawler.py abc 8`
  * `python crawler.py abc_def 5`
  * `python crawler.py subtle_art_of_not_giving_a 3`
  
  Expect a dictionary with {position : product_name} for all products on requested page number for search keyword or relevant error message
* Run tests with `python test_crawler.py`
