# sih2020
Only for sharing purpose for SIH task

This project is entirely for the MIXORG organization for the purpose of SIH.
It includes various features for the purpose of vehicle surveillance and parking management in residential, business complexes and toll plazas.

Currently we are sumbitting few of the features. Following are the featuers that we are submitting as of now-
1. Object Segmenatation which is done using Mask-RCNN technique in which multiple objects are detected from video.
2. Extraction of number plate from vehicle in which we verify the vehicle entering in the building is of resident or a visitor vehicle. We have used MySQLite for database and Tesseract (OCR library of Python) is used for extraction and reading number plate.
3. Web Interface built using Tensorflow.js in which a separate pre-trained model is deployed and currently hosted on chrome server.
