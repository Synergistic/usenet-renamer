# usenet-renamer
 A simple script used for bulk-renaming items downloaded from usenet.

Given a collection of folders

    ├── ShowA.S1E1.ASDF
    │   ├── 7kjhsadf.mkv          
    ├── ShowA S3E12 XYZ
    │   ├── afg3fasdf.mkv          
    ├── ShowB S02E22
    │   ├── d2q3dg34.mkv          
    ├── ShowC.S01E10.ABC
    │   ├── faf3325g.mkv          
    └── ...

This script will use the show name and season/episode identifier to rename the .mkv file contained within the folder.

    ├── ShowA                
    │   ├── ShowA S1E1.mkv          
    │   ├── ShowA S3E12.mkv          
    ├── ShowB  
    │   ├── ShowB S02E22.mkv          
    ├── ShowC  
    │   ├── ShowC S01E10.mkv          
    └── ...


Copy main.py to the root directory containing all your folders, then execute using ```py main.py```


Notes:
 - Folder names MUST contain "S#E#" or they will be skipped
 - Folders must contain a .mkv file
 - If multiple .mkv files are present only the first one will be renamed
