# Program Made By: Ian McDowell
# Started and Finished 30 December 2018

from PIL import Image
import glob, os, imageio

path = 'images'
if(os.path.exists(path) == False):
	os.mkdir(path)
delList = glob.glob(os.path.join(path, "*.PNG"))
for f in delList:
	os.remove(f)

# height and width of the bar
height = 100
width = 500

# color of empty bar
img = Image.new("RGB",(width, height),(220,220,220))
img.save('images/0'+ '.PNG')
i = 1

#changing each pixel and saving an image when each column has been colored
for x in xrange(width):
	for y in xrange(height):
		# color of loaded bar
		img.putpixel((x,y),(116, 9, 142))
		# print(i)	
	img.save('images/'+str(i) + '.PNG')
	i = i + 1

#adds the above created images to a list
images = []
sorting = []
image_path = os.getcwd() + '\\images\\*.PNG'
files = glob.glob(image_path)

for file in files:
	images.append(imageio.imread(file))
	data = file.replace('.PNG', '')
	data = data.replace(os.getcwd() + '\\images\\', '')
	sorting.append(int(data))

# ~(-*-)~

# sorting the images list using the sorting list (selection sort)
for i in range(len(sorting)):
	minIndex = i
	for j in range(i+1, len(sorting)):
		if sorting[minIndex] > sorting[j]:
			minIndex = j
	sorting[i], sorting[minIndex] = sorting[minIndex], sorting[i]
	images[i], images[minIndex] = images[minIndex], images[i]

# makes the gif
imageio.mimsave(os.getcwd()+'\\customLoadingBar.gif', images)