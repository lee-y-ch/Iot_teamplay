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



## 주요 기능
1. 버섯의 독성 유무 판독
미리 학습된 모델을 바탕으로 설계된 라즈베리파이에 연결된 카메라를 이용해 버섯을 탐지한 후, 학습된 데이터를 바탕으로 버섯의 독성 유무를 파악할 수 있다.
총 10개의 버섯을 탐지할 수 있으며, 그 중 4개는 독버섯이고 나머지 6개는 식용버섯이다. 독성 유무를 가시적으로 보여주기 위해 라즈베리파이로 LED를 구현했다. 독버섯이면 빨간색 LED가 빛나고 식용버섯이면 초록색 LED가 빛난다.
2. 버섯의 대략적인 정보 제공
탐지된 버섯의 대략적인 정보를 웹페이지를 통해 제공한다. 미리 만들어 둔 웹페이지의 링크를 해당 버섯에 맞게 연결하여 사용자에게 보여준다.
버섯의 겉모습과 위험도를 위주로 정보를 제공한다. 

1. Reading the Toxicity of Mushrooms
After detecting mushrooms using a camera connected to a raspberry pie designed based on a pre-trained model, it is possible to determine the toxicity of mushrooms based on the learned data.
A total of 10 mushrooms can be detected, four of which are poisonous mushrooms and the remaining six are edible mushrooms. To show the presence or absence of toxicity visually, LEDs are implemented with raspberry pie. If it is a poisonous mushroom, the red LED glows, and if it is an edible mushroom, the green LED glows.
2. Provide approximate information on mushrooms
It provides approximate information on detected mushrooms through a web page.

1. Reading the Toxicity of Mushrooms<br/>
After detecting mushrooms using a camera connected to a raspberry pie designed based on a pre-trained model, it is possible to determine the toxicity of mushrooms based on the learned data.<br/>
A total of 10 mushrooms can be detected, four of which are poisonous mushrooms and the remaining six are edible mushrooms.<br/>
To show the presence or absence of toxicity visually, LEDs are implemented with raspberry pie. If it is a poisonous mushroom, the red LED glows, and if it is an edible mushroom, the green LED glows.
3. Provide approximate information on mushrooms<br/>
It provides approximate information on detected mushrooms through a web page.<br/>

-> Connect the link to the pre-made web page to the corresponding mushroom and show it to the user.(information based on the appearance and risk of mushrooms.)

## Architecture map


## Key Features
1. Reading the Toxicity of Mushrooms<br/>
- The system uses a camera connected to a Raspberry Pi to detect mushrooms based on a pre-trained YOLOv8 model.
- It identifies whether the mushrooms are poisonous or edible from a dataset of 10 types (4 poisonous, 6 edible).
- LEDs indicate toxicity status: red for poisonous, green for edible.
  
2. Provide approximate information on mushrooms<br/>
- Detailed information about the detected mushrooms is displayed on a web page.
- Users can access specific details about the appearance and risks associated with each type of mushroom through linked web pages.



