# Configuration Management for SMART C-CDA Tools

Use these scripts to get a **fresh Ubuntu 12.10 machine** up and running with:
 * Direct Java Reference Implementation [version 2.1](http://wiki.directproject.org/message/view/Java+Reference+Implementation/60702540)
 * SMART [Consolidated CDA Receiver](https://github.com/chb/ccdaReceiver) (Expose a RESTful API on C-CDA data)
 * SMART [C-CDA Scorecard](https://github.com/chb/ccdaScorecard) (Rate C-CDAs for adherence to best practices)
 * SMART [reDirect](https://github.com/jmandel/ccda-receiver-direct-connector) (push e-mail attachments into the Receiver)

##  VM-only ("ansible local")  mode

Everything runs on your VM, including the ansible installer scripts. (Note that
ansible also supports an ssh-based remote configuraiton mode, where all the
installer scripts run elsewhere and are pushed the the VM when you specify 
remote hosts and run `ansible-playbook`.)

We'll focus on local mode, since it's simpler (and only requires a single machine).


##### 1. Provision a fresh Ubuntu 12.10 VM in the cloud
##### 2.  Install dependencies, ansible, and this playbook

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
##### 3.  Configuration your environment (see below)
##### 4.  Run this playbook
```
ansible-playbook -c local -i hosts -v playbook.yml
```

* `-c local`         use a local connection
* `-i hosts`         uses hosts defined in the `hosts` file
* `-v`               verbose mode for better error reporting
* `playbook.yml`     the top-level [install script](playbook.yml)

### Config files
There are three short files you'll need to edit:

---


##### `settings/ccda_receiver.yml`
Set up the URLs for your C-CDA Receiver.  You'll simply substitute your
hostname for the default.

For a complete example, see [settings/ccda_receiver.yml](settings/ccda_receiver.yml).

---

##### `settings/direct_server.yml`
Set up your Direct server.  You'll want to edit the default template to use
your VM's fully qualified domain name, then enter your organization's detail in
the "certificate" field.  Finally, this is your opportunity to pre-configure
any end-user Direct email accounts you need (supplying a username and a
password for each)

For a complete example, see [settings/direct_server.yml](settings/direct_server.yml).

---

##### `hosts`
If you want to install all three components (Direct, C-CDA Receiver, and C-CDA Scorecard), you're all set.

If you'd rather leave some components out, just delete the relevant blocks.

For a complete example, see [hosts](hosts).

---

##  Remote mode
To install against a remote host, you'll:
 * install ansible on your local "control" machine
 * modify the `hosts` file to point to a remote machine
 * Run `ansible-playbook  -i hosts -v playbook.yml`


## Configuring external DNS

This playbook will get you up and running with a machine running its own DNS
server.  (You'll need this for Direct, because X509 Certificates are exposed
via DNS.)  Outside of the VM, you'll need to make sure that your DNS configuration
allows this machine to be its own DNS authority. A simple way to do this, 
given the exampe domain `direct-ansible.smartplatforms.org`:

In your domain's DNS, add two entries:

* `ns.direct-ansible.smartplatforms.org` (record type: `A`, value: `your IP`)
* `direct-ansible.smartplatforms.org` (record type `NS`, value: `ns.direct-ansible.smartplatforms.org`)

With those two entries, you should be up and running!

