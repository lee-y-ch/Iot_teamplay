# Detection and information of poisonous mushrooms using machine learning
임베디드시스템및IOT로의 활용 팀 프로젝트

## 프로젝트 소개
'라즈베리파이를 이용한 독버섯 탐지"를 주제로 한 머신러닝 프로젝트. 실시간으로 탐지한 버섯의 독성 유무를 알리고, 해당 버섯에 대한 대략적인 정보를 제공하는 목적을 가지고있다.
Yolov8을 이용한 머신러닝과 라즈베리파이가 핵심인 프로젝트로서, 라즈베리파이에 연결한 카메라로 탐지된 버섯의 독성 유무를 LED 신호로 알려주고 해당 버섯에 대한 정보를 웹페이지로 제공한다. 

## 개발 기간
 - 2024.5.5 ~ 2024.6.17
 - Project Plan 작성
 - dataset 수집 & 라벨링(labelme)
 - YOLOv8을 활용한 머신러닝 프로그래밍
 - 웹 페이지 프로그래밍
 - 라즈베리파이(Python) 프로그래밍 & 라즈베리파이 구현(LED, Camera ..)

## 개발 환경
- 언어: Python
- 머신러닝: YOLOv8
- 개발 환경: Raspberry Pi, VScode, SSH, VNC
- 라벨링 도구: Labelme
- 웹 개발: HTML, CSS

## Data set
- Number of data:
- kind of labes(kind of mushroom data): poisonous - Hypholoma fasciculare, Ramaria formosa, Galerina marginata, Amanita virosa<br/>
                 eible - Hypholoma lateritium, agaricus arvensis, Oyster mushroom, Sparassis crispa, Volvariella volvacea, Apioperdon pyriforme
- how to gather data: Using kaggle site - Mushroom Classification Dataset(updated by ZAIN UL ABDIN, https://www.kaggle.com/datasets/zedsden/mushroom-classification-dataset)

## 아키텍쳐


## 주요 기능
<<<<<<< HEAD
>>>>>>> ee8843a (Update README.md)
=======
1. 버섯의 독성 유무 판독
미리 학습된 모델을 바탕으로 설계된 라즈베리파이에 연결된 카메라를 이용해 버섯을 탐지한 후, 학습된 데이터를 바탕으로 버섯의 독성 유무를 파악할 수 있다.
총 10개의 버섯을 탐지할 수 있으며, 그 중 4개는 독버섯이고 나머지 6개는 식용버섯이다. 독성 유무를 가시적으로 보여주기 위해 라즈베리파이로 LED를 구현했다. 독버섯이면 빨간색 LED가 빛나고 식용버섯이면 초록색 LED가 빛난다.
2. 버섯의 대략적인 정보 제공
탐지된 버섯의 대략적인 정보를 웹페이지를 통해 제공한다. 미리 만들어 둔 웹페이지의 링크를 해당 버섯에 맞게 연결하여 사용자에게 보여준다.
버섯의 겉모습과 위험도를 위주로 정보를 제공한다. 
>>>>>>> 006f546 (Update README.md)
