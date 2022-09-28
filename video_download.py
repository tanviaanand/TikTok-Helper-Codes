
# TikTokApi requirements, run: (from https://github.com/davidteather/TikTok-Api)
# pip install TikTokApi
# python3 -m playwright install

# Pandas requirements, run:
# pip install pandas

from TikTokApi import TikTokApi
import pandas as pd

def download(read_path, write_path):
    # function takes path to your csv file
    df = pd.read_csv(read_path)
    # assuming your csv contains IDs in a column named "id". Change accordingly.
    ids = df["id"]

    api = TikTokApi()
        
    for id in ids:
        try:
            video = api.video(id=id)
            video_file = video.bytes()
            with open(write_path+str(id)+".mp4", "wb") as out_file:
                out_file.write(video_file)
                # print(id) # uncomment this if you want to see download progress 
        except Exception as e:
            # most exceptions that come up here are because of random tiktok download issues, 
            # e.g. if the video has been deleted, so I simply ignore these exceptions.
            pass 
