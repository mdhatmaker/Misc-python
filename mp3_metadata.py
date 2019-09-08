import eyed3
from os import listdir
from os.path import isfile, join

def list_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def print_mp3_metadata(pathname):
    audiofile = eyed3.load(pathname)
    print("artist:", audiofile.tag.artist)
    print("album:", audiofile.tag.album)
    print("albumn_artist:", audiofile.tag.album_artist)
    print("title:", audiofile.tag.title)
    print("track #:", audiofile.tag.track_num)
    print()
    return

def update_mp3_metadata(pathname, tracknum, title, artist, album):
    try:
        audiofile = eyed3.load(pathname)
        #audiofile.tag.artist = u"Integrity"
        #audiofile.tag.album = u"Humanity Is The Devil"
        #audiofile.tag.album_artist = u"Integrity"
        #audiofile.tag.title = u"Hollow"
        #audiofile.tag.track_num = 2
        audiofile.tag.track_num = tracknum
        audiofile.tag.title = title
        audiofile.tag.artist = artist
        audiofile.tag.save()
    except:
        print("***EXCEPTION: Error updating metadata for '{0}'".format(pathname))
    return

def update_folder_metadata(folder, album, trackcount):
    li_filenames = list_files(folder)
    for filename in li_filenames:
        temp = str(filename.encode('ascii', 'ignore'))
        split = temp.split('.')
        tracknum = split[0]
        trackname = split[1]
        split = trackname.split('-')
        title = split[0]
        artist = split[1]
        mp3file = join(folder, filename)
        #print_mp3_metadata(mp3file)
        print(tracknum, title, artist)
        update_mp3_metadata(mp3file, (tracknum, trackcount), title, artist, album)
    return

################################################################################

# This particular folder had 3 subfolders (CD1, CD2, CD3), and the
# filenames were structured in a way that I could pull some metadata
# from the filename and update it in the mp3 file.

mp3_folder = r"Z:\Shared Music\The Workout Mix (2011)\CD1"
mp3_album = r"The Workout Mix 2011 - CD1"
mp3_trackcount = 16
update_folder_metadata(mp3_folder, mp3_album, mp3_trackcount)

mp3_folder = r"Z:\Shared Music\The Workout Mix (2011)\CD2"
mp3_album = r"The Workout Mix 2011 - CD2"
mp3_trackcount = 17
update_folder_metadata(mp3_folder, mp3_album, mp3_trackcount)

mp3_folder = r"Z:\Shared Music\The Workout Mix (2011)\CD3"
mp3_album = r"The Workout Mix 2011 - CD3"
mp3_trackcount = 16
update_folder_metadata(mp3_folder, mp3_album, mp3_trackcount)


"""
audiofile = eyed3.load(mp3_filename)

print(audiofile.tag.artist)
print(audiofile.tag.album)
print(audiofile.tag.album_artist)
print(audiofile.tag.title)
print(audiofile.tag.track_num)

audiofile.tag.artist = u"Integrity"
audiofile.tag.album = u"Humanity Is The Devil"
audiofile.tag.album_artist = u"Integrity"
audiofile.tag.title = u"Hollow"
audiofile.tag.track_num = 2

#audiofile.tag.save()
"""
