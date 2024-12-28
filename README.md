# I Care - Smart Doctor
Comprehensive Medical System - Easy Healthcare for Anyone Anytime!

![Logo Design](media/Picsart_23-10-20_06-03-49-430.png)
(Graduation Project)

## OverView

Test Run Video

As a team leader i have distributed the tasks on the team members, i have decided to work with Agile methodology so i was making a meeting each one or two weeks with the team members to presenting the work done
i was responsible for the AI modules which are:

### My part in the project consists of three main modules:

**Module 1:** An AI based smart chatbot called "Caroline" talking to the patient 
and taking its disease symptoms by text or voice messages, then diagnosing the disease and 
recommend making some tests or medical imaging scans to do as x-ray, MRI, Complete Blood Count CBC, ... in addition, given 
information about the predicted disease as an overview, symptoms, and 
treatments.

It can predict 30 diseases such as (Breast Cancer, Influenza, Covid 19, Stroke, ...) 

**Module 2:** A sequence of AI Computer Vision models for scanning medical 
imaging scans and medical tests it can scan (X-ray, MRI, CT, OCT, CBC, or Food images), 
detect the image type (Image Recognition), if it is medical imaging image, 
applying anatomical recognition, disease evaluation, disease diagnosis, and also in tumor or bone fraction cases 
it can segmentate the tumor or the fraction using image segmentation.
         
It can predict 25 disease types such as (Bone Fracture, Brain Tumor, Covid 19, Breast Cancer, ...) 

It can read the Complete Blood Count (CBC) test images and evaluate overall health and diagnose conditions like anemia, infections, clotting disorders, and blood cancers by analyzing red and white blood cells, hemoglobin, hematocrit, and platelets.

It also can recognize 101 food types from images and shows the approximate number of calories per gram.

**Module 3:** An ensemble Machine Learning (Random Forest) Model for scan Electrocardiography ECG and diagnosis the heart diseases.

In addition of making algorithm for MBTI personality analysis test.

## Implementation Methodology
Using transfer learning to get a pre-trained models on a huge dataset image net and customize their input layer shape to be suitable with the images and customize the output layer structure and activation function as need, so the models have an initial value for the parameters then they train faster and gives better accuracy. 

The AI module is designed in different parts. There are a Natural Language Processing NLP, Deep Learning Computer Vision Classification, Image Segmentation, Optical Character Recognition OCR, Large Language Model LLM, Speech Recognition, and Machine Learning Models all are combined together to mimic a doctor for all specialties.

**AI Model Table**
Contains Input, Output, Functionality, Training and Testing Accuracy, and Recall information
![Logo Design](media/models table.jpg)

**AI Scan Models Work Flow**
Sequence for the Image Scan Computer Vision Models
![Logo Design](media/Final_ai.drawio.svg)

**AI Scan Models Work Flow**
Sequence for the Image Scan Computer Vision Models
![Logo Design](media/Final_ai.drawio.svg)

## Results
accuracy

## References
datasets
