############
Docker Guide
############

Introduction
============

Diving into using docker is covered on this page. Podman can also be used which is designed to be a drop-in replacement for docker. Details about podman can be further found in the `redhat documentation <https://www.redhat.com/en/topics/containers/what-is-podman>`_ and `official podman documentation <https://podman.io/>`_. Docker or podman is assumed to be already installed.

.. note::
    To use ``podman`` instead of ``docker``, simply replacing the commands will suffice as it's intended to be a drop-in replacement. The initial installation of podman may alias the ``docker`` command to ``podman`` by redefining the docker socket environment variable ``DOCKER_HOST``.


Docker Architecture
-------------------

The docker architecture follows a server/client model in which a daemon is ran as a background service. The server is the docker host which runs a daemon (docker daemon) that will run all the commands. The docker client is commonly used which communicates via an API to the docker socket which is exposed by default to ``/var/run/docker.sock`` and can alternatively be exposed via TCP to communicate across networks. Running docker commands are running as a client that connects to the socket and communicates via the API. The docker registry is a repository of images which can be leveraged and built upon. To begin, view the information of the installed docker/podman instance.

.. code-block::
    :caption: View docker instance information

    docker info

.. note::
    Since the docker daemon is a service, managing the status/stop/start of the service can be done with ``systemctl`` or ``service`` commands. (ie; ``systemctl status docker``)

.. figure:: assets/docker-architecture.webp
    :alt: Docker Architecture
    :align: center

    Docker Architecture

.. note::
    Podman is daemon-less by design which does not rely upon a daemon. The daemon-less nature of podman is due to the ability to run containers at the root level (as opposed to docker which runs the daemon as root) which possess a security risk to allow containers to operate as root. Podman does, however, allow communication over a socket

Pulling an Image and Running a Container
========================================

Running a Container
-------------------

Diving right in, start by pulling an image:

.. code-block:: bash
    :caption: Pull and run a docker hello-world image

    # pull the hello-world image
    docker pull hello-world

    # view the docker images currently downloaded locally
    docker image ls

    # run the hello-world image as a running container
    docker run hello-world

In the commands above, the ``hello-world`` image is pulled from the default `Docker Hub <https://hub.docker.com/>`_ registry to the local registry. The local registry is stored and managed by the docker daemon as a local copy of the image. The local image registry is viewed with ``docker image ls`` which lists all the local images. The container is then executed by running ``docker run ...`` command which starts running a container from an image. The ``hello-world`` image simply echos a hello world statement and then exits.

The ``docker run`` command is heavily used and the documentation is a useful reference in starting out: https://docs.docker.com/reference/cli/docker/container/run/. When running the container without pulling the image, docker will search the registry to see if the image exists and will search/download the image from the registry if it doesn't. For example, running ``docker run godlovedc/lolcow`` will automatically pull the image and run it.


.. note::
    Images follow a notation of ``[registry_hostname[:port]/][namespace/]repository_name[:tag]`` which are also interpreted and stored on the registry appropriately. The ``registry_hostname`` defaults to ``docker.io`` which is Docker Hub, the main docker registry. Other registries can be specified such as redhat's `Quay.io <https://quay.io/>`_, `Nvidia Container Registry <https://catalog.ngc.nvidia.com/>`_, and `Github Container Registry <https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry>`_. The ``namespace`` and ``repository_name`` define the image itself and the ``tag`` is used to specify a particular version of the image.

Looking at a more practical use of containers run the following to run a specific version of python using tags.

.. code-block:: bash
    :caption: Run ``python-3.14`` with the ``alpine`` variant

    # Run python 3.14 built on-top of the alpine linux OS
    # --rm deletes the container after it exits (instead of stopping the container)
    # -it attaches the container to the current tty to make it interactive with the current shell
    docker run --rm -it python:3.14.0-alpine

    # >> import sys
    # >> sys.version
    # >> exit()

In this code block, an image of python 3.14 built on-top of the minimal OS of `Alpine Linux <https://www.alpinelinux.org/>`_ (~MB). However, the python image is a bare-bones implementation of python without any packages or add-ons. To add required dependencies, a new docker image can be created that builds upon the initial python image through the use of a Dockerfile.

Docker Commands
---------------

Before moving on, it's useful to highlight some common docker commands.

The common notation for commands follow

.. code-block:: text
    :caption: Docker command notation

    docker [MANAGEMENT_COMMAND] [COMMAND] [ARGUMENTS...]

- ``MANAGEMENT_COMMAND``: is optionally the docker object to interact with (``container``, ``volume``, ``network``, ``image``, ``node``, etc.)
- ``COMMAND``: is the command to run against the object
- ``OPTIONS``: are the various augments passed to the command itself

The ``docker run`` command is particularly important to look at as it follows as an alias to ``docker container run``.

.. code-block:: text
    :caption: ``docker run``

    docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

- ``OPTIONS``: are arguments to the ``docker container`` command
- ``IMAGE``: specifies which image to run
- ``COMMAND``: overwrites the default command set by the image to run within the container
- ``ARG``: overwrites additional arguments passed to the container's ``COMMAND``

References
^^^^^^^^^^

- Docker Guides https://docs.docker.com/guides/
- RedHat Containers https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/building_running_and_managing_containers/index