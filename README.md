# NGINX Load Balancing Algorithms Demo

This repository contains a demonstration of various load balancing algorithms used in NGINX for distributing incoming client requests among backend servers.

## Overview

NGINX is a powerful and popular web server and reverse proxy that can be used as a load balancer to distribute client requests across multiple backend servers. It offers several load balancing algorithms, each with its strengths and use cases.

This demo provides a simple setup to showcase how each of these algorithms works and how they affect the distribution of client requests.

> **Stage-1**: Implemation of Round Robin Algorithm using Flask.

> **Stage-2**: Upcoming...

## Load Balancing Algorithms

1. **Round Robin**: Distributes requests evenly across all backend servers in a circular manner.

2. **Least Connections**: Directs a new request to the server with the fewest active connections.

3. **IP Hash**: Uses a hash of the client's IP address to determine which server should receive the request, ensuring the same client is always directed to the same backend server.

4. **Weighted Round Robin**: Similar to Round Robin but allows assigning different weights to each backend server to control the proportion of traffic each server receives.

5. **Weighted Least Connections**: Similar to Least Connections but allows assigning different weights to each backend server.

## Docker Compose Setup

To make it easier for users to run the demonstration, this repository includes Docker Compose support.

### Prerequisites

- Install Docker and Docker Compose on your system. Refer to the [official Docker documentation](https://docs.docker.com/get-docker/) for installation instructions specific to your OS.

### Clone the Repository

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/yadav-vikas/nginx-load-balancer-algorithms.git
   ```
### Run the Demo with Docker Compose

1. Open a terminal and navigate to the root directory of the cloned repository:

   ```bash
   cd nginx-load-balancer-algorithms
   ```
2. Use Docker Compose to build and start the application:

   ```bash
   docker-compose up -d
   ```

   This command will create and start the necessary containers, including NGINX and the backend servers with the specified load balancing algorithm.

3. Open you web browser to send HTTP requests to [http://localhost:1337](http://localhost:1337). Observe how the different load balancing algorithms distribute the requests among backend servers.

4. To stop the demo, run the following command:

   ```bash
   docker-compose down
   ```

   This will stop and remove the containers and associated resources.

## Helpful Links

Here are some useful links for understanding NGINX load balancing and its algorithms:

- [NGINX Official Documentation on Load Balancing](https://docs.nginx.com/nginx/admin-guide/load-balancer/)
- [NGINX Load Balancing Methods](https://docs.nginx.com/nginx/admin-guide/load-balancer/http-load-balancer/)
- [NGINX Load Balancing Algorithms Explained](https://www.digitalocean.com/community/tutorials/understanding-nginx-http-proxying-load-balancing-buffering-and-caching)

## Contributions

Contributions to this demo repository are welcome! If you have ideas to improve the demonstration or additional load balancing algorithms to showcase, feel free to create pull requests.

## License

This demo repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
