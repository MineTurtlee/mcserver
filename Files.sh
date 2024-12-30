ERRORS_LOG=$(grep "command failed" ${LOG_FILE})

if [[ -e "${LOG_FILE}" && -z "${ERRORS_LOG}" ]]; then
    SSH_CMD="$(grep -oE "tcp://(.+)" ${LOG_FILE} | sed "s/tcp:\/\//ssh ${USER}@/" | sed "s/:/ -p /")"
    MSG="
*GitHub Actions - ngrok session info:*

⚡ *CLI:*
\`${SSH_CMD}\`
**tips:** This is the server and port
"
