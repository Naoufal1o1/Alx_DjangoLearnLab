# Django HTTPS & Security Enhancements

## Configurations in settings.py
| Setting                         | Description                                                       |
|----------------------------------|-------------------------------------------------------------------|
| SECURE_SSL_REDIRECT              | Redirects HTTP to HTTPS                                           |
| SECURE_HSTS_SECONDS              | Tells browsers to use HTTPS only for 1 year                       |
| SECURE_HSTS_INCLUDE_SUBDOMAINS  | Includes all subdomains in HSTS                                  |
| SECURE_HSTS_PRELOAD              | Eligible for browser HSTS preload lists                          |
| SESSION_COOKIE_SECURE            | Session cookies transmitted over HTTPS only                      |
| CSRF_COOKIE_SECURE               | CSRF tokens transmitted over HTTPS only                          |
| X_FRAME_OPTIONS = 'DENY'         | Prevents clickjacking via iframes                                |
| SECURE_CONTENT_TYPE_NOSNIFF      | Prevents MIME-type sniffing attacks                              |
| SECURE_BROWSER_XSS_FILTER        | Enables browser XSS filter                                       |

## Deployment (Nginx)
- Enforced HTTPS with Let's Encrypt SSL certificate
- HTTP traffic automatically redirected to HTTPS

## Security Review Summary
✅ HTTPS enforced via redirect and HSTS  
✅ All cookies marked secure  
✅ Strong headers against clickjacking, XSS, and MIME sniffing  
✅ SSL certificates configured on Nginx  
✅ No sensitive data transmitted over HTTP

## Future Recommendations
- Add CSP headers via `django-csp`
- Use `SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"`
- Set `SECURE_PROXY_SSL_HEADER` if behind a reverse proxy (like Nginx)

