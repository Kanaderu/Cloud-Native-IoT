#######################
Container Orchestration
#######################

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   docker-swarm
   kubernetes

In the previous sections discussing containers and compose files, the focus has been on running containers on a single host node system. Container orchestration, especially with the ease of using compose files, allows for easily spinning up multiple containers to work together of an application has really been covered. However, in orchestration, linking multiple nodes together is really the focus to allow for scaling containers across multiple systems to provide more compute capability to house a network of containers. The quick and simple path to orchestration is through Docker Swarm which extends the capability of docker compose files to apply to multiple nodes. In leveraging Docker Swarm, one can begin to notice some of the limitations of docker swarm within the nuances of orchestration. At that point, the transition to Kubernetes becomes more apparent to really begin to apply orchestration at scale.

In continuing to learn orchestration, it's important to understand how data is being stored and process. One of the key points within orchestration is how an application is to go about data persistence and how applications are configured.