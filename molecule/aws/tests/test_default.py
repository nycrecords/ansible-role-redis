import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_redis_config_exists(host):
    f = host.file("/etc/opt/rh/rh-redis5/redis.conf")

    assert f.exists
    assert f.user == "redis"
    assert f.group == "root"


def test_redis_running(host):
    redis = host.service("rh-redis5-redis")

    assert redis.is_running
    assert redis.is_enabled


def test_redis_listening(host):
    port = host.socket("tcp://127.0.0.1:6379")

    assert port.is_listening
