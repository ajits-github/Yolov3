The repo from Ultralytics for YOLOv3 has been extended and tested for the German Traffic Sign Recognition Dataset (GTSRB) and the Inferences have been found to be working good with 10-20 ms as the Inference time.
The data preprocessing has been carried out in accordance with the requirements, for e.g. in YOLOv3 one text file per image needs to be created. The text files, contains the data about bounding boxes’ coordinates and their class IDs.
The training/testing dataset ratio has been kept as 80:20.
The testing is being performed after every epoch i.e. testing is being conducted on test dataset simultaneously.
The training of YOLOv3 has been done for almost 100 epochs over 4 GPUs (each of 32Gbs) with distributed networking mode of PyTorch,  achieving a very good precision(94%) and recall(99%) with very minimal total loss.
The output here contains a good visualization like Confusion matrix, labels visualization, precision-recall curve graph, train and test batches with bounding boxes, and the biggest of all, results.png and results.txt, showing the flow of different types of losses (discussed previously) and metrics like mAP for IoU=0.5-0.95 (for validation).
A good visualization is also being facilitated in this framework(YOLOv3) with both, Wandb and Tensorboard.

