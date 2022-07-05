# pibic-emotion-classification

Repo for my research project on real-time face recognition and emotion classification using a camera.

# The Project

PIBIC: **P**rograma **I**nstitucional de **B**olsas de **I**niciação **C**ientífica - Research Project at *Universidade Federal do ABC* (UFABC), in Brazil. Official paper number 01/2019, voluntary. This project was developed alongside the research PIE633-2020 from UFABC: "*Análise de requisitos linguístico-computacionais em interfaces presenciais homem-máquina*".

Supervisor: Dr. João Henrique Ranhel Ribeiro.

It is important to note that this project was developed in 2019-2020 and possibly may not be repeated today in the same method.

The full report in portuguese can be found in the repo, along with codes. This is just a simplified explanation.

## Objective

Automate real-time facial expression recognition, integrating with the video and audio annotation tool <a href="https://archive.mpi.nl/tla/elan" title="https://archive.mpi.nl/tla/elan">ELAN</a>. Through this integration, establish real-time emotion classification through multimodal interaction of video and audio.

## Development

A large part of this research was focused on studying and testing facial recognition and emotion classification processes and methods, such as *YOLO* (You Only Look Once), *CNN* (Convolutional Neural Network), *LBP* (Local Binary Patterns) and *HOG* (Histogram of Oriented Gradientes). Afterwards, it was decided that the ideal method was through the toolkit <a href="https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html" title="https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html">Intel(R) Distribution of OpenVINO toolkit</a>.

This toolkit used *Haar Feature-Based Cascade* and *Histogram of Oriented Gradientes* descriptors to classify images, in an optimized manner. The application <a href="https://docs.openvino.ai/latest/omz_demos_interactive_face_detection_demo_cpp.html" title="https://docs.openvino.ai/latest/omz_demos_interactive_face_detection_demo_cpp.html">Interactive Face Detection C++ Demo</a> allowed us to idetify human faces, as well as head orientation, facial traces, biological sex and emotion on each face, trained from the dataset <a href="http://mohammadmahoor.com/affectnet/" title="http://mohammadmahoor.com/affectnet/">AffectNet</a>.

This application is very good, although it only classifies 5 emotions (neutral, happy, sad, surprised, angry) instead of the 7 universal emotions defined by <a href="https://www.paulekman.com/universal-emotions/" title="https://www.paulekman.com/universal-emotions/">Paul Ekman</a>.

By running this toolkit on each frame from the input camera, it was possible to detect faces and classify their emotion in real-time.

![Example of the output of the application, with identified information from a human face](/images/openvino-detect.png "OpenVINO detecting my information in real-time")

By altering the output of the application, it was possible to display the emotion detected in each frame in a text format, and, afterwards, display in text format the frames in which the emotion changed. The notation used in this was "*frame_number*,*new_emotion*"; where the 5 emotions where *n* (neutral), *h* (happy), *t* (sad), *s* (surprised), *a* (angry), and *0* (unidentified).

![Example of the text output showing each frame where the emotion changed](/images/txt-emotions.png "Text output with frames in which emotion changed")

This notation could be treated as a track in ELAN, allowing for frame by frame comparison of the emotion classification obtained in this project and the emotion classification from a specialist obtained from viewing the video.

## Results

The comparison of the emotion classification obtained in this project and the classification of a specialist showed that the automated emotion classification was close to what humans would consider. This way it was possible to develop and automated process for identifying emotion in real-time and saving it as a track in ELAN for video-audio emotion analysis (part of the other project related to this one).

