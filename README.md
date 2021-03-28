# Computer-Center-People-Counter <!-- omit in toc -->
Application to count number of people entering and exiting a computer centre in NUS.

## Contents <!-- omit in toc -->
- [Introduction](#introduction)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This application is used to analyze the usage of AS8 computer centre in NUS. It takes in a CCTV footage and outputs a CSV as well as graph indicating the number of people in the computer centre at each point in time.

## Usage
1. Either get ready some videos or your web cam.
2. Try the program out with the following command:
- using web cam:
```shell
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --output output/<video-filename>.avi --confidence 0.4 --skip-frames <frames-to-skip> --output-csv output/<video-filename>.csv --output-plots <video-filename>
```
- using video input:
 ```shell
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/<video-filename>.mp4 --output output/<video-filename>.avi --confidence 0.4 --skip-frames <frames-to-skip> --output-csv output/<video-filename>.csv --output-plots output/<video-filename>
```
- example using video input:
```
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/ch05_20201211120000.mp4 --output output/ch05_20201211120000.avi --confidence 0.4 --skip-frames 60 --output-csv output/ch05_20201211120000.csv --output-plots output/ch05_20201211120000
```

## Contributing
1. Codes obtained from: https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/

2. Pre-trained model from: https://github.com/chuanqi305/MobileNet-SSD/tree/master/voc

3. Primary results looks pretty promising. Logic goes like this: if u on the left of line and moving left, it classifies as going out and vice versa.

4. Pros: Works fine, 0 training needed.

5. Potential improvements: 
- find a pre-trained model with higher precision
- fine-tune existing input parameters

## License
[Computer Center People Counter](#Computer-Center-People-Counter) is released under the [MIT License](./LICENSE).
