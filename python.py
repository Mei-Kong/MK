from urllib.parse import unquote

a = '妹控'
url = 'http://www.baidu.com/s?wd=%E5%A6%B9%E6%8E%A7'
print(unquote(url))
