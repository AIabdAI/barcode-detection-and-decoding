from detect import Detect
from decode import Decode
import matplotlib.pyplot as plt
def show_image(title, img, cmap='gray'):
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()
    
    
    
    
import cv2
images =["05102009081.jpg","barcode.jpg","1612547890639.jpg","multiple.jpg","bar1.jpg"]
if __name__ == "__main__":    
    for ima in images:
        dt = Detect(ima)
        candidates,bn = dt.detect()
        show_image("orgenal image", dt.image)
        show_image("bainary & erosion image", bn)


        
        for i in range(len(candidates)):
            
            #img = cv2.imread("WebTWAINImage.bmp")
            
            candidate = candidates[i]
            decode =Decode()
            ean13, is_valid, thresh =decode.decode(candidate["cropped"])
            if is_valid:
                print("Detected code:",ean13)
                show_image(str(i), thresh)
