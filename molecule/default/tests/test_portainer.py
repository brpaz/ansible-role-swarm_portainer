import testinfra


def test_portainer_container_running(host):
    """Test if the Portainer service is running and enabled."""
    cmd = host.run(
        "docker service ls --filter name=portainer --format '{{.Name}} {{.Replicas}}'"
    )
    assert cmd.rc == 0
    assert "portainer" in cmd.stdout
    assert "1/1" in cmd.stdout


def test_portainer_container_healthy(host):
    """Test if the Portainer container is healthy."""
    cmd = host.run("docker ps --filter name=portainer --format '{{.Names}}'")
    assert cmd.rc == 0
    container_name = cmd.stdout.strip()
    assert container_name != ""

    inspect = host.run(
        f"docker inspect --format='{{{{.State.Health.Status}}}}' {container_name}"
    )

    assert inspect.stdout.strip() == "healthy"


def test_portainer_accessible_on_host_network(host):
    """Test if Portainer is accessible via HTTP and HTTPS."""
    http_port = 9000

    http_response = host.run(
        f"curl -s -o /dev/null -w '%{{http_code}}' http://localhost:{http_port}"
    )

    assert http_response.stdout.strip() == "200"
