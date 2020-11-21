"""The only files available for direct download are the ones which are listed under yt.streams.all().
However, it is straightforward to convert the downloaded audio file from .mp4 to .mp3 format.
For example, if you have ffmpeg installed, running this command from the terminal will do the
trick (assuming you're in the download directory):

$ ffmpeg -i downloaded_filename.mp4 new_filename.mp3

Alternatively, you can use Python's subprocess module to execute the ffmpeg command programmatically:"""

import sys
import os
import subprocess
import pytube

# https://www.tutorialspoint.com/python-library-pytube-to-download-youtube-videos


if __name__ == "__main__":
    try:
        #url = "https://www.youtube.com/watch?v=WH7xsW5Os10"
        url = "https://youtu.be/rVV_tGBKgB4"
        yt = pytube.YouTube(url)

        # For example, if you would like to download mp4 video file format it would look like the following:
        # yt.streams.filter(file_extension='mp4').first()
        # If you would like to pull audio it would look like the following:
        # yt.streams.filter(only_audio=True).all()

        first_mp4 = yt.streams.filter(file_extension='mp4').first()
        print(first_mp4)

        """vids = yt.streams.all()
        for i in range(len(vids)):
            print(i,'. ',vids[i])
        vnum = int(input("Enter vid num: "))
        vid = vids[vnum]"""
        vid = first_mp4

        
        #print(vid.title)
        #print(dir(vid))
        #print(vid.default_filename)
        default_filename = vid.default_filename  # get default name using pytube API
        print(default_filename)

        parent_dir = r"D:\Users\mhatm\Downloads\YTDownloads"
        vid.download(parent_dir)

        #new_filename = input("Enter filename (including extension): ")  # e.g. new_filename.mp3
        new_filename = default_filename + '.mp3'

        #command = r'ffmpeg'
        command = r'C:\apps\ffmpeg\bin\ffmpeg'

        subprocess.call([                               # or subprocess.run (Python 3.5+)
            command,
            '-i', os.path.join(parent_dir, default_filename),
            os.path.join(parent_dir, new_filename)
        ])
    except Exception as e:  # pytube.exceptions.VideoUnavailable:
        #e = sys.exc_info()[0]
        print('ERROR: %s' % e)
    finally:
        print('done')

    #except: # catch *all* exceptions
    #    e = sys.exc_info()[0]
    #    write_to_page( "<p>Error: %s</p>" % e )

    # By using raise with no arguments, you will re-raise the last exception. A common
    # place to use this would be to roll back a transaction, or undo operations.
