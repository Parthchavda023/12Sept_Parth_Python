#---Only for Educaion Purpose---#

import pyqrcode

link="https://www.youtube.com/"
sp=pyqrcode.create(link)
sp.png('YoutubeCode.png')