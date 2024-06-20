# Detection and information of poisonous mushrooms using machine learning
Team Projects for Embedded Systems and IOT<br/>
YOUTUBE about our team project: 

## Project Introduction
A machine learning project with the theme of "Detecting Poison Mushrooms Using Raspberry Pi".<br/>
This project aims to detect poisonous mushrooms in real-time using a Raspberry Pi and machine learning.<br/> 
By leveraging the YOLOv8 model, the system identifies mushrooms through a connected camera and signals their toxicity status via LED lights. Additionally, detailed information about the detected mushrooms is provided on a web page.

## Development period (contents)
 - 2024.5.5 ~ 2024.6.17
 - Writing Project Plan
 - dataset Collecting & Labeling(labelme)
 - Machine Learning Programming with YOLOv8
 - Web page programming
 - Raspberry Pi Programming(Python) & Implementation(LED, Camera ..)

## Develoment environment
- Main Language: Python
- Machine Learning Framework: YOLOv8
- Development Tools: Raspberry Pi, VScode, SSH, VNC
- Labeling tool: Labelme
- Web Programming Languages: HTML, CSS

## Data set
- source(how to gather data): Using kaggle site - Mushroom Classification Dataset(updated by ZAIN UL ABDIN, https://www.kaggle.com/datasets/zedsden/mushroom-classification-dataset)
- Number of Data Points: 400 photographic data
- kind of labes(kind of mushroom data):
  - poisonous - Hypholoma fasciculare, Ramaria formosa, Galerina marginata, Amanita virosa<br/>
  - eible - Hypholoma lateritium, agaricus arvensis, Oyster mushroom, Sparassis crispa, Volvariella volvacea, Apioperdon pyriforme

1. Reading the Toxicity of Mushrooms
After detecting mushrooms using a camera connected to a raspberry pie designed based on a pre-trained model, it is possible to determine the toxicity of mushrooms based on the learned data.

## Architecture map(Block Diagram)
![diagram_iot](https://github.com/SeongbinCho01/EmbeddedIoT/assets/83772963/e08a8182-cc97-4eab-84b3-8ef600aba1e2)



## Key Features
1. Reading the Toxicity of Mushrooms<br/>
- The system uses a camera connected to a Raspberry Pi to detect mushrooms based on a pre-trained YOLOv8 model.
- It identifies whether the mushrooms are poisonous or edible from a dataset of 10 types (4 poisonous, 6 edible).
- LEDs indicate toxicity status: red for poisonous, green for edible.
  
2. Provide approximate information on mushrooms<br/>
- Detailed information about the detected mushrooms is displayed on a web page.
- Users can access specific details about the appearance and risks associated with each type of mushroom through linked web pages.



