
from urllib.request import urlretrieve
destination = "C:/Users/jpher/Downloads/"

url="http://www.jphe.net/index.html"
dest=destination + "test_chargement.php"
urlretrieve(url,dest)
print ("test commit")