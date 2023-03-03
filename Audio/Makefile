INPUT_FOLDER = $(input)
OUTPUT_FOLDER = $(output)

INPUT_FILES = $(wildcard $(INPUT_FOLDER)/*.mp3)
OUTPUT_FILES = $(patsubst $(INPUT_FOLDER)/%.mp3,$(OUTPUT_FOLDER)/%.mp3,$(INPUT_FILES))

.PHONY: all

all: $(OUTPUT_FILES)

$(OUTPUT_FOLDER)/%.mp3: $(INPUT_FOLDER)/%.mp3
	@mkdir -p $(dir $@)
	ffmpeg -i $< -ac 1 -ar 11025 -b:a 32k -codec:a libmp3lame -qscale:a 2 $@
	@$(eval COUNT=$(if $(COUNT),$(shell echo $$(($(COUNT)+1))),0))
	mv $@ $(dir $@)/$${COUNT}.mp3