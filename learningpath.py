import subprocess


urlfile = '/content/lynda-dl/url.txt'

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  


# with open(urlfile, mode='r') as f:
#     url=[line.strip() for line in f]
#     subprocess.call(['python', '/content/lynda-dl/lynda-dl.py', '-u', '1331987', '-p', 'eikaykhine', '-o', 'detroitpubliclibrary.org', '-d', '/content/drive/Shared drives/Hein Ko Zin Unlimited/Lynda Courses/Download/Learning Paths/Become a MERN Stack JavaScript Developer/ ', '-q', '720',  listToString(url)]);


with open(urlfile) as fp:
   line = fp.readline()
   while line:
       
       subprocess.call(['python', '/content/lynda-dl/lynda-dl.py', '-u', '1331987', '-p', 'eikaykhine', '-o', 'detroitpubliclibrary.org', '-d', '/content/drive/Shared drives/Hein Ko Zin Unlimited/Lynda Courses/Download/Learning Paths/Become a MERN Stack JavaScript Developer/ ', '-q', '720',  listToString(line.strip())]);
       line = fp.readline()
       
