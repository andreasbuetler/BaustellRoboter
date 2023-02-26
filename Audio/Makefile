# This converts a audio file to a compressed mp3 file below 450kb
INPUT_FILE = $(input)
OUTPUT_FILE = $(basename $(INPUT_FILE))_compressed.mp3

$(OUTPUT_FILE): $(INPUT_FILE)
	ffmpeg -i $(INPUT_FILE) -ar 8000 -codec:a libmp3lame -b:a 64k -ac 1 -fs 400k $@
