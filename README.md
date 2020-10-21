# Unbox AI


### welcome to subscribe my channel
- [youtube channel](https://youtube.com/channel/UCAebg3DDFtidQJ0Jp20kyaw)
- [bilibili channel](https://space.bilibili.com/326361150)


## unbox project
- Zero-VIRUS*: Zero-shot VehIcle Route Understanding System for Intelligent Transportation ([CVPR 2020 AI City Challenge Track 1](https://www.aicitychallenge.org/2020-data-and-evaluation/))


## video
- youtube

[![3 minutes to experience an AI open source project in NVIDIA 2020 AI CITY CHALLENGE, Zero-VIRUS](https://res.cloudinary.com/marcomontalbano/image/upload/v1603257486/video_to_markdown/images/youtube--Lps2CfKMGX8-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=Lps2CfKMGX8 "[Unbox AI] Zero-VIRUS")


## system requirements
- ubuntu 18.04
- python >= 3.6
- cuda 10.2


## setup environments
1. clone source codes

    ```$ git clone https://github.com/dyh/unbox_Lijun-Yu_zero_virus.git```

2. enter project directory

    ```$ cd unbox_Lijun-Yu_zero_virus```

3. create a python virtual environment

    ```$ python3 -m venv venv```

4. activate the virtual environment

    ```$ source venv/bin/activate```

5. upgrade pip

    ```$ python -m pip install --upgrade pip```

6. install requirements package

    1. install other packages
    
        ```$ pip install -r requirements.txt```
    
    2. install detectron2 (based on cuda 10.2 and pytorch 1.5.1)
    
        and you could choose other version at [here](https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md#install-pre-built-detectron2-linux-only)
    
        ```$ python -m pip install https://dl.fbaipublicfiles.com/detectron2/wheels/cu102/torch1.5/detectron2-0.2.1%2Bcu102-cp36-cp36m-linux_x86_64.whl```


## execute the program
1. detect the "./unbox_test/input/MVI_40855.mp4" video file of this project

    ```$ python unbox.py```

2. the output results are saved in "./unbox_test/output" directory for some image files

    0.png, 1.png, 2.png ... n.png

3. you can use ffmpeg to merge these images into one video file

    ```$ ffmpeg -f image2 -i ./unbox_test/output/%d.png ./unbox_test/output.mp4```

## sample dataset
- the test video [MVI_40855.mp4](/unbox_test/input/MVI_40855.mp4) is made up of images in the directory "MVI_40855" in the [DETRAC-test-data.zip](http://detrac-db.rit.albany.edu/Data/DETRAC-test-data.zip) file.
- download dataset: http://detrac-db.rit.albany.edu/download
- introduction of dataset: http://smart-city-sjsu.net/AICityChallenge/data.html


----

# AI开箱


### 欢迎订阅我的频道
- [bilibili频道](https://space.bilibili.com/326361150)
- [youtube频道](https://youtube.com/channel/UCAebg3DDFtidQJ0Jp20kyaw)


## 开箱项目
- 用于智能交通的 Zero-shot 车辆路线理解系统
- Zero-VIRUS*: Zero-shot VehIcle Route Understanding System for Intelligent Transportation ([CVPR 2020 AI City Challenge Track 1](https://www.aicitychallenge.org/2020-data-and-evaluation/))


## 视频
- bilibili

[![3分钟体验一个NVIDIA 2020 AI CITY CHALLENGE挑战赛的AI开源项目 Zero-VIRUS](https://res.cloudinary.com/marcomontalbano/image/upload/v1603257486/video_to_markdown/images/youtube--Lps2CfKMGX8-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.bilibili.com/video/bv1sp4y1k7nd "[Unbox AI] Zero-VIRUS")


## 系统需求
- ubuntu 18.04
- python >= 3.6
- cuda 10.2


## 环境配置
1. 下载代码

    ```$ git clone https://github.com/dyh/unbox_Lijun-Yu_zero_virus.git```

2. 进入目录

    ```$ cd unbox_Lijun-Yu_zero_virus```

3. 创建python虚拟环境

    ```$ python3 -m venv venv```

4. 激活虚拟环境

    ```$ source venv/bin/activate```

5. 升级pip

    ```$ python -m pip install --upgrade pip```

6. 安装软件包

    1. 安装其他包
    
        ```$ pip install -r requirements.txt```

    2. 安装 detectron2 (基于 cuda 10.2 和 pytorch 1.5.1)
    
        你也可以在 [这里](https://github.com/facebookresearch/detectron2/blob/master/INSTALL.md#install-pre-built-detectron2-linux-only) 选择其他版本
    
        ```$ python -m pip install https://dl.fbaipublicfiles.com/detectron2/wheels/cu102/torch1.5/detectron2-0.2.1%2Bcu102-cp36-cp36m-linux_x86_64.whl```


## 运行程序
1. 对项目中的 ./unbox_test/input/MVI_40855.mp4 视频文件进行检测

    ```$ python unbox.py```

2. 输出结果为图片文件，保存在 ./unbox_test/output 目录

    0.png, 1.png, 2.png ... n.png

3. 可以使用 ffmpeg 将图片文件合并为视频文件

    ```$ ffmpeg -f image2 -i ./unbox_test/output/%d.png ./unbox_test/output.mp4```

## 样本数据集
- 测试视频 [MVI_40855.mp4](/unbox_test/input/MVI_40855.mp4) 是由 [DETRAC-test-data.zip](http://detrac-db.rit.albany.edu/Data/DETRAC-test-data.zip) 文件中的 MVI_40855 目录下图片组成。
- 数据集下载 http://detrac-db.rit.albany.edu/download
- 数据集说明 http://smart-city-sjsu.net/AICityChallenge/data.html


----

# below is the origin README file

----


# Zero-VIRUS*: Zero-shot VehIcle Route Understanding System for Intelligent Transportation ([CVPR 2020 AI City Challenge Track 1](https://www.aicitychallenge.org/2020-data-and-evaluation/))

Authors: [Lijun Yu](https://me.lj-y.com), Qianyu Feng, Yijun Qian, Wenhe Liu, Alexander G. Hauptmann \
Email: lijun@lj-y.com

*Written in the era of Coronavirus Disease 2019 (COVID-19), with a sincere hope for a better world.

```bib
@inproceedings{yu2020zero,
  title={Zero-VIRUS: Zero-shot VehIcle Route Understanding System for Intelligent Transportation},
  author={Yu, Lijun and Feng, Qianyu and Qian, Yijun and Liu, Wenhe and Hauptmann, Alexander G.},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition Workshops},
  year={2020}
}
```

## Setup

Install [miniconda](https://conda.io/en/latest/miniconda.html), then create the environment and activate it via

```sh
conda env create -f environment.yml
conda activate zero_virus
```

Directory structure:

* datasets
  * Dataset_A (`AIC20_track1_vehicle_counting.zip/Dataset_A`)
  * Dataset_B (hidden evaluation)
* experiments
  * efficiency
    * aic2020-base.json
  * `<experiment_name>`
    * output.txt

## Evaluate

As a zero-shot system, no training is required.
We use [Mask R-CNN](http://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html) pretrained on [COCO](http://cocodataset.org/#home) from [detectron2](https://github.com/facebookresearch/detectron2) as detector, whose weights will be downloaded automatically at the first run.

As the dataset only provided screenshots of the pre-defined routes, we created our own [annotation](monitor/tracks) of them with [labelme](https://github.com/wkentaro/labelme).

To get system outputs, run

```sh
./evaluate.sh <experiment_name> <dataset_split>
# For example
./evaluate.sh submission Dataset_A
```

To get efficiency base score, run

```sh
python utils/efficiency_base.py
```

## Performance

On Dataset A with 8 V100 GPUs:

* S1: 0.9328
  * S1_Effectiveness: 0.9120
    * mwRMSE: 4.2738
  * S1_Efficiency: 0.9815
    * time: 3084.04
    * baseline: 0.546801

Visualizations available at [Google Drive](https://drive.google.com/drive/folders/1s3TPykPa3JTaPOHUVOQF8S4iUi3SduAN?usp=sharing).

## License

See [LICENSE](LICENSE). Please read before use.
