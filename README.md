# Auto-Configuration for Direct Server + SMART C-CDA Receiver

Use these scripts to get a fresh Ubuntu 12.10 machine up and running with:
 * Direct Java Reference Implementation version 2.1
 * SMART Consolidated CDA Receiver
 * SMART reDirect (push e-mail attachments into the Receiver)

##  VM-only ("ansible local")  mode

Everything runs on your VM, including the ansible installer scripts. (Note that
ansible also supports an ssh-based remote configuraiton mode, where all the
installer scripts run elsewhere and are pushed the the VM when you specify 
remote hosts and run `ansible-playbook`.)

We'll focus on local mode, since it's simpler (and only requires a single machine).


##### 1. Provision a fresh Ubuntu 12.10 VM in the cloud.
##### 2.  Install dependencies, ansible, and this playbook.

```
# Install package dependencies
apt-get -y install git \
                   make \
                   python-yaml \
                   python-jinja2 \
                   python-paramiko \
                   software-properties-common

# Install Ansible
git clone git://github.com/ansible/ansible.git
cd ansible
make install

# Grab this playbook (the one whose README you're reading now)
git clone https://github.com/jmandel/ansible-ccda 
cd ansible-ccda
```
##### 3.  Edit the configuration parameters (see below)
##### 4.  Run the playbook
```
ansible-playbook -c local -i hosts -v playbook.yml
```

* `-c local`         use a local connection
* `-i hosts`         uses hosts defined in the `hosts` file
* `-v`               verbose mode for better error reporting
* `playbook.yml`     the top-level install script

### Config files
There are two main files you'll need to edit to get going:

#####  `settings/ccda_receiver.yml`

Set up the URLs for your C-CDA Receiver.  You'll want to substitute your
hostname for teh default ("direct-ansible.smartplatforms.org").

For a complete example, see [settings/ccda_receiver.yml](settings/ccda_receiver.yml)

#####  `settings/direct_server.yml`

Set up your Direct server.  You'll want to edit the default template to use
your VM's fully qualified domain name, then enter your organization's detail in
the "certificate" field.  Finally, this is your opportunity to pre-configure
any end-user Direct email accounts you need (supplying a username and a
password for each)

For a complete example, see [settings/direct_server.yml](settings/direct_server.yml)

##  Remote mote
TODO


## Configuring external DNS

This playbook will get you up and running with a machine running its own DNS
server.  (You'll need this for Direct, because X509 Certificates are exposed
via DNS.)  Outside of the VM, you'll need to make sure that your DNS configuration
allows this machine to be its own DNS authority. A simple way to do this, 
given the exampe domain of "direct-ansible.smartplatforms.org":

In your domain's DNS, add two entries:

 * ns.direct-ansible.smartplatforms.org (record type: `A`, value: `your IP`)
 * direct-ansible.smartplatforms.org (record type `NS`, value: `ns.direct-ansible.smartplatforms.org`)

With those two entries, you should be up and running!

