# http-Basic-Bruteforce
## Python program to create bruteforce lists for http basic authentification

**Usage**<br/>
open commandline and cd to the directory where you downloaded the script

`python http_basic_bruteforce.py -u [path to user file] -p [path to password file]`  

**Parameters**  
-u: path to username file e.g. C:\Users\you\Desktop\user.txt<br/>
-p: path to password file e.g. C:\Users\you\Desktop\password.txt<br/>
<br/>
If username or password file are in the same directory as the script, you can just use the name of the file and don´t have to type the path (e.g. user.txt)

--help/-h: display the help message
<br/>
<br/>
**User and password wordlists**<br/>
There´s a variety of sources for username and password wordlists. A few are listed below, but feel free to use others or create your own:<br/>
- https://github.com/jeanphorn/wordlist/blob/master/usernames.txt
- https://github.com/insidetrust/statistically-likely-usernames/blob/master/john.smith.txt
- https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt<br/>

<br/>**Output**<br/>
For http basic authentification a string in the form of username:password is encoded in base64. <br/>
The script takes every name in the supplied username file and combines it with every password in the supplied password file.<br/>
The output is written to a file called bruteforce.txt where every line contains one http basic authentification string. <br/>
Be aware that with large input files, the file size of bruteforce.txt will be huge so make sure you have enough disk space. <br/>

<br/>**Test**<br/>
In the Test Files Directory you can find two simple input files: a user.txt file (contains 4 usernames) and a password.txt file (contains 6 passwords).<br/>
With this input, a bruteforce.txt file with 24 http basic authentification strings is created.<br/>
You can use https://www.base64decode.org/ to check if the strings are generated correctly.<br/>
