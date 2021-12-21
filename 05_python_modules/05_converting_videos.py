'''
    → Converting videos with FFmpeg

    https://ffmpeg.org/documentation.html
    https://ffmpeg.org/download.html

    https://ffmpeg.zeranoe.com/builds/
'''

import os
import fnmatch
import sys

if sys.platform == 'linux':
    ffmpeg_command = 'ffmpeg'
else:
    ffmpeg_command = r'FFmpeg\bin\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'
debug = ''

source_path = '/dev/python/utilities_python/05_python_modules/media'
path_destination = '/dev/python/utilities_python/05_python_modules/media/new_videos'

for root, folders, files in os.walk(source_path):
    for file in files:
        if not fnmatch.fnmatch(file, '*.mp4'):
            continue

        full_path = os.path.join(root, file)
        file_name, file_extension = os.path.splitext(full_path)
        caption_path = file_name + '.srt'

        if os.path.isfile(caption_path):
            input_caption = f'-i "{caption_path}"'
            map_caption = '-c:s srt -map v:0 -map to -map 1:0'
        else:
            input_caption = ''
            map_caption = ''

        file_name, file_extension = os.path.splitext(file)

        new_file_name = file_name + '_NEW' + file_extension
        output_file = os.path.join(root, new_file_name)

        command = f'{ffmpeg_command} -i "{full_path}" {input_caption} ' \
            f'{codec_video} {crf} {preset} {codec_audio} {bitrate_audio} ' \
            f'{debug} {map_caption} "{output_file}"'

        os.system(command)