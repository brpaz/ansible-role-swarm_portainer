# Ansible Docker Swarm Portainer Role

> An Ansible role to deploy [Portainer](https://portainer.io) service to a Docker Swarm cluster.

## Requirements

- Docker installed on the target machine
- Docker Swarm initialized on the target machine
- An overlay network for the swarm services

## Installation

### Using Ansible Galaxy

You can install this role directly from Ansible Galaxy:

```bash
ansible-galaxy install brpaz.swarm_portainer
```

### Using requirements.yml

For version-controlled, repeatable role installations, add to your `requirements.yml`:

```yaml
---
roles:
  - name: brpaz.swarm_portainer
    version: v1.0.0  # Specify the version you want

collections:
  - name: community.docker
```

Then install with:

```bash
ansible-galaxy install -r requirements.yml
```

### Manual Installation

Alternatively, you can clone the repository directly:

```bash
# Create a roles directory if it doesn't exist
mkdir -p ~/.ansible/roles
# Clone the repository
git clone https://github.com/brpaz/ansible-role-swarm-portainer.git ~/.ansible/roles/brpaz.swarm_portainer
```

## Role Variables

This role includes the following variables for configuration:

| Variable                         | Default Value            | Description                                                                   |
| -------------------------------- | ------------------------ | ----------------------------------------------------------------------------- |
| `portainer_image`                | `portainer/portainer-ce` | Portainer Docker image                                                        |
| `portainer_tag`                  | `2.30.1-alpine`          | Portainer image tag/version                                                   |
| `portainer_reservation_cpu`      | `0.1`                    | CPU reservation for the container                                             |
| `portainer_reservation_memory`   | `64M`                    | Memory reservation for the container                                          |
| `portainer_limit_memory`         | `256M`                   | Memory limit for the container                                                |
| `portainer_networks`             | `[]`                     | Additional networks to connect to                                             |
| `portainer_labels`               | `{}`                     | Additional Docker labels                                                      |
| `portainer_published_port_http`  | `9000`                   | HTTP port for Portainer. UI. Set to null if want to not expose the container  |
| `portainer_published_port_https` | `9443`                   | HTTPS port for Portainer. UI  Set to null if want to not expose the container |  |
| `portainer_network_mode`         | `ingress`                | Network mode for the container                                                |

## Portainer Configuration

### Resource Configuration

```yaml
portainer_reservation_cpu: 0.1
portainer_reservation_memory: "64M"
portainer_limit_memory: "256M"
```

### Network Configuration

```yaml
portainer_networks: []  # Add any additional networks here
portainer_network_mode: "ingress"
portainer_published_port_http: 9000
portainer_published_port_https: 9443
```

### Docker Container Configuration

You can add custom Docker labels:

```yaml
portainer_labels:
  custom.label: "value"
  another.label: "another-value"
```

## Example application

To expose Portainer through Traefik, you can use the following labels in your service definition:

```yaml
version: '3.8'
services:
  portainer:
    image: portainer/portainer-ce:2.30.1-alpine
    deploy:
      labels:
        - "traefik.enable=true"
        - "traefik.http.routers.portainer.rule=Host(`example.com`)"
        - "traefik.http.routers.portainer.entrypoints=websecure"
        - "traefik.http.routers.portainer.tls.certresolver=letsencrypt"
        - "traefik.http.services.portainer.loadbalancer.server.port=8000"
```

## Example Playbook

```yaml
- hosts: swarm_manager
  vars:
    portainer_tag: "2.30.1-alpine"
    portainer_reservation_memory: "128M"
    portainer_limit_memory: "512M"
    portainer_published_port_http: 9000
    portainer_published_port_https: 9443
    portainer_labels:
      traefik.enable: "true"
      traefik.http.routers.portainer.rule: "Host(`portainer.example.com`)"
  roles:
    - brpaz.swarm_portainer
```

## Role Dependencies

- [community.docker](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html) collection

## Contribute

All contributions are welcome. Please check [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

## 🫶 Support

If you find this project helpful and would like to support its development, there are a few ways you can contribute:

[![Sponsor me on GitHub](https://img.shields.io/badge/Sponsor-%E2%9D%A4-%23db61a2.svg?&logo=github&logoColor=red&&style=for-the-badge&labelColor=white)](https://github.com/sponsors/brpaz)

<a href="https://www.buymeacoffee.com/Z1Bu6asGV" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## License

This project is MIT Licensed [LICENSE](LICENSE)

## 📩 Contact

✉️ **Email** - [oss@brunopaz.dev](oss@brunopaz.dev)

🖇️ **Source code**: [https://github.com/brpaz/ansible-role-swarm-portainer](https://github.com/brpaz/ansible-role-swarm-portainer)
