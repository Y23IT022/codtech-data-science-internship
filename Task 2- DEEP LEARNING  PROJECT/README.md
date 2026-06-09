**TASK 2: DEEP LEARNING MODEL FOR CLASSIFICATION**

**Fashion Item Classification using PyTorch**

**OBJECTIVE**

The objective of this project is to build a deep learning model capable of classifying fashion items using PyTorch.

The model learns patterns from image data and predicts clothing categories.

**DATASET**

FashionMNIST Dataset from PyTorch.

* Total Images: 70,000
* Classes: 10
* Image Size: 28×28 grayscale images

**TECHNOLOGIES USED**

* Python
* PyTorch
* Torchvision
* Matplotlib

**WORKFLOW**

**1. Dataset Loading**

* Loaded FashionMNIST dataset using torchvision.
* Applied image transformations.

**2. Data Preparation**

* Created training and testing datasets.
* Used DataLoader for batch processing.

**3. Model Building**

* Built a neural network using PyTorch.
* Used fully connected layers and ReLU activation.

**4. Model Training**

* Applied CrossEntropyLoss and Adam optimizer.
* Trained the model for multiple epochs.

**5. Evaluation**

* Monitored training loss.
* Generated performance graph.

**6. Model Saving**

* Saved trained model using PyTorch.

**DEEP LEARNING ARCHITECTURE**

* Input Layer
* Hidden Layer (128 neurons)
* Hidden Layer (64 neurons)
* Output Layer (10 classes)

**OUTPUT FILES**

* fashion_classifier.py
* fashion_model.pth
* accuracy_graph.png

**HOW TO RUN**

Install Dependencies:

pip install torch torchvision matplotlib

Run Program:

python fashion_classifier.py

**RESULT**

The deep learning model successfully classifies fashion items using image data. The trained model was saved and training performance was visualized using a graph.

**AUTHOR**

Bonthala supriya sindhu
