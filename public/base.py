
from public import Config

def get_url(endpoint):
    
    host=Config.url()
    
    url=host+endpoint
    
    return url
    