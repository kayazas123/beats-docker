from .fixtures import beat
import os


def test_binary_file_version(Command, beat):
    version_string = '%s version %s (amd64), libbeat %s' \
                     % (beat.name, beat.version, beat.version)
    command = Command('%s --version' % beat.binary_file.path)
    assert command.stdout.strip() == version_string


def test_binary_file_permissions(beat):
    assert beat.binary_file.user == 'root'
    assert beat.binary_file.group == beat.name
    assert beat.binary_file.mode == 0o0750


def test_net_raw_capability(Command, beat):
    if beat.name in ['packetbeat', 'heartbeat']:
        assert 'cap_net_raw' in beat.capabilities
    else:
        assert 'cap_net_raw' not in beat.capabilities


def test_net_admin_capability(Command, beat):
    if beat.name == 'packetbeat':
        assert 'cap_net_admin' in beat.capabilities
    else:
        assert 'cap_net_admin' not in beat.capabilities


def test_config_file_permissions(beat):
    assert beat.config_file.user == 'root'
    assert beat.config_file.group == beat.name
    assert beat.config_file.mode == 0o0640


def test_config_dir_permissions(beat):
    assert beat.config_dir.user == 'root'
    assert beat.config_dir.group == beat.name
    assert beat.config_dir.mode == 0o0750


def test_data_dir_permissions(beat):
    assert beat.data_dir.user == 'root'
    assert beat.data_dir.group == beat.name
    assert beat.data_dir.mode == 0o0770


def test_kibana_dir_permissions(beat):
    assert beat.kibana_dir.user == 'root'
    assert beat.kibana_dir.group == beat.name
    assert beat.kibana_dir.mode == 0o0750


def test_log_dir_permissions(beat):
    assert beat.log_dir.user == 'root'
    assert beat.log_dir.group == beat.name
    assert beat.log_dir.mode == 0o0770
