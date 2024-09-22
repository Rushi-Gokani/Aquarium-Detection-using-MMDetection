from mmdet.apis import init_detector, inference_detector
from mmdet.registry import VISUALIZERS
import mmcv
import cv2

config_file = 'E:/projects/Aqua/mmdetection/configs/_base_/default_runtime.py' 
checkpoint_file = 'E:/projects/Aqua/work_dirs/default_runtime/epoch_5.pth'




model = init_detector(config_file, checkpoint_file, device='cpu')

image = mmcv.imread('test6.jpg')
result = inference_detector(model, image)

visualizer = VISUALIZERS.build(model.cfg.visualizer)

visualizer.dataset_meta = model.dataset_meta

visualizer.add_datasample(
    'result',
    image,
    data_sample=result,
    draw_gt=False,
    wait_time=0,
    out_file='outputs/result.png' 
)
visualizer.show()