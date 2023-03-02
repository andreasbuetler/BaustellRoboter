# This converts a audio file to a compressed mp3 file below 450kb
INPUT_FILE = $(input)
OUTPUT_FILE = $(basename $(INPUT_FILE))_compressed.mp3

$(OUTPUT_FILE): $(INPUT_FILE)
	ffmpeg -i $(INPUT_FILE) -ac 1 -ar 11025 -b:a 32k -codec:a libmp3lame -qscale:a 2 $@
