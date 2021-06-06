import urllib2
import optparse
from urlparse import urlsplit
from os.path import basename
from bs4 import BeautifulSoup
from PIL import Image
from PIL.ExifTags import TAGS


def findImages(url):
      print '[+] finding imagesnya sekarang' + url
      urlContent = urllib2.urlopen(url).read()
      soup = BeautifulSoup(urlContent)
      imgTags = soup.findAll('img')
      return imgTags
def downloadImage(imgTag):
   try:
       print '[+] download image now .......'
       imgSrc = imgTag['src']
       imgContent = urllib2.urlopen(imgSrc).read()
       imgFileName = basename(urlsplit(imgSrc)[2])
       imgFile - open(imgFileName, 'wb')
       imgFile.write(imgContent)
       imgFile.close()
       return imgFIleName
   except:
       return ''
def testForExif(imgFileName):
   try:
       exifData = []
       imgFile = image.open(imgFileName)
       info = imgFile._getexif()
       if info:
          for (tag, value) in info.items():
            decode = TAGS.get(tag, tag)
            exifData[decoded] = value
          exifGPS = exifData['GPSinfo']
          if exifGPS:
             print '[*] ' + imgFileName + ' gps for info guys'
       except:
          pass
def main():
   parser = optparse.OptionsParser('usage%prog "+\ "-u <tagret url>')
   parser.add_option('-u', dest='url', type='string', help='specify url addres')
   (options, args) = parser.parse_args()
   url = options.url
   if url == None:
      print parser.usage
      exit(0)
   else:
     imgTags = findImages(url)
     for imgTag in imgTags:
       imgFileName = downloadImage(imgTag)
       testForExif(imgFIleName)

if __name__ == '__main__':
   main()
