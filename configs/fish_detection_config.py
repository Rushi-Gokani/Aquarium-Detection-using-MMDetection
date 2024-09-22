_base_ = [
    'E:/projects/Aqua/mmdetection/configs/_base_/models/faster-rcnn_r50_fpn.py',
    'E:/projects/Aqua/mmdetection/configs/_base_/datasets/coco_detection.py',
    'E:/projects/Aqua/mmdetection/configs/_base_/schedules/schedule_1x.py',
    'E:/projects/Aqua/mmdetection/configs/_base_/default_runtime.py'
]


dataset_type = 'CocoDataset'
classes = ('puffin', 'starfish', 'stingray', 'fish', 'shark', 'jellyfish','penguin')

data = dict(
    train=dict(
        img_prefix='E:\projects\Aqua\datasets\train',
        classes=classes,
        ann_file='E:\projects\Aqua\datasets\train\_annotations.coco.json',
    ),
    val=dict(
        img_prefix='E:\projects\Aqua\datasets\valid',
        classes=classes,
        ann_file='E:\projects\Aqua\datasets\valid\_annotations.coco.json',
    ),
    test=dict(
        img_prefix='E:\projects\Aqua\datasets\test',
        classes=classes,
        ann_file='E:\projects\Aqua\datasets\test\_annotations.coco.json',
    )
)

model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=len(classes))
    )
)

runner = dict(type='EpochBasedRunner', max_epochs=12)

load_from = 'checkpoints/faster_rcnn_r50_fpn_1x_coco.pth'
