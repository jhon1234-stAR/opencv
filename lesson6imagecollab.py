import os
import cv2
from PIL import Image

folder = r"C:\Users\rache\OneDrive\Desktop\opencv\images"

exts = ( '.jpg','.jpeg','.png','.webp')

fps = 1
#collet imagws abs sort

files = sorted ([f for f in os.listdir(folder) if f.lower().endswith(exts)])

if not files:

    raise SystemExit("no images found!")

# compute mean sizer over file images
total_W = total_H = 0

for f in files:
    with Image.open(os.path.join(folder,f)) as im:

        w , h =im.size
        total_W += w; total_H +=h

mean_w = total_W // len(files)

mean_h = total_H // len(files)


resize_folder=os.path.join(folder,"resized")

os.makedirs(resize_folder,exist_ok=True)

resize_files = []


for f in files:

    with Image.open(os.path.join(folder,f))as im:
        im = im.convert('RGB')

        im_resized = im.resize((mean_w,mean_w),Image.Resampling.LANCZOS)

        outname = os.path.splitext(f)[0] + '.jpg'

        outpath = os.path.join(resize_folder, outname)

        im_resized.save(outpath,"JPEG",quality=95)

        resize_files.append(outname)




   

#create video
out_vidio = os.path.join (folder , "MYfirstvidio.mp4")

first_frame = cv2.imread(os.path.join(resize_folder, resize_files[0]))

h , w = first_frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
vidio = cv2.VideoWriter(out_vidio, fourcc , fps , (w,h))

for f in files :
    frame = cv2.imread(os.path.join(resize_folder, f ))
    if frame is None:
        continue
    vidio.write(frame)

vidio.release()


