# Ansible Role: sshd

[![Build Status](https://travis-ci.org/markahesketh/ansible-role-sshd.svg?branch=master)](https://travis-ci.org/markahesketh/ansible-role-sshd)

Ansible role to manage sshd on Debian/Ubuntu servers.

## Installation

```
ansible-galaxy install markahesketh.sshd
```

## Role Variables

Default values are listed below (see [`defaults/main.yml`](defaults/main.yml)):

```yml
sshd_permit_root_login: no
sshd_password_authentication: no
```

## License

This role is open-sourced software licensed under the [MIT license](http://opensource.org/licenses/MIT).

## Author

By [Mark Hesketh](https://www.markhesketh.co.uk/), a web developer from Manchester, UK.
