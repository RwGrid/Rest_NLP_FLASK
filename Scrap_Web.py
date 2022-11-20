from newspaper import Article

from urllib.parse import quote
class ScrapData(object):


    def getdata(self,sent_url):
        url = sent_url
        print(url)
       # url='https://www.sciencealert.com/scientists-find-mice-brain-switches-to-activate-hibernation-on-demand'

        article = Article(url, fetch_images=False)  # https://newspaper.readthedocs.io/en/latest/user_guide/advanced.html#parameters-and-configurations
        article.download()
        article.parse()

        return article
