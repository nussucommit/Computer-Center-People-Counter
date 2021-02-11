# Computer-Center-People-Counter <!-- omit in toc -->
Program to count number of people entering and exiting a computer centre in NUS.

## Contents <!-- omit in toc -->
- [Introduction](#introduction)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Work in progress...

## Usage
1. Either get ready some videos or your web cam.
2. Try the program out with the following command:
- using web cam:
```shell
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --output output/<output-video-filename>1.avi --output-csv output/<output-csv-filename>.csv
```
- using video input:
 ```shell
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/<input-video-filename>.mp4 --output output/<output-video-filename>1.avi --output-csv output/<output-csv-filename>.csv
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
