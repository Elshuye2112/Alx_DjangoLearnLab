# LibraryProject

This is a basic Django project created as part of the ALX Django Learning Lab. It includes initial setup and configuration for learning the Django framework.

# Security Overview

- **HTTPS Enforcement:** All HTTP requests are redirected to HTTPS via `SECURE_SSL_REDIRECT`.
- **HSTS:** Configured to tell browsers to only access the site over HTTPS for 1 year (`SECURE_HSTS_SECONDS`), including all subdomains and preloading enabled.
- **Secure Cookies:** `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` ensure cookies are sent over HTTPS only.
- **Clickjacking Protection:** `X_FRAME_OPTIONS = 'DENY'` prevents framing.
- **Content Type Sniffing:** `SECURE_CONTENT_TYPE_NOSNIFF` prevents MIME type sniffing.
- **XSS Filter:** `SECURE_BROWSER_XSS_FILTER` enables the browser's XSS filter.
- **Deployment:** Web server configured for SSL/TLS with valid certificates and redirects HTTP to HTTPS.

**Next Steps / Improvements:**
- Regularly update SSL certificates.
- Monitor security headers using tools like [Mozilla Observatory](https://observatory.mozilla.org/).
- Implement Content Security Policy (CSP) for additional XSS protection.
