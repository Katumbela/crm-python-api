
from facebook_scraper import get_posts  


for post in get_posts('angola', pages=3): 
    print(post['text'][:50])
 


