## Lab-8
ffuf -w /usr/share/wordlists/wfuzz/general/common.txt -u https://0a4b00eb0407462a8243ddc4003400a0.web-security-academy.net/my-account?id=FUZZ -mc 200
found => adminstrator

## Lab-9
GET /download-transcript/1.txt

## Lab-12
The second step request isn't correctly managed and can be accessed by any user because developers think that if the current user got past the first request then they must be an admin.
Put the normal user cookie and send the second request.

## Lab-13
The server authenticats based on the referer header, becuase the developers think that if someone accessed the admin page before sending a request to /admin-roles they must be an admin. But that header can be modified from the client side and the server trusts it.
Put the normal user cookie and add /admin to the referer header to the request.
