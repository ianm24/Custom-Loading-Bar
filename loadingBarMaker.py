# Program Made By: Ian McDowell
# Started 30 December 2018

from PIL import Image
import glob, os, imageio

path = 'images'
if(os.path.exists(path) == False):
	os.mkdir(path)
delList = glob.glob(os.path.join(path, "*.PNG"))
for f in delList:
	os.remove(f)

# height and width of the bar
height = 25
width = 100

images = []

# color of empty bar
img = Image.new("RGB",(width, height),(220,220,220))
img.save('images/0.PNG')
images.append(imageio.imread(os.getcwd() + '\\images/0.PNG'))
i = 1

#changing each pixel and saving an image when each column has been colored
for x in xrange(width):
	for y in xrange(height):
		# color of loaded bar
		img.putpixel((x,y),(116, 9, 142))
	file = 'images/'+str(i) + '.PNG'
	img.save(file)	
	images.append(imageio.imread(os.getcwd() +'\\'+file)) 
	i = i + 1

# makes the gif
imageio.mimsave(os.getcwd()+'\\customLoadingBar.gif', images)
