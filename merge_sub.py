"""
Created on Fri Sep  4 17:34:00 2020
This program takes a single folder path as arguement and merges all video
and subtitle files under it, retaining the their original audio quality
videl quality is compressed to 2000kbps

Sample usage:
python merge_sub.py sample_folder/files

Useful resources for ffmpeg:
https://stackoverflow.com/questions/57869367/ffmpeg-subtitles-alignment-and-position
https://ffmpeg.org/ffmpeg.html

@author: Daniel Hao
"""
import os
import sys

# This us a sample command line usage of ffmpeg, it outputs an video with 2000kbps and retains original audio by not re-encoding, only copying
# It also changes the subtitle size and reposition it to the bottom center of the screen, moving it slightly up
# It will overwrite the file if a file with the same name exists
sample = "ffmpeg -y -i test.mp4 -b:v 2M -c:a copy -vf subtitles=test.srt:force_style='Alignment=2,Fontsize=18,MarginV=30' out.mp4"
mp4 = ".mp4"
mkv = ".mkv"

def get_ffmpeg_comm(video, subtitle, output_folder):
    ffmpeg_comm = "ffmpeg -y -i " + "\"" + video + "\""
    ffmpeg_comm +=  " -b:v 2M -c:a copy -vf subtitles=\"" + subtitle + "\":force_style='Alignment=2,Fontsize=19,MarginV=30' "
    ffmpeg_comm += "\"" + output_folder + "\\" + video + "\""
    return ffmpeg_comm


# get the path to desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
output_folder = os.path.join(desktop, 'merged')

# retrive folder path from command line and make it our current directory
if __name__ == "__main__":
    file_path = sys.argv[1]
    
os.chdir(file_path)    

# create a output folder on the desktop
if not os.path.exists(output_folder):
    os.mkdir(output_folder)


"""
loop through every file in our current directory
if it's a video file look for its corresponding srt file and if it's there
merge it and output it to the merged folder on desktop
"""
# retriev all files under current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)] 
    
for f in files:
    # if its an mp4 file we look for its correspoding srt file, assuming it has the exact same file name
    if mp4 in f:
        
        file_name = f[:-4]
        
        srt_file = (file_name + ".srt")
        ass_file = (file_name + ".ass")
        
        if srt_file in files:
            ffmpeg_comm = get_ffmpeg_comm(f, srt_file, output_folder)
            os.system(ffmpeg_comm)
            print(ffmpeg_comm)
            
        elif ass_file in files:
            ffmpeg_comm = get_ffmpeg_comm(f, ass_file, output_folder)
            os.system(ffmpeg_comm)
            print(ffmpeg_comm)
        




    
    
    
    
    
    