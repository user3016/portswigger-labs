# What is the Host Header?

The Host header speceifies the domain the client wants to access.
It's very useful when multiple domains are hosted on the same server(they all have the same IP address).
Those domains are called virtual hosts.

```In either case, although each of these distinct websites will have a different domain name, they all share a common IP address with the server. Websites hosted in this way on a single server are known as "virtual hosts". ```

```When a browser sends the request, the target URL will resolve to the IP address of a particular server. When this server receives the request, it refers to the Host header to determine the intended back-end and forwards the request accordingly. ```

# Host header attack
HTTP Host header vulnerabilities typically arise due to the flawed assumption that the header is not user controllable. This creates implicit trust in the Host header and results in inadequate validation or escaping of its value, even though an attacker can easily modify this using tools like Burp Proxy. 

Even if the Host header itself is handled more securely, depending on the configuration of the servers that deal with incoming requests, the Host can potentially be overridden by injecting other headers. Sometimes website owners are unaware that these headers are supported by default and, as a result, they may not be treated with the same level of scrutiny.

In fact, many of these vulnerabilities arise not because of insecure coding but because of insecure configuration of one or more components in the related infrastructure. These configuration issues can occur because websites integrate third-party technologies into their architecture without necessarily understanding the configuration options and their security implications. 

```<a href="https://_SERVER['HOST']/support">Contact support</a>```

## Identification
### 1. Supply an arbitrary Host header
Servers are sometimes configured with a default or fallback option in case they receive requests for domain names that they don't recognize. If your target website happens to be the default, you're in luck. In this case, you can begin studying what the application does with the Host header and whether this behavior is exploitable. 

### 2.Check for flawed validation
### 3. Inject duplicate Host headers
### 4.Supply an absolute URL 
```
GET https://vulnerable-website.com/ HTTP/1.1
Host: bad-stuff-here
```

### 5.Add line wrapping
```
GET /example HTTP/1.1
    Host: bad-stuff-here
Host: vulnerable-website.com
```

## Exploitation

### 1.Password reset poisoning
If the password reset link is dynamically generated based on the host header, we can construct the attack as follows:

1- The attacker obtains the victim's email address or username, as required, and submits a password reset request on their behalf. When submitting the form, they intercept the resulting HTTP request and modify the Host header so that it points to a domain that they control. For this example, we'll use hacker.com.

2-The victim receives a genuine password reset email directly from the website. This seems to contain an ordinary link to reset their password and, crucially, contains a valid password reset token that is associated with their account. However, the domain name in the URL points to the attacker's server: ```https://hacker.com/reset?token=0a1b2c3d4e5f6g7h8i9j```
    
3-If the victim clicks this link (or it is fetched in some other way, for example, by an antivirus scanner) the password reset token will be delivered to the attacker's server and can be accessed via reading the server's logs.

4-The attacker can now visit the real URL for the vulnerable website and supply the victim's stolen token via the corresponding parameter. They will then be able to reset the user's password to whatever they like and subsequently log in to their account.


