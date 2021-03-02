The repo from Ultralytics for YOLOv3 has been extended and tested for the German Traffic Sign Recognition Dataset (GTSRB) and the Inferences have been found to be working good with 10-20 ms as the Inference time.
The data preprocessing has been carried out in accordance with the requirements, for e.g. in YOLOv3 one text file per image needs to be created. The text files, contains the data about bounding boxes’ coordinates and their class IDs.
The training/testing dataset ratio has been kept as 80:20.
The testing is being performed after every epoch i.e. testing is being conducted on test dataset simultaneously.
The training of YOLOv3 has been done for almost 100 epochs over 4 GPUs (each of 32Gbs) with distributed networking mode of PyTorch,  achieving a very good precision(94%) and recall(99%) with very minimal total loss.
The output here contains a good visualization like Confusion matrix, labels visualization, precision-recall curve graph, train and test batches with bounding boxes, and the biggest of all, results.png and results.txt, showing the flow of different types of losses (discussed previously) and metrics like mAP for IoU=0.5-0.95 (for validation).
A good visualization is also being facilitated in this framework(YOLOv3) with both, Wandb and Tensorboard.



## Requirements

Python 3.8 or later with all [requirements.txt](https://github.com/ultralytics/yolov3/blob/master/requirements.txt) dependencies installed, including `torch>=1.7`. To install run:
```bash
$ pip install -r requirements.txt
```

## Inference

detect.py runs inference on a variety of sources, downloading models automatically from the [latest YOLOv3 release](https://github.com/ultralytics/yolov3/releases) and saving results to `runs/detect`.
```bash
$ python detect.py --source 0  # webcam
                            file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
                            rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa  # rtsp stream
                            rtmp://192.168.1.105/live/test  # rtmp stream
                            http://112.50.243.8/PLTV/88888888/224/3221225900/1.m3u8  # http stream
```

To run inference on example images in `data/images`:
```bash
$ python detect.py --source data/images --weights yolov3.pt --conf 0.25


## Training

Download [COCO](https://github.com/ultralytics/yolov3/blob/master/data/scripts/get_coco.sh) and run command below. Training times for YOLOv3/YOLOv3-SPP/YOLOv3-tiny are 6/6/2 days on a single V100 (multi-GPU times faster). Use the largest `--batch-size` your GPU allows (batch sizes shown for 16 GB devices).
```bash
$ python train.py --data coco.yaml --cfg yolov3.yaml --weights '' --batch-size 24
                                         yolov3-spp.yaml                       24
                                         yolov3-tiny.yaml                      64
```
<img src="https://user-images.githubusercontent.com/26833433/100378028-af170c80-3012-11eb-8521-f0d2a8d021bc.png" width="900">


## Citation

[![DOI](https://zenodo.org/badge/146165888.svg)](https://zenodo.org/badge/latestdoi/146165888)

