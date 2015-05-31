# ispcheck
Python module to check if a domain name or email address belongs to an ISP by looking up a list of ISP domain names.

The list of ISP domains is by no means all inclusive. If you'd like to include an ISP that's not in the system, feel free to send me a line or create a pull request.

### How to use
```
In [1]: from ispcheck import check_domain, check_email

In [2]: is_isp_domain('gmail.es')
Out[2]: True

In [3]: is_isp_email('foo@appfluence.com')
Out[3]: False
```
