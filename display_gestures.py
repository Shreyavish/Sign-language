import cv2, os, random
import numpy as np

def get_image_size():
	img = cv2.imread('new_gest/0/35.jpg', 0)
	return img.shape

new_gest = os.listdir('new_gest/')
new_gest.sort(key = int)
begin_index = 0
end_index = 5
image_x, image_y = get_image_size()



if len(new_gest)%5 != 0:
	rows = int(len(new_gest)/5)+1
else:
	rows = int(len(new_gest)/5)

full_img = None
for i in range(rows):
	col_img = None
	for j in range(begin_index, end_index):
		img_path = "new_gest/%s/%d.jpg" % (j, random.randint(1, 1500))
		img = cv2.imread(img_path, 0)
		if np.any(img == None):
			img = np.zeros((image_y, image_x), dtype = np.uint8)
		if np.any(col_img == None):
			col_img = img
		else:
			col_img = np.hstack((col_img, img))

	begin_index += 5
	end_index += 5
	if np.any(full_img == None):
		full_img = col_img
	else:
		full_img = np.vstack((full_img, col_img))


cv2.imshow("new_gest", full_img)
cv2.imwrite('full_img.jpg', full_img)
cv2.waitKey(0)