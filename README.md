# remove_date_stamp
### Python script to remove the date stamp added to file names by Windows File History.

I used to rely on Windows File History to back up the files on my computer. A while ago, I decided to change over to Linux. Instead of copying my files off the old computer, It's much easier to just use the copy that was created by File History. The problem is that there at least two versions of each file, and there is a date stamp added to the file name (it looks like this `Calander (2018_06_29 23_18_32 UTC).pub`). I wrote this Python 3.6 script to get rid of the duplicates and remove the date stamp.


###### Instructions for use:
* Open a terminal window in the scrip's directory.
* Enter `$ main.py`.
* Follow the onscreen instructions.

###### Notes:
* If you want to use a version of Python that is older than 3.6, You can just set `VERBOSE` to `FALSE`. The only part of 3.6 the script uses is `f strings`, which is only used to print the changes.
* This script will not work properly if the original file names contained parenthesis.