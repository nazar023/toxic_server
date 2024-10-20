ARG ROS_DISTRO=humble
FROM osrf/ros2:nightly-rmw-nonfree

# Install necessary packages for ROS2, colcon, and development
RUN apt-get update && apt-get install -y \
      tree \
      git \
      python3-colcon-common-extensions \
      ros-${ROS_DISTRO}-ament-cmake \
      ros-${ROS_DISTRO}-demo-nodes-cpp \
      ros-${ROS_DISTRO}-demo-nodes-py && \
    rm -rf /var/lib/apt/lists/*

# Clone specific branch of your repository
RUN mkdir -p ~/ros2 && \
    cd ~/ros2 && \
    git clone https://github.com/nazar023/toxic_server.git && \
    cd toxic_server && \
    colcon build --packages-select toxic_server toxic_relationship

