# Experimental Configuration Management for SMART C-CDA Scorecard

Experimental branch providing a Vagrant installer for the C-CDA Scorecard.

The two prerequisites, which are available on Mac, Windows, and Linux are:

1. [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](http://www.vagrantup.com/downloads)

Once you have Virtualbox and Vagrant installed on your machine, you can:

```
vagrant plugin install vagrant-vbguest
git clone https://github.com/jmandel/ansible-ccda/ -b vagrant-scorecard
cd ansible-ccda/vagrant
vagrant up
```

... wait ~20min while everything installs (depending on your Internet connection speed).

Now visit `http://localhost:3000` in a web browser on your local ("host")
maachine and you should have a working, totally local copy of the C-CDA
Scorecard. When you're done you can shut it down with:

```
vagrant halt
```
