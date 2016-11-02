# Simple Echo Server

This is the 1st assignment for CS4032 (Distributed Systems). The goal was to develop  a socket-based client to ping a PHP server using a simple HTTP request.

My information:

|Name             |Student ID|Status|
|-----------------|:--------:|:--------:|
|Benoit Chabod    |16336617  |Erasmus  |

## Usage

On SCSS OpenNebula, I've tested this system using two nodes :

 * A Debian node called master hosts the PHP server
 * A boot2docker node created from master with docker-machine runs the client script


### Running server

Just clone the repository anywhere, and run this in the same directory as echo.php:

```bash
php -S 0.0.0.0:3000 -t .
```

### Running client

Just clone the repository anywhere, and run this in the same directory as client.py (the IP address entered here needs to be the server one):

```bash
python client.py 10.62.0.36 3000
```

Obviously, python is a prerequisite to use this application. If you don't have it, it can be installed easily on a boot2docker node using:

```bash
tce-load -w -i python.tcz
```

Note: I've chosen to use the port 3000, but feel free to use another one.
