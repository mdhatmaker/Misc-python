from os import listdir, rename
from os.path import isfile, join
import re

def get_only_files(mypath):
    print "Getting filenames..."
    filenames = [f for f in listdir(mypath)]
    print "Filtering for only files (not folders)..."
    onlyfiles = [f for f in filenames if isfile(join(mypath, f))]
    return onlyfiles

def filter_starts_with(onlyfiles, starts_with_text):
    print "Filtering for filenames that start with '{0}'...".format(starts_with_text)
    filename_list = [f for f in onlyfiles if f.lower().startswith(starts_with_text)]
    return filename_list

def starts_with(mypath, text, fn_replace, perform_rename=False):
    print mypath
    print
    print "[performing rename]" if perform_rename else "[printing only--NOT renaming files]"
    print "filenames start with: '{0}'".format(text)
    print
    onlyfiles = get_only_files(mypath)
    filename_list = filter_starts_with(onlyfiles, text)
    print
    # Rename the movie filenames by replacing spaces with periods
    for f in filename_list:
        (f1, f2) = fn_replace(f)
        print "'{0}' --> '{1}'".format(f1, f2)
        # We want to rename f1->f2
        fullname1 = join(mypath, f1)
        fullname2 = join(mypath, f2)
        if perform_rename: rename(fullname1, fullname2)
    return

def replace_spaces_with_periods(f):
    f2 = f.replace(' ', '.')
    f2 = f2.replace('.-.', '.')
    f2 = f2.replace('..', '.')
    return (f, f2)

def rename_series_episodes(mypath, pattern, repl, perform_rename=False):
    print mypath
    print
    print "[performing rename]" if perform_rename else "[printing only--NOT renaming files]"
    #print "filenames start with: '{0}'".format(text)
    #print
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
            print "'{0}' --> '{1}'".format(f1, f2)
            # We want to rename f1->f2
            if perform_rename: rename(fullname1, fullname2)
    return

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


