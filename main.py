import shutil, os.path, re
REGEX_SEASON_AND_EPISODE = re.compile("S\d{1,2}\BE\d{1,2}", re.IGNORECASE)

showFolders = next(os.walk('.'))[1];
for folder in showFolders:
    seasonAndEpisode = REGEX_SEASON_AND_EPISODE.search(folder);
    if seasonAndEpisode is not None and seasonAndEpisode[0] is not None:
        showName = folder.split(seasonAndEpisode[0])[0].replace(".", " ")
        desiredFileName = showName + seasonAndEpisode[0] + ".mkv"
        desiredFileDestination = f'.\\{showName.rstrip()}'
        filteredFilesToManipulate = [f for f in next(os.walk('.\\' + folder))[2] if ".mkv" in f]

        if not os.path.exists(desiredFileDestination):
            os.makedirs(desiredFileDestination)

        shutil.copy(f'.\\{folder}\\{filteredFilesToManipulate[0]}', f'{desiredFileDestination}\\{desiredFileName}')
        print(f'Copied {desiredFileDestination}\\{desiredFileName}')
    else:
        print(folder + " doesn't contain season/episode, skipping")
