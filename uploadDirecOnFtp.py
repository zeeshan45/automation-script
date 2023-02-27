import os
import ftplib
ftp_host = "192.168.0.158"
ftp_user = "ftp-user"
ftp_pass = "pass@123"

ftp = ftplib.FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)
images_directories = os.listdir(local_path)
for img_dir in images_directories:
    sku_direct = os.path.join(local_path,img_dir)
    list_images = os.listdir(sku_direct)
    ftp.mkd(img_dir)
    ftp.cwd(img_dir)
    for img in list_images:
        img_path = os.path.join(sku_direct+'/',img)
        with open(img_path, "rb") as f:
            ftp.storbinary("STOR " + img, f)
#         print(img_dir,img,img_path)
#         break
    ftp.cwd('..')
    if images_directories.index(img_dir) == 1000:
        break