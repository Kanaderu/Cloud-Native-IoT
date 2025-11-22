############
Docker Swarm
############

.. note::
    Understanding of docker compose and the basic Docker objects are assumed to be known before covering Docker Swarm. It is recommended to review the `practical-docker-guide <../docker/practical-docker-guide.rst>`_ and `orchestration/index <../orchestration/index.rst>`_ prior to continuing here.

.. note::
    No additional installation is required to use Docker Swarm! Docker Swarm is included as part of the standard docker installation.

To begin docker swarm, additional objects are introduced to handle orchestration across multiple nodes. These objects include:

- Nodes
- Swarm
- Stacks
- Services

-----
Nodes
-----

Nodes are objects that define the host system which participates in the swarm. Nodes can either be a manager node or a worker node. The manager node has the responsibility of managing the swarm, allocating services, and handling networking between the nodes. The worker nodes are responsible for running the services that are allocated to them by the manager node. Nodes can be added or removed from the swarm as needed to scale the swarm up or down. Both manager and worker nodes can run docker containers, however, manager nodes are the only nodes that have permissions to manage running the swarm.

-----
Swarm
-----

The swarm is the overall orchestration object that defines the collection of nodes that are participating in the swarm. The swarm is initialized on a manager node which then generates a join token for worker nodes to join the swarm. The swarm manages the allocation of services across the nodes and handles the networking between the nodes to allow for communication.

A swarm requires at least one manager node to be running in the swarm. Additional manager nodes can be added to provide redundancy and high availability for the swarm management. When a manager node fails, another manager node can take over the management of the swarm. Manager nodes maintain quorum to ensure that the swarm remains consistent and available which, under the hood, applies the Raft consensus algorithm. An odd number of manager nodes is recommended to avoid split-brain scenarios.

.. .. toctree::
..    :maxdepth: 2
..    :caption: Contents:

..    docker-swarm-setup
..    docker-swarm-services
..    docker-swarm-networks
..    docker-swarm-volumes