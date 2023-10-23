# Prepare datasets

If you have a dataset directory, you could use os environment variable named `YOLOX_DATADIR`. Under this directory, YOLOX will look for datasets in the structure described below, if needed.
```
$YOLOX_DATADIR/
  KITTI/
```
You can set the location for builtin datasets by
```shell
export YOLOX_DATADIR=/path/to/your/datasets
```
If `YOLOX_DATADIR` is not set, the default value of dataset directory is `./datasets` relative to your current working directory.

# Preprocess

1. link [KITTI](https://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=2d) data folder to datasets/ and put datasplit.py、txt2xml.py、xml2txt.py to KITTI folder:

```
├── datasets  
    ├── KITTI                  // data folder
        ├── image_2            // raw images
        │   └── 000001.png
        ├── label_2            // raw labels
        │   └── 000001.txt
        ├── datasplit.py       // tool
        ├── txt2xml.py         // tool
        └── xml2txt.py         // tool
```

2. use txt2xml.py to generate xml files and put it to annotations folder automatically.

> class_ind = ('Car', 'Cyclist', 'Truck', 'Van', 'Pedestrian', 'Tram') # attention
> img_name = name+'.png' # attention

```bash
python txt2xml.py
```
```
├── datasets  
    ├── KITTI                  // data folder
        ├── image_2            // raw images
        │   └── 000001.png
        ├── label_2            // raw labels
        │   └── 000001.txt
        ├── annotations        // ⭐xml files folder  
        ├── datasplit.py       // tool
        ├── txt2xml.py         // tool
        └── xml2txt.py         // tool
```

3. use xml2txt.py to covert kitti format to voc
```bash
python xml2txt.py
```

```
├── datasets  
    ├── KITTI                  // data folder
        ├── image_2            // raw images
        │   └── 000001.png
        ├── label_2            // raw labels
        │   └── 000001.txt
        ├── annotations        // xml files folder  
        ├── labels             // ⭐ txt files folder, training labels
        ├── datasplit.py       // tool
        ├── txt2xml.py         // tool
        └── xml2txt.py         // tool
```

4. split data to train、val and test

TODO: modify file path 

```bash
python datasplit.py
```

```
├── KITTI                  // result looks like this
    ├── image_2            // raw images
    │   └── 000001.png
    ├── label_2            // raw labels
    │   └── 000001.txt
    ├── annotations       // xml files folder  
    ├── labels            // training labels
    ├── test.txt          // ⭐ test data list
    ├── train.txt         // ⭐ train data list
    ├── val.txt           // ⭐ val data list
    ├── datasplit.py       // tool
    ├── txt2xml.py         // tool
    └── xml2txt.py         // tool
```


5. ln image_2 to images and JPEGImages
```bash
ln -s image_2/ images
ln -s image_2/ JPEGImages
```

```
├── KITTI                  // result looks like this
    ├── image_2            // raw images
    │   └── 000001.png
    ├── label_2            // raw labels
    │   └── 000001.txt
    ├── annotations       // xml files folder  
    ├── labels            // training labels
    ├── images            // ⭐ link to image_2
    ├── JPEGImages        // ⭐ link to image_2
    ├── test.txt          // test data list
    ├── train.txt         // train data list
    ├── val.txt           // val data list
    ├── datasplit.py       // tool
    ├── txt2xml.py         // tool
    └── xml2txt.py         // tool
```

6. put test、train、val to ImageSets/

```
├── KITTI                  // result looks like this
    ├── image_2            // raw images
    │   └── 000001.png
    ├── label_2            // raw labels
    │   └── 000001.txt
    ├── annotations       // ⭐ xml files folder  
    ├── labels            // training labels
    ├── images            // link to image_2
    ├── JPEGImages        // link to image_2
    ├── ImageSets         // ⭐ label sets
        ├── test.txt      // test data list
        ├── train.txt     // train data list
        ├── val.txt       // val data list
    ├── datasplit.py       // tool
    ├── txt2xml.py         // tool
    └── xml2txt.py         // tool
```

