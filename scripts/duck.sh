#!/bin/sh
echo url="https://www.duckdns.org/update?domains=DOMAIN&token=TOKEN_DE_DUCKDNS&ip=" | curl -k -o /app/log/duck.log -K -
