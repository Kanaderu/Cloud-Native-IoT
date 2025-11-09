##########
Containers
##########

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   docker-guide

Containers are a virtualization environment that is used deliver services/applications and their dependencies in a lightweight package. Containers have largely become popular through the popular tool, docker, and has been widely adopted due to its lightweight nature and ease of use. The rise of the use of containers has lead to a governing body called the `Open Container Initiative (OCI) <https://opencontainers.org/>`_ which has defined a set of standards/specifications for creating containers. OCI compliant tools follow the defined specifications and allows for other container technologies to work fairly seamless with one another. Containers are used for a variety of applications and services which include sidecar containers (largely for kubernetes), devcontainers (development environment), continuous integration/continuous deployment (CI/CD), and more. Docker and Podman will be used here as starting points into learning about and using containers.

-------------
Docker/Podman
-------------

Docker defines several common objects which are fairly common among most container platforms. These objects include:

- Images
- Containers
- Volumes
- Networks
- Nodes

Podman extends docker by adding rootless containers for improved security and redhat integration. Podman is developed to be a drop-in replacement for docker for easier transition from docker to podman. Additionally, podman supports pods for grouping containers together to support the transition to kubernetes.

Images
------

Images are frozen snapshots of a container that includes the application/services. Images are self-contained objects that are then saved off to a registry for distribution and deployment. Images are built using a set of instructions defined by a Dockerfile (docker) or Containerfile (podman) which defines the base image, dependencies, configurations, and commands for when the image is executed as a container. From these frozen snapshots, containers are executed and ran from a known state and are started here every time a container is executed.

Containers
----------

Containers are running instances of images that are executed on a node. Containers, when started, are isolated from the host system and exposing access to the host must be explicitly defined. Default resources available to containers are the CPU and memory of the host system to allow the container to run efficiently along with a default network interface to allow for internet communication. Containers, similar to virtual machines, can be started, stopped, paused, and deleted as needed. Data created within a container is ephemeral and will be lost when the container is deleted unless persistent storage is used. Various forms of persistent storage are defined by the use of volumes.

Volumes
-------

Volumes are persistent storage objects that are used to store data for a container. Volumes are initially created and then mounted to a container onto a specific mount location within the container. Since images store the state of a snapshot which always start from the same point when ran as a container, volumes enable data persistence across multiple runs of a container. 

.. note::
    When a running container is ran without any volumes, all the data is lost when the container exits. Volumes must be taken into consideration to avoid losing and valuable data from a container. Situations without volumes can be applicable if data persistence is not required such as, to make API calls, to run stateless servers, etc.

Networks
--------

Networks are virtual networks created by docker to facilitate networking communication across containers. The virtual networks allow containers to easily talk with one another if they are on the same network or create isolated containers for tightly managed interfaces.

Nodes
-----

Nodes define the host platform/system for which the containers are ran on. Nodes describe a more advanced topic around container orchestration in which multiple compute nodes contribute to running a set of containers. The use of orchestration provides scalability, redundancy, and management of allocating containers across multiple systems. The most common tools for orchestration are Docker Swarm, Kubernetes, and Hashicorp Nomad.

References
^^^^^^^^^^

- Docker Guides https://docs.docker.com/guides/
- Docker Manuals https://docs.docker.com/manuals/
- Open Container Initiative (OCI) https://opencontainers.org/
- OCI Spec https://github.com/opencontainers/image-spec
- Kubernetes https://kubernetes.io/
- Podman https://podman.io/
- Apptainer https://apptainer.org/
- Dev Containers https://containers.dev/
- Hashicorp Nomad https://developer.hashicorp.com/nomad