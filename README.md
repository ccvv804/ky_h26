# ky_h26

ffmpeg -i input.mp4 -f mp4 -vf "scale=1920:1080:flags=bicubic,setsar=1/1" -c:v libx264 -x264opts deblock=0,0:cabac:bframes=3:b-adapt=1:weightb:weightp=1:ref=1:scenecut=40:ipratio=1.4:pbratio=1.3:vbv-bufsize=15000:vbv-maxrate=7500:qcomp=0.60:rc-lookahead=10:mbtree:aq-mode=1:aq-strength=1:chroma-me:merange=16:me=hex:subme=2:direct=spatial:trellis=0:psy:dct-decimate:fast-pskip:deadzone-inter=21:deadzone-intra=11:videoformat=ntsc:colorprim=bt709:transfer=bt709:colormatrix=bt709 -preset medium -b:v 5000k -c:a copy -an -sn -map_metadata -1 -map_chapters -1 -profile:v high -r 29.97 -vsync cfr out.mp4

ffmpeg -i out.mp4 -vbsf h264_mp4toannexb -vcodec copy -an out.h264

h261.py out.h264
