# Web Infrastructure Design

The goal of this project was to draw diagrams of a web stack.

### Simple Web Stack
Design a web server infrastructure that hosts the website that is reachable via `www.foobar.com`.

[0-simple_web_stack](https://imgur.com/gallery/GCvjYrQ)

Requirements:
  > - 1 server
  > - 1 web server (Nginx)
  > - 1 application server
  > - 1 application files (your code base)
  > - 1 database (MySQL)
  > - 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8


### Distributed Web Infrastructure
Design a three server web infrastructure that hosts the website `www.foobar.com`.

[1-distributed_web_infrastructure](https://imgur.com/gallery/WwT5xz8)

Requirements:
  > - 2 servers
  > - 1 web server (Nginx)
  > - 1 application server
  > - 1 load-balancer (HAproxy)
  > - 1 set of application files (your code base)
  > - 1 database (MySQL)

### Secured and Monitored Web Infrastructure
Design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.

[2-secured_and_monitored_web_infrastructure](https://imgur.com/gallery/fAjF5gZ)

Requirements:
  > - 3 firewalls
  > - 1 SSL certificate to serve `www.foobar.com` over HTTPS
  > - 3 monitoring clients
