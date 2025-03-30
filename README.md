# bad_apple_py
# To run the program
you will need to extract frames from the video, to do this i used ffmpeg in WSL 
# use the commands
      mkdir frames
      cd frames
      ffmpeg -i bad-apple.mp4 -vf fps=30 -frames:v 300 output_frames_%04d.jpeg
then import the folder in windows
			
