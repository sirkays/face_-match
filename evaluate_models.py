
from Deep_class import deep_class

images = [('ed2','eddy'),('ed3','eddy'),('ed4','eddy'),('ed5','eddy'),
('ed6','eddy'),('godwin1','godwin'),('godwin2','godwin'),
('godwin3','godwin'),('img4','nkechi'),
('img5','nkechi'),('img6','favour'),('img7','favour'),('img8','favour'),
('img9','nkechi'),('img10','kayode'),('kay','kayode'),('kay2','kayode'),
('kay3','kayode'),('img12','chukwu'),('img13','chukwu')]


img_dir = [('ed2','eddy'),('ed3','eddy'),('ed4','eddy'),('ed5','eddy'),
('ed6','eddy'),('godwin1','godwin'),('godwin2','godwin'),
('godwin3','godwin'),('img4','nkechi'),
('img5','nkechi'),('img6','favour'),('img7','favour'),('img8','favour'),
('img9','nkechi'),('img10','kayode'),('kay','kayode'),('kay2','kayode'),
('kay3','kayode'),('img12','chukwu'),('img13','chukwu')]

results_x = []

original_count = 0
for img in img_dir:
	count = 0
	for img_x in images:
		original_count += 1
		correct_pred = img[1] == img_x[1]
		obj_vgg = deep_class.Vgg_model_analysis(img[0]+".jpg",img_x[0]+".jpg",
			'retinaface','cosine','not set')
		obj_vgg.perform_verification()
		if(obj_vgg.get_verification() == correct_pred):
			count+=1

	results_x.append((obj_vgg.get_model_name(),count,original_count))
	print(results)



