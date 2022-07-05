# https://www.superdatascience.com/blogs/opencv-face-detection
#----------------

import cv2
import time

#----------------
def detect_faces(tipoCascade='haar', video=0, scaleFactor=1.1, minNeighbors=5, saveVid=False, framerate=5.0):
	'''
	Localiza e enquadra rostos humanos durante um video (ou da camera).
	Utiliza a biblioteca 'cv2', do pacote 'opencv-python'.
	Inclui os modelos de cascata 'haarcascade_frontalface_default.xml' e 'lbpcascade_frontalface_improved.xml'.
	Haar eh mais preciso, mas Lbp eh mais rapido.

	Params:
		tipoCascade [string] (default='haar'): Tipo de cascata pode ser 'haar' ou 'lbp'.
		video [string ou int] (default=0): Int se refere ao indice do dispositivo da camera
										   (caso so haja um dispositivo de camera, este tem indice 0).
										   String se refere ao diretorio do arquivo de video.
		scaleFactor [float] (default=1.1): Taxa de redimensionamento para identificar faces com tamanhos diferentes.
		minNeighbors [int] (default=5): Quantidade de faces identificadas proximas entre si para ser considerado como face.
		saveVid [bool] (default=False): True para gravar o video no arquivo "recorded.avi". False nao grava.
		framerate [float] (default=5.0): Taxa de frames por segundo a ser gravado, caso saveVid seja "True".
										 Framerate deve estar de acordo com a taxa de captura, caso esteja recebendo da camera.
		
	Retorna:
		None.
	'''


	if tipoCascade=='haar':
		cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	elif tipoCascade=='lbp':
		cascade = cv2.CascadeClassifier("lbpcascade_frontalface_improved.xml")
	else:
		print("Tipo de cascata invalida. Tipo de cascata pode ser 'haar' ou 'ibp'.")
		return

	cap = cv2.VideoCapture(video)

	fourcc = cv2.VideoWriter_fourcc(*'XVID') 
	out = cv2.VideoWriter('recorded.avi', fourcc, 5.0, (640, 480))

	while(True):

		ret, img = cap.read()
		gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(image = gray_img, scaleFactor = scaleFactor, minNeighbors = minNeighbors)

		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(124,255,0),2)

		out.write(img)
		cv2.imshow('img',img)

		if (cv2.waitKey(1) & 0xFF == ord('q')): #Aperta q para sair
			break

	cap.release()
	out.release()
	cv2.destroyAllWindows()

#----------------------
#MAIN

detect_faces(tipoCascade='haar', video=0, scaleFactor=1.1, minNeighbors=4, saveVid=False, framerate=5.0)
#detect_faces(tipoCascade='lbp', video=0, scaleFactor=1.1, minNeighbors=4, saveVid=False, framerate=5.0)