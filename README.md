# Configuration Management for SMART C-CDA Tools

Use these scripts to get a **fresh Ubuntu 12.10 machine** up and running with:
 * Direct Java Reference Implementation [version 2.1](http://wiki.directproject.org/message/view/Java+Reference+Implementation/60702540)
 * SMART's C-CDA [reDirect](https://github.com/jmandel/ccda-reDirect) (push e-mail attachments into the Receiver)

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

##### `settings/direct_server.yml`
Set up your Direct server.  You'll want to edit the default template to use
your VM's fully qualified domain name, then enter your organization's detail in
the "certificate" field.  This is also your opportunity to pre-configure
any end-user Direct email accounts you need (supplying a username and a
password for each)

You'll want to pay special attention to two settings that make SMART C-CDA reDirect work:

* `CCDA_POST_URL` tells SMART C-CDA reDirect where C-CDA attachments should be sent.
It can be a simple URL like `http://my-server/incoming/ccda` or it 
can be a URL template with access to two variables:
`to` (email recipient address) and `from` (email sender address).
For example, you could use 
`http://my-server/incoming/ccda/for-direct-address/{to}` if your server
expets to partition C-CDA documents by Direct address.

* `catchall: true` allows your Direct server to work in "catchall" mode,
where Direct e-mail to `*@yourdomain` will be handled automatically  If catchall mode is disabled,
your Direct server will only be able to receive messages to pre-configured users.

For a complete example, see [settings/direct_server.yml](settings/direct_server.yml).

---

##### `hosts`
Default installs on the local machine.
If you want to install the stack on a remote host, edit `hosts` as needed. (See below.)

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

