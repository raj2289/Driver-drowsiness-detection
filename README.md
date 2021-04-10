# Driver-drowsiness-detection using CNN

<h2>DATASET</h2>
 we were using Real Life Drowsiness Detection Dataset(RLDD) for training our CNN model.
 Using dataset extactraion code we croped images of eyes which were used for training CNN classification moddel.
 <h3>Citation</h3>
All documents (such as publications, presentations, posters, etc.) that report results, analysis, research, or equivalent that were obtained by using the UTA-RLDD database should cite the following research paper:
https://arxiv.org/abs/1904.07312
<h3>RLDD Dataset Videos</h3>
You can access the data using this link:
<href>http://vlm1.uta.edu/~athitsos/projects/drowsiness/</href>

			       
<h2>Prerequisites for project</h2>
The requirement for this Python project is a webcam through which we will capture images. You need to have Python (3.6 version recommended) installed on your system, then using pip, you can install the necessary packages.
<p>1.OpenCV – pip install opencv-python (face and eye detection).</p>
<p>2.TensorFlow – pip install tensorflow (keras uses TensorFlow as backend).</p>
<p>3.Keras – pip install keras (to build our classification model).</p>
<p>4.Pygame – pip install pygame (to play alarm sound).</p>
<h2>The Model Architecture</h2>
The CNN model architecture consists of the following layers:

<p>Convolutional layer; 32 nodes, kernel size 3</p>
<p>Convolutional layer; 32 nodes, kernel size 3</p>
<p>Convolutional layer; 64 nodes, kernel size 3</p>
<p>Fully connected layer; 128 nodes</p>
The final layer is also a fully connected layer with 2 nodes. In all the layers, a Relu activation function is used except the output layer in which we used Softmax.

<h2>Steps to detect drowsiness</h2>
<p><b>Step 1</b> Take image as input from a camera.</p>
<p><b>Step 2</b> Detect the face in the image and create a Region of Interest (ROI).</p>
<p><b>Step 3</b>  Detect the eyes from ROI and feed it to the classifier.</p>
<p><b>Step 4</b>  Classifier will categorize whether eyes are open or closed.</p>
<p><b>Step 5</b>  Calculate score to check whether the person is drowsy.</p>




