from ftplib import FTP

# Reading password
with open('passwd.txt', 'r') as f:
    passwd = f.read().strip()  # Corrected to read() and strip()

# Enter credentials after creating an FTP directory on bplaced.net
host = 'abc.bplaced.net'  # Corrected hostname
user = 'abc'
password = passwd  # Corrected variable

with FTP(host) as ftp:
    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    # Downloading file from server
    # with open('test.txt', 'wb') as f:
    #     ftp.retrbinary('RETR ' + 'mytest.txt', f.write, 1024)  # Space added

    # Uploading files to server
    # with open('myupload.txt', 'rb') as f:
    #     ftp.storbinary('STOR ' + 'upload.txt', f)  # Space added

    # Changing directory then writing a file to the server
    ftp.cwd('mydir')
    with open('myfile.txt', 'wb') as f:
        ftp.retrbinary('RETR ' + 'otherfile.txt', f.write, 1024)  # Space added

    ftp.quit()
