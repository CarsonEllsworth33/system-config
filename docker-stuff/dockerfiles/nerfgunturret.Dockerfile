FROM ros:latest
RUN mkdir -p "/opt/ros_ws/src"
RUN apt update && apt install -y cmake g++ wget unzip

# Python dev files and numpy install
RUN apt install -y python3-dev python3-numpy

# Download and unzip opencv
WORKDIR /opt
RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
RUN unzip opencv.zip
RUN unzip opencv_contrib.zip
RUN rm opencv.zip
RUN rm opencv_contrib.zip
WORKDIR ./opencv-4.x

# Make build dir
RUN mkdir -p build
WORKDIR ./build

# Configure
RUN cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.x/modules ../../opencv-4.x

# Build
RUN cmake --build .
RUN make install

# Change directory back to root
WORKDIR /
# Delete apt cache
RUN rm -rf /var/cache/apt/archives
      
