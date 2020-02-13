import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ssh_installed(host):
    ssh = host.package("ssh")
    assert ssh.is_installed


def test_config_updated(host):
    config = host.file("/etc/ssh/sshd_config")
    assert config.exists
    assert config.contains("PasswordAuthentication no")
    assert config.contains("PermitRootLogin no")
