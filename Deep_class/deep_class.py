class Vgg_model_analysis:

	def __init__(self,image_1,image_2,backend,metrics,
		display,result={'model':'not set','distance':'not set','verified':'not set'}):
		self.image_1 = image_1
		self.image_2 = image_2
		self.backend = backend
		self.metrics = metrics
		self.display = display
		self.result = result

	def perform_verification(self):
		from deepface import DeepFace
		self.result = DeepFace.verify(self.image_1,self.image_2, 
		 detector_backend = self.backend,model_name = 'VGG-Face', distance_metric = self.metrics, enforce_detection=False)
		return self.result

	def get_model_name (self):
		return self.result['model']

	def get_metrics(self):
		return self.metrics

	def get_backend(self):
		return self.backend

	def get_distance(self):
		return self.result['distance']

	def get_verification(self):
		return self.result['verified']

class FaceNet_model_analysis:

	def __init__(self,image_1,image_2,backend,metrics,
		display,result={'model':'not set','distance':'not set','verified':'not set'}):
		self.image_1 = image_1
		self.image_2 = image_2
		self.backend = backend
		self.metrics = metrics
		self.display = display
		self.result = result

	def perform_verification(self):
		from deepface import DeepFace
		self.result = DeepFace.verify(self.image_1,self.image_2, 
		 detector_backend = self.backend,model_name = '', distance_metric = self.metrics, enforce_detection=False)
		return self.result

	def get_model_name (self):
		return self.result['model']

	def get_metrics(self):
		return self.metrics

	def get_backend(self):
		return self.backend

	def get_distance(self):
		return self.result['distance']


class FaceNet512_model_analysis:

	def __init__(self,image_1,image_2,backend,metrics,
		display,result={'model':'not set','distance':'not set','verified':'not set'}):
		self.image_1 = image_1
		self.image_2 = image_2
		self.backend = backend
		self.metrics = metrics
		self.display = display
		self.result = result

	def perform_verification(self):
		from deepface import DeepFace
		self.result = DeepFace.verify(self.image_1,self.image_2, 
		 detector_backend = self.backend,model_name = '', distance_metric = self.metrics, enforce_detection=False)
		return self.result

	def get_model_name (self):
		return self.result['model']

	def get_metrics(self):
		return self.metrics

	def get_backend(self):
		return self.backend

	def get_distance(self):
		return self.result['distance']

class DeepFace_model_analysis:

	def __init__(self,image_1,image_2,backend,metrics,
		display,result={'model':'not set','distance':'not set','verified':'not set'}):
		self.image_1 = image_1
		self.image_2 = image_2
		self.backend = backend
		self.metrics = metrics
		self.display = display
		self.result = result

	def perform_verification(self):
		from deepface import DeepFace
		self.result = DeepFace.verify(self.image_1,self.image_2, 
		 detector_backend = self.backend,model_name = '', distance_metric = self.metrics, enforce_detection=False)
		return self.result

	def get_model_name (self):
		return self.result['model']

	def get_metrics(self):
		return self.metrics

	def get_backend(self):
		return self.backend

	def get_distance(self):
		return self.result['distance']






