# What is the Host Header?

The Host header speceifies the domain the client wants to access.
It's very useful when multiple domains are hosted on the same server(they all have the same IP address).
Those domains are called virtual hosts.

```In either case, although each of these distinct websites will have a different domain name, they all share a common IP address with the server. Websites hosted in this way on a single server are known as "virtual hosts". ```

```When a browser sends the request, the target URL will resolve to the IP address of a particular server. When this server receives the request, it refers to the Host header to determine the intended back-end and forwards the request accordingly. ```

# Host header attack

