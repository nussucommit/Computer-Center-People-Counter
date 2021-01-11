# Computer-Center-People-Counter
Program to count number of people entering and exiting a computer centre in NUS.

## Contents
- [Introduction](#Introduction)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)

## Introduction
Work in progress...

## Usage
1. Either get ready some videos or your web cam.
2. Try the program out with the following command:
- using web cam:
```shell
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --output output/<output-video-filename>.avi
```
- using video input:
 ```shell
python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input <input-video-filename>.mp4 --output output/output_01.avi
```

## Contributing

## License
Computer Center People Counter is released under the [MIT License](./LICENSE).
