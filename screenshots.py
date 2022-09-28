import ffmpeg
from os import listdir
from os.path import isfile, join

def screenshots(read_path, write_path):
    video_path = read_path
    video_list = [f for f in listdir(video_path) if isfile(join(video_path, f))]
    video_list = [x for x in video_list if ".mp4" in x]

    for video_file in video_list:
        try:
            print(video_file)
            probe = ffmpeg.probe(video_path+video_file)
            time = float(probe['streams'][0]['duration']) 
            width = probe['streams'][0]['width']
            
            # uncomment whichever you want to use

            # part a) divide videos into 'n' parts and take screenshots

            # parts = 8
            # intervals = time // parts
            # intervals = int(intervals)

            # part b) specify intervals at which you want to take screenshots

            intervals = 1
            parts = time // intervals
            parts = int(parts)
            
            interval_list = [(i * intervals, (i + 1) * intervals) for i in range(parts)]
            i = 0
            for item in interval_list:
                try:
                    ffmpeg.input(video_path+video_file, ss=item[1]).filter('scale', width, -1).output(write_path+video_file[:-4]+'_'+str(i)+'.jpg', vframes=1).run()
                except:
                    print("")
                i += 1
        except:
            print("")
