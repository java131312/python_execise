#!/bin/env python
from bs4 import BeautifulSoup
soup = BeautifulSoup(open('index.html'),"html5lib")
soup = BeautifulSoup("<html>data</html>","html5lib")
