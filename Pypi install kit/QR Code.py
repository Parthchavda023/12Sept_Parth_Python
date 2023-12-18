#---Only for Educaion Purpose---#
# pyqrcode and pypng kit pc ka install krvi
import pyqrcode

link="https://www.youtube.com/"
sp=pyqrcode.create(link)
sp.png('YoutubeCode.png')