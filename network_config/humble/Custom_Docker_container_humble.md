## UB custom Docker-based ROS2 Humble environment

We have designed a University of Barcelona custom Docker-based ROS 2 Humble environment to simplify student access to ROS 2 and ensure platform-independent workflows in robotics courses.

A proper Docker Image has been created with the custom configuration on Dockerfile and uploaded to my DockerHub account (https://hub.docker.com/r/manelpuig/ros2-humble-biorobub-pc).

**Students** in the lab they only need to:
- Verify you have installed `Docker Engine` and `Docker Compose plugin` from the official Docker repositories. Open Docker Desktop on your Host PC.
- Open VScode in a working directory (e.g., `~/Desktop/rob/`) on your Host PC.
    - Install the `Docker` and `Remote Development` extensions from the VScode marketplace.
    - Clone your forked repository `ROS2_rUBot_tutorial`
- In `~/ROS2_rUBot_tutorial/network_config/humble` review on:
    - `docker-compose.yaml` file: 
        - `ROS_DOMAIN_ID=1` variable to match your Group number.
        - `ROS_STATIC_PEERS=192.168.1.14` variable to match your robot ID.
    - `cyclonedds_pc.xml` file: verify `<NetworkInterface name="wlp1s0"/>`.
- Open a terminal in `~/ROS2_rUBot_tutorial/network_config/humble` and run:
    ````bash
    xhost +local:root            # allow X11 for Docker (lab use only)
    docker compose up -d
    ````
- Verify the environment variables are correctly set by checking the container startup output.
- In Host VScode you can `attach VScode`. You can also connect with container typing:
    ```bash
    docker exec -it pc_humble bash
    code .                     # open VSCode inside the container
    ```
- Verify the `ROS_DOMAIN_ID` in container .bashrc

You are ready to work inside the container and to connect to the robot hardware within ROS2 Humble on Docker!

- To stop the container:
    ````bash
    docker compose down
    ````
- To see the Images and Containers:
    ````bash
    docker ps -a               # containers
    docker images              # images
    ````
