#from ultralytics import YOLO

#model= YOLO("models\yolo5_best.pt")
#result = model.predict('input_videos\input_video.mp4', save=True)

lines = [
            (0, 2),
            (4, 5),
            (6,7),
            (1,3),
            
            (0,1),
            (8,9),
            (10,11),
            (10,11),
            (2,3)
        ] 

for line in lines:
    print(line[0]*2)
    print(line[0]*2+1)
    print(line[1]*2)
    print(line[1]*2+1)