import sys
from os import listdir, rename
from os.path import isfile, join, isdir
import re

def get_only_files(mypath):
    print("Getting filenames...")
    filenames = [f for f in listdir(mypath)]
    print("Filtering for only files (not folders)...")
    onlyfiles = [f for f in filenames if isfile(join(mypath, f))]
    return onlyfiles

def filter_starts_with(onlyfiles, starts_with_text):
    print("Filtering for filenames that start with '{0}'...".format(starts_with_text))
    filename_list = [f for f in onlyfiles if f.lower().startswith(starts_with_text)]
    return filename_list

def starts_with(mypath, text, fn_replace, perform_rename=False):
    print(mypath)
    print()
    print("[performing rename]" if perform_rename else "[printing only--NOT renaming files]")
    print("filenames start with: '{0}'".format(text))
    print()
    onlyfiles = get_only_files(mypath)
    filename_list = filter_starts_with(onlyfiles, text)
    print()
    # Rename the movie filenames by replacing spaces with periods
    for f in filename_list:
        (f1, f2) = fn_replace(f)
        print("'{0}' --> '{1}'".format(f1, f2))
        # We want to rename f1->f2
        fullname1 = join(mypath, f1)
        fullname2 = join(mypath, f2)
        if perform_rename: rename(fullname1, fullname2)
    return

def insert_at_beginning_tickers(f):     # fn_replace(f)
    if f.startswith('_'):
        f2 = "tickers" + f
    else:
        f2 = f
    return (f, f2)

def replace_spaces_with_periods(f):     # fn_replace(f)
    f2 = f.replace(' ', '.')
    f2 = f2.replace('.-.', '.')
    f2 = f2.replace('..', '.')
    return (f, f2)

def rename_series_episodes(mypath, pattern, repl, perform_rename=False):
    print(mypath)
    print()
    print("[performing rename]" if perform_rename else "[printing only--NOT renaming files]")
    #print("filenames start with: '{0}'".format(text))
    #print()
    onlyfiles = get_only_files(mypath)
    #filename_list = filter_starts_with(onlyfiles, text)
    filename_list = onlyfiles
    print
    # Rename the tv episode filenames with appropriate "SxxEyy" naming convention
    for f1 in filename_list:
        f2 = re.sub(pattern, repl, f1, re.M|re.I)
        fullname1 = join(mypath, f1)
        fullname2 = join(mypath, f2)
        if fullname1 != fullname2:
            print("'{0}' --> '{1}'".format(f1, f2))
            # We want to rename f1->f2
            if perform_rename: rename(fullname1, fullname2)
    return

def remove_from_filename(mypath, pattern, perform_rename=False):
    files = get_only_files(mypath)
    for f in files:
        i1 = f.find(pattern)
        if (i1 >= 0):
            f2 = f.replace(pattern, "")
            print(f2)
            if perform_rename: rename(join(mypath, f), join(mypath, f2))
    return

def remove_from_subdir_filename(mypath, textToReplace, replaceWith="", perform_rename=False):
    onlydirs = [f for f in listdir(mypath) if isdir(join(mypath, f))]
    for d in onlydirs:
        #print('Checking folder %s for "%s"' % (d, textToReplace))
        subdir = join(mypath, d)
        onlyfiles = [f for f in listdir(subdir) if isfile(join(subdir, f))]
        for f in onlyfiles:
            f2 = f.replace(textToReplace, replaceWith)
            if (f2 != f):
                print('  "%s" --> "%s"' % (f, f2))
                if perform_rename: rename(join(subdir, f), join(subdir, f2))
    return

# Rename "Episode N" and "Episode NN" to "Scorpion.S03E0N" and "Scorpion.S03ENN" format
# Useful when folder contains filenames like "Episode 1.mp4", "Episode 2.mkv", ..., "Episode 10.mp4", ...
def rename_scorpion_season(mypath, prefix="Scorpion.S03E", perform_rename=False):    
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for f in onlyfiles:
        #print(f)
        #f1 = "Life On Top -02- Shoegasm.avi"
        f3 = re.sub(r'Episode (\d{2})', prefix + r'\1', f, re.M|re.I)
        if (f3 != f):
            print(f3)
            if perform_rename: rename(join(mypath, f), join(mypath, f3))
            continue
        f2 = re.sub(r'Episode (\d{1})', prefix + r'0\1', f, re.M|re.I)
        if (f2 != f):
            print(f2)
            if perform_rename: rename(join(mypath, f), join(mypath, f2))
    return

# search for torrents
# https://thepiratebay.org/search/riverdale/0/99/0

################################################################################

# Path of the Movie filenames:
movies_path = r"Z:\Shared Videos\MOVIES"

# Rename movie filenames to replace spaces with periods
#starts_with(movies_path, 'the ', replace_spaces_with_periods)    #, True)
#starts_with(movies_path, 'a ', replace_spaces_with_periods) #, True)


# Path of the TV Series filenames:
tv_series_path = r"D:\Users\mhatmaker\Downloads\torrents\COMPLETED_TORRENTS\Co-Ed Confidential Season 2 Part 1"

# Sample regex search/replace
#f1 = "Life On Top -02- Shoegasm.avi"
#print re.sub(r' -(\d{2})- ', r'.S01E\1.', f1, re.M|re.I)

# For example, replace ' -02- ' with '.S01E02.'
#rename_series_episodes(tv_series_path, r' - (\d{2}) - ', r'.S02E\1.', True)

# For example, replace ' - 102 - ' with '.S01E02.'
#rename_series_episodes(tv_series_path, r' - (\d{1})(\d{2}) - ', r'.S0\1E\2.', False)


###################################### Specific Single-Use Renaming Code ###############################################
completed_path = r"D:\Users\mhatmaker\Downloads\torrents\COMPLETED_TORRENTS"



sys.exit()

#-----------------------------------------------------------------------------------------------------------------------
perform_rename = True

# Remove "WwW.SeeHD.PL_" from filenames in a specific folder (and subfolders)
remove_from_subdir_filename(completed_path, "WwW.SeeHD.PL_", "", perform_rename)

# Clean up filenames of rDX movies
remove_from_subdir_filename(completed_path, "18+ ", "", perform_rename)
remove_from_subdir_filename(completed_path, " ☻rDX☻", "", perform_rename)

# Remove "Crazy4TV.com - " from filenames in a specific folder
_path = join(completed_path, "Legion Season 1 S01 1080p 6CH BluRay x265-HETeam")
remove_from_filename(_path, "Crazy4TV.com - ", False)

# Rename Scorpion episodes from format like "Episode 1.mp4"
rename_scorpion_season(join(completed_path, "Scorpion S03 Season 3 Complete HDTV x264-EVO"), "Scorpion.S03E", False)

# Remove "-w1nt3r" from filenames
remove_from_filename(join(completed_path, "scorpion.season.2.complete"), "-w1nt3r", True)

# Add "tickers" to beginning of tickers files that mistakenly only begin with "_"
crypto_path = r"D:\Users\mhatmaker\Dropbox\alvin\data\DF_CRYPTO"
starts_with(crypto_path, "_", insert_at_beginning_tickers, perform_rename=True)

