import random
import cv2
import os
from glob import glob
import numpy as np
from tqdm import tqdm
from PIL import Image
from pathlib import Path
from pyfiglet import Figlet
print(Figlet(font='big').renderText('  MOSIAC'))

OUTPUT_SIZE = (720, 1280)  # Height, Width
SCALE_RANGE = (0.5, 0.5) # Space occupy by each image
NUM_IMG =10 # Total number of MOSIAC images wants to generates
ANNO_DIR = "dataset/Annotations"
IMG_DIR = "dataset/Images"
OUT_DIR = "output"
Print_Bbox=True #Keep True if wants to print Bbox on image

os.makedirs(OUT_DIR,exist_ok = True)
for f in os.listdir(OUT_DIR):
    os.remove(os.path.join(OUT_DIR, f))

def main():
	img_paths, annos = get_dataset(ANNO_DIR, IMG_DIR)

	for idx in tqdm(range(NUM_IMG), desc="AUGMENTATION-NO:", total=NUM_IMG):

		idxs = random.sample(range(len(annos)), 4)

		new_image, new_annos = update_image_and_anno(img_paths,annos,idxs,OUTPUT_SIZE,SCALE_RANGE)

		cv2.imwrite(os.path.join(OUT_DIR,'image_'+str(idx)+'.jpg'),new_image)

		#anno---> [cls_id, x1, y1, x2, y2]
		path_txt=os.path.join(OUT_DIR,'image_'+str(idx)+'.txt')
		for anno in new_annos:
			xc,yc,w,h= (anno[1] + anno[3])/2.0 , (anno[2] + anno[4])/2.0, anno[3] - anno[1], anno[4] - anno[2]
			with open(path_txt,'a') as f:
				f.write(f'{anno[0]} {xc} {yc} {w} {h}\n')

		if Print_Bbox:
			for anno in new_annos:
				start_point = (int(anno[1] * OUTPUT_SIZE[1]),int(anno[2] * OUTPUT_SIZE[0]))
				end_point = (int(anno[3] * OUTPUT_SIZE[1]),int(anno[4] * OUTPUT_SIZE[0]))
				cv2.rectangle(new_image, start_point, end_point, (0, 255, 255), 1,cv2.LINE_AA)

			cv2.imwrite(os.path.join(OUT_DIR,'image_'+str(idx)+'_with_boxes.jpg'),new_image)


def update_image_and_anno(all_img_list,all_annos,idxs,output_size,scale_range):

	output_img = np.zeros([output_size[0], output_size[1], 3], dtype=np.uint8)
	scale_x = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
	scale_y = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
	divid_point_x = int(scale_x * output_size[1])
	divid_point_y = int(scale_y * output_size[0])

	new_anno = []
	for i, idx in enumerate(idxs):
		path = all_img_list[idx]
		img_annos = all_annos[idx]

		img = cv2.imread(path)
		if i == 0:  # top-left
			img = cv2.resize(img, (divid_point_x, divid_point_y))
			output_img[:divid_point_y, :divid_point_x, :] = img
			for bbox in img_annos:
				xmin = bbox[1] * scale_x
				ymin = bbox[2] * scale_y
				xmax = bbox[3] * scale_x
				ymax = bbox[4] * scale_y
				new_anno.append([bbox[0], xmin, ymin, xmax, ymax])

		elif i == 1:  # top-right
			img = cv2.resize(img,
							 (output_size[1] - divid_point_x, divid_point_y))
			output_img[:divid_point_y, divid_point_x:output_size[1], :] = img
			for bbox in img_annos:
				xmin = scale_x + bbox[1] * (1 - scale_x)
				ymin = bbox[2] * scale_y
				xmax = scale_x + bbox[3] * (1 - scale_x)
				ymax = bbox[4] * scale_y
				new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
		elif i == 2:  # bottom-left
			img = cv2.resize(img,
							 (divid_point_x, output_size[0] - divid_point_y))
			output_img[divid_point_y:output_size[0], :divid_point_x, :] = img
			for bbox in img_annos:
				xmin = bbox[1] * scale_x
				ymin = scale_y + bbox[2] * (1 - scale_y)
				xmax = bbox[3] * scale_x
				ymax = scale_y + bbox[4] * (1 - scale_y)
				new_anno.append([bbox[0], xmin, ymin, xmax, ymax])
		else:  # bottom-right
			img = cv2.resize(img, (output_size[1] - divid_point_x,
								   output_size[0] - divid_point_y))
			output_img[divid_point_y:output_size[0],
					   divid_point_x:output_size[1], :] = img
			for bbox in img_annos:
				xmin = scale_x + bbox[1] * (1 - scale_x)
				ymin = scale_y + bbox[2] * (1 - scale_y)
				xmax = scale_x + bbox[3] * (1 - scale_x)
				ymax = scale_y + bbox[4] * (1 - scale_y)
				new_anno.append([bbox[0], xmin, ymin, xmax, ymax])

	return output_img, new_anno


def get_dataset(anno_dir, img_dir):
	img_paths = []
	annos = []
	base_path = Path(".")
	images = IMG_DIR
	annotations = ANNO_DIR+'\*.txt'

	annot_paths = list(glob(annotations))
	for anno_file in annot_paths:
		anno_id = anno_file.split('\\')[-1].split('.')[0]  #Chnage split to "/"is using UBUNTU

		img_path = os.path.join(images,anno_id+'.jpg')

		img = cv2.imread(img_path)
		img_height, img_width, _ = img.shape
		del img

		boxes = []
		with open(anno_file) as f:
			for i in f.readlines():
				i = i.split()
				class_id = int(i[0])
				x, y, w, h = float(i[1]), float(i[2]), float(i[3]), float(i[4])
				x1, y1, x2, y2 = x-w/2, y-h/2 , x+w/2, y+h/2

				boxes.append([class_id, x1, y1, x2, y2])

		if not boxes:
			continue

		img_paths.append(img_path)  # img_path is a list of images
		annos.append(boxes)

	return img_paths, annos


if __name__ == '__main__':
	main()