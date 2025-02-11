Black Box testing: just the URL and scope.
White Box testing: access to the source code.
Grey Box testing: mix of black and White.



## HTTP Request
1. When you enter http://website1.com/file.html in your browser, your system performs a DNS lookup for website1.com.
The DNS server responds with the IP address of website1.com (e.g., 192.168.1.10).

2. Your browser then establishes a TCP connection to 192.168.1.10.
This happens before any HTTP request is sent.
HTTP Request is Sent Over the Established Connection

3. Once the TCP handshake is complete, your browser sends an HTTP request over this connection.
The Host header inside the HTTP request tells the web server which domain the request is for.
In your case, you intercept the request and modify:
Host: website2.com
However, the actual TCP connection is still with website1.com’s server (192.168.1.10).

## What Happens on the Server?

If website1.com and website2.com share the same server:
The web server (e.g., Apache, Nginx) checks the Host header and may serve content for website2.com (if configured).
If website1.com and website2.com are on different servers:
The request still goes to website1.com's server (192.168.1.10).
The server at 192.168.1.10 has no knowledge of website2.com.
It may reject the request (400 Bad Request), return an error page, or serve a default site.
