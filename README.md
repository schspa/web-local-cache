# cicd-log-browser

Browser log for cicd

# Usage

## Prepare a directory contains a config file:

    <local-url-cache>/config.toml

```toml
# Configuration
LOCAL_PATH = "/var/lib/www"
REMOTE_HOST = "https://www.xxx.com"
```

## Launch with docker-compose

```bash
CONFIG_PATH=<local-url-cache> FILE_PATH=/var/lib/www docker-compose up
```

# Test

```bash
curl http://localhost:5000/xxx
```

