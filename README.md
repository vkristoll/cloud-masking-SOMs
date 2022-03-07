# Fine-tuning  Self-Organizing Maps (SOMs) for cloud masking 

This repository contains code related to the study analyzed in the paper cited below:

Kristollari, V.; Karathanassi, V. Fine-Tuning Self-Organizing Maps for Sentinel-2 Imagery: Separating Clouds from Bright Surfaces. Remote Sens. 2020, 12, 1923. 

It can be accessed in: https://www.mdpi.com/2072-4292/12/12/1923

![SOM stages 1 and 2](/images/SOM_stage1_and_2.png)

![SOM stage 3](/images/SOM_stage3.png)

## Steps to implement the code

Run:

>1. "read_h5file.py" to download Sentinel-2 spectra and extract the 6 categories of reflectance data.
>
>2. "data_preprocessing.py" to create training data for the SOM. 
>
>3. "SOM_training.py" to train and save the network.
>
>4. "BMUs_detection.py" to detect and save the coordinates of the Best Matching Units (BMUs) for each spectral signature of the training set.
>
>5. "labeling.py" to label the SOM neurons through majority voting.
>
>6. "test_data_downloading.py" to download the test Sentinel-2 images.
>
>7. the commands in the "gdal_commands" file to convert the Sentinel-2 images to .tiff files.
>
>8. "convert_image_to_csv.py" to convert Sentinel-2 .tiff files to .csv files.
>
>9. "create_cloudmasks.py" to create the cloud masks for the Sentinel-2 images.
>
>10. "evaluation_metrics.py" to evaluate the cloud masks.

### Optionally:

Run:

- "Creating_hit_rate_maps.py" , "Creating_component_planes.py", "Creating_scatterplots.py" to evaluate through visualization techniques.
- "colored_cloudmasks.py" to produce cloud masks with different colours for TP,TN,FN,FP.
- "add_georeference.py" to add georeference to the cloud masks.

*Detailed guidelines are included inside each script.

*The trained SOM ("SOM_trained.p") can be downloaded from https://mega.nz/file/WEkjEIba#Q85WGr14UljMVQ8vui2Otou21-q71l7ZKeF4fL0b-8w

*The output file of "BMUs_detection.py" ("BMUs.csv") can be downloaded from https://mega.nz/file/SR0hVSpQ#1z5yK6alpe5TC33lTVZSbt5DZ9dW_9eaI2B23O-Fzgk

If you use this code, please cite the below paper.

```
@Article{rs12121923,
AUTHOR = {Kristollari, Viktoria and Karathanassi, Vassilia},
TITLE = {Fine-Tuning Self-Organizing Maps for Sentinel-2 Imagery: Separating Clouds from Bright Surfaces},
JOURNAL = {Remote Sensing},
VOLUME = {12},
YEAR = {2020},
NUMBER = {12},
ARTICLE-NUMBER = {1923},
URL = {https://www.mdpi.com/2072-4292/12/12/1923},
ISSN = {2072-4292},
DOI = {10.3390/rs12121923}
}
```




























