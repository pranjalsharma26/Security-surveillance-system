
It includes various features for the purpose of vehicle surveillance and parking management in the areas like residential, business complexes and toll plazas.

The following features are available in this repo-

1. Object Segmenatation which is done using Mask-RCNN technique in which multiple objects are detected from video.
Here is the link for google colaboratory notebook- https://drive.google.com/open?id=1pFqA6Xupz5dYfomhTeNYj06rVZQbGHH5 for the above mentioned purpose.

2. Extraction of number plate from vehicle in which we verify the vehicle entering in the building is of resident or a visitor vehicle. We have used MySQLite for database and Tesseract (OCR library of Python) is used for extraction and reading number plate.

3. Web Interface built using Tensorflow.js in which a separate pre-trained model is deployed and currently hosted on chrome server.

4. Annotation are done using Labelme in which we use polygon annotation whose output is json file and is used in Mask-RCNN technique on which the object segmentation model is actually based on.

NOTE - Further, you can extend this work if you wish to by combining this all parts!
