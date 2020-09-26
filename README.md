# mp4_sub_merge
This is a simple python script to batch hardcode subtitles into mp4 videos.
To run this script you'll need ffmpeg and add it to your PATH variables.

It takes in a single folder path as argument and merges every mp4 video with its corresponding subtitles file, assuming they have the same name. e.g. sample.mp4 and sample.srt
The output video will be in the merge folder created on the desktop.

### Sample Usage
```
python merge_sub.py C:\Users\user1\Desktop\mp4_folder
```

