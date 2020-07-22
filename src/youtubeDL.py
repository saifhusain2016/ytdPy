import os
url = ""
savePath = "D:\\%(playlist)s\\%(title)s.%(ext)s"
format = "--merge-output-format bestvideo"
os.system("youtube-dl "+format+" -o "+savePath+" "+url);

