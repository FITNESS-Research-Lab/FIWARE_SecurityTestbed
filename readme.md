
# Building Your Own Security Testbed with FIWARE

## Description
This repository enables users to set up an environment for building a security testbed with a digital twin via FIWARE. It integrates technologies like Orion Context Broker, from FIWARE, KAFKA and OpenSearch, offering a streamlined setup process through Docker Compose. This testbed is ideal for experimenting with security scenarios in a controlled, customizable setting.

## Table of Contents
- [Requisites](#Requisites)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

### Requisites

#### **Environment**
It is not mandatory but highly recommended to use a x86 system architecture.


#### **Docker and Docker Compose**
Follow these detailed instructions to install Docker and Docker Compose on your machine:
- **Docker**: [Docker Installation Guide](https://www.docker.com/get-started)
- **Docker Compose**: [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

To check if Docker Compose is installed:
```shell
docker compose --version
```
#### **Basic Knowledge of FIWARE Smart Data Models**
FIWARE smart data models provide a standardized framework, allowing data interoperability across diverse applications. They establish a common ground for various entities and systems to communicate seamlessly.

A smart data model comprises four key elements. These include the schema, defining technical data types and structure; a written document specifying details; a URI with a functional URL offering basic information about the attribute or entity; and payload examples for both NGSIv2 and NGSI-LD versions.

For more information, please refere to the following documentation:
- FIWARE smart data model principles and general guidelines -> `https://fiware-datamodels.readthedocs.io/en/stable/howto/index.html/`
- NGSIv2 vs NGSI-LD ->  `https://fiware-datamodels.readthedocs.io/en/stable/ngsi-ld_howto/`


### Setting up the Environment
Clone the repository and navigate to the directory:
```shell
git clone https://github.com/your-username/your-project.git
cd your-project
```

## Usage
Here's how to get started with the testbed:
1. **Starting the Testbed**: In the project folder, run the following command:
   ```shell
   docker compose up -d
   ```
   This command starts all the services defined in the Docker Compose file. In particular, the full architecture deployed is the following:
   ![Example Image](asset/sample_architecture.png)


    1. **Devices**: The base of the architecture, these are the hardware components or sensors deployed in the field that generate data such as measurements and status updates.

    2. **Context Broker (Orion)**: At the core of the FIWARE platform, the Orion Context Broker aggregates data from the devices and maintains the current system state or "context." It enables the creation of a digital twin by reflecting the real-time status of the devices digitally.

    3. **KAFKA**: Acting as the central data bus, KAFKA manages the stream of data updates from the Context Broker. It decouples the production of data from its consumption, enabling flexibility and scalability in processing and analyzing data streams.

    4. **Zookeeper**: This service coordinates and manages the KAFKA cluster, ensuring that the data streams are stable and reliable.

    5. **Connector**: This serves as a bridge between the Orion Context Broker and KAFKA, formatting and directing the flow of device data onto the KAFKA bus.

    6. **External Applications**: These can be analytics tools, other services, or applications that consume data from KAFKA topics, process it, and potentially take actions or provide insights.

    7. **Logstash**: A data processing component that ingests data from KAFKA, processes it as needed, and then forwards it to OpenSearch.

    8. **OpenSearch**: A powerful search and analytics engine used to index, search, and analyze the data for insights. It facilitates quick data retrieval and real-time analysis.

    9. **Grafana**: A tool for data visualization and monitoring, which connects to OpenSearch to create dashboards that graphically represent the data analytics results.

    Devices produce data that is managed by the Orion Context Broker, which then updates the KAFKA bus through subscriptions,  a subscription in this context is a mechanism by which the Context Broker can notify other components when changes occur. For example, when a device updates its status, the Context Broker can inform other interested parties (like analytics tools or databases) about this change. External applications consume this data for further processing, analysis, or visualization, using tools like OpenSearch and Grafana.

2. **Accessing Services**: 
It is possible to access some services reaching the following links:
   - Grafana dashboard is available at `http://localhost:3000/`
   - OpenSearch is available at `http://localhost:9200/`

   To handle the interaction with the Orion Context Broker and to build the digital twin please refere to the following links:
   - Orion-LD Reference Material at `https://ngsi-ld-tutorials.readthedocs.io/en/latest/ngsi-ld-operations.html`

   To understand the Kafka publish-subscribe mechanism following the link below:
   - Kafka Refrence Material at `https://www.confluent.io/learn/publish-subscribe/`
   
   In this repository, you will not find any device simulator, we strongly recommend to build your own simulated environment.

## Getting Started
In this guide you will be able to build your own security testbed with a simplified example. In particular:

- You will understand the concept of FIWARE smart data models

- You will set up your digital twin

- You will create a simple dashboard for visualizating devices measurements

### Entities Management in Orion Context Broker

The first entity that we are going to create is a temperature sensor. This can be done using a simple POST http requesto to Orion Context Broker:

```shell
   curl --location 'http://localhost:1026/ngsi-ld/v1/entities/' \
--header 'Content-Type: application/json' \
--header 'Link: <http://context/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
--header 'Ngsild-Tenant: basetopic' \
--data '{
    "id": "urn:ngsi-ld:TemperatureSensor:001",
    "type": "TemperatureSensor",
    "category": {
        "type": "Property",
        "value": "sensor"
    },
    "temperature": {
        "type": "Property",
        "value": 25,
        "unitCode": "CEL"
    }
}'

   ```

We can retrieve the entity that has been created using a GET http request:

```shell
curl --location 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:TemperatureSensor:001' \
--header 'Link: <http://context/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
--header 'Ngsild-Tenant: basetopic'

   ```


Now that we have the entity, we want to be able to modify values of the sensor, simulating a change in the measurament values, we can do this with a PATCH http reuqest:

```shell
curl --location --request PATCH 'http://localhost:1026/ngsi-ld/v1/entities/urn:ngsi-ld:TemperatureSensor:001/attrs' \
--header 'Content-Type: application/json' \
--header 'Link: <http://context/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"' \
--header 'Ngsild-Tenant: basetopic' \
--data '{
    "temperature": {
        "type": "Property",
        "value": 689,
        "unitCode": "CEL"
    }
}'

   ```


```shell

   ```



### Enabling Grafana Visualization trough OpenSearch

## Contributing
We welcome contributions! Please read our [Contributing Guidelines](LINK_TO_CONTRIBUTING_GUIDELINES) for more information on how to report issues, submit pull requests, and contribute to the code.

## License
This project is licensed under the [YOUR LICENSE NAME](LINK_TO_LICENSE).

## Contact
For any queries or further information, please contact [YOUR EMAIL/CONTACT INFORMATION].

---

#### Docker Compose Configuration Explained
Here's a brief overview of each service in the `docker-compose.yml`:

- `fiware_connector`: Connects FIWARE components, accessible on port 2020.
- `orion`: FIWARE Orion context broker, listens on port 1026.
- `mongo-db`: MongoDB service for data persistence, exposed on port 27017.
- ...

(Remainder of the Docker Compose services with brief explanations)
