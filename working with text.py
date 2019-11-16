# my_file=open("test.txt","w")
# my_file.write("Lets see if this actually works\n")
# my_file.write("------------\n")
# my_file.write("Did it really workk? Cool lets close it then\n")
# my_file.close()

# Opening a file for reading
new_file = open("text.txt", "r")
while True:
    line_read = new_file.readline()
    if len(line_read) == 0:
        break
    print(line_read, end="")
new_file.close()

# Reading and saving a text file
new_file = open("text.txt", "r")
list_file=new_file.readlines()
new_file.close()
# print(list_file)
save_list=open("save.txt","w")
for item in list_file:
    save_list.write(item)
save_list.close()

save=open("save.txt")
# save_string=save.read()
# print(save_string)
# for i in save_string:
#     print(i)
# save.close()
# words=save_string.split()
# print(words)
# print("we have {0} words in this file".format(len(words)))

# Reading and Writing images
photo=open("image.jpg","rb")
image_file=open("image_file.jpg","wb")
while True:
    buf=photo.read(1024)
    if len(buf)==0:
        break
    image_file.write(buf)
photo.close()
image_file.close()

# Reading content from URLS
import urllib.request
url="https://console.actions.google.com/u/0/project/qwiklabs-gcp-00-295cefd876dc/simulator"
destination="text.txt"
urllib.request.urlretrieve(url,destination)

import urllib.request

def retrieve_page(url):
    """ Retrieve the contents of a web page.
        The contents is converted to a string before returning it.
    """
    my_socket = urllib.request.urlopen(url)
    dta = str(my_socket.read())
    my_socket.close()
    return dta

the_text = retrieve_page("http://cs.berea.edu/courses/csc226book/files.html")
print(the_text)



