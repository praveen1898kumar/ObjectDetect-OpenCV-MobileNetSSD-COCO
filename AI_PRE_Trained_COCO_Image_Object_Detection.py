# %% [markdown]
# To Install import cv2
# import matplotlib.pyplot as plt

# %%
import cv2
import matplotlib.pyplot as plt

# %%
config_file = '/Users/praveen18kumar/Downloads/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = '/Users/praveen18kumar/Downloads/frozen_inference_graph.pb'


# %%
model = cv2.dnn_DetectionModel(frozen_model, config_file)

# %%
classLabels = []
file_name = '/Users/praveen18kumar/Downloads/labels.txt'  # Corrected the file name and removed extra spaces

with open(file_name, 'rt') as fpt:
    classLabels = fpt.read().rstrip('\n').split('\n')  # Corrected the syntax and indentation

# %%
print(classLabels)

# %%
print(len(classLabels))

# %%
model.setInputSize(320, 320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)


# %%
img = cv2.imread('/Users/praveen18kumar/Downloads/istockphoto-509011871-612x612.jpeg')

# %%
plt.imshow(img)

# %%
ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)

# %%
print(ClassIndex)


# %%
font_scale = 3
font = cv2.FONT_HERSHEY_PLAIN

for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
    cv2.rectangle(img, boxes, (255, 0, 0), 2)
    cv2.putText(img, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font, fontScale=font_scale, color=(0, 255, 0), thickness=3)


# %%
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))