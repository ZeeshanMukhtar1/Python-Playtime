import ffmpeg

# Replace 'input_file.mp4' with the path to your MP4 file
# Replace 'output_file.mp3' with the desired path and name for the output MP3 file
input_file = 'input_file.mp4'
output_file = 'output_file.mp3'

# Use ffmpeg to convert the MP4 file to MP3
ffmpeg.input(input_file).output(output_file, acodec='mp3').run()

print('Conversion complete!')
