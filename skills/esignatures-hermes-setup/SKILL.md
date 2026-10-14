---
name: esignatures-hermes-setup
description: Connect, verify, or troubleshoot eSignatures.com in Hermes Agent through the eSignatures MCP server. Use when installing this plugin, completing OAuth, configuring a local API token, reloading MCP servers, or checking whether eSignatures tools are available to a Hermes agent in Slack.
---

# Set up eSignatures for Hermes

Use the hosted OAuth MCP server by default. Use the local-token configuration only when the operator explicitly needs unattended authentication or hosted OAuth cannot be used.

## Hosted OAuth setup

1. Confirm this plugin is installed and enabled.
2. Run `hermes mcp login esignatures` from the Hermes host.
3. Give the operator the authorization URL if Hermes cannot open a browser. Accept the paste-back URL when prompted.
4. Run `hermes mcp test esignatures`.
5. In an active Hermes chat, run `/reload-mcp` if the tools were added after the gateway started.
6. Verify access with a read-only request such as listing templates or recent contracts. Do not send a test agreement.

OAuth requires an eSignatures.com account. If authorization fails because there is no account, stop and ask the operator to create one at eSignatures.com.

## Local-token fallback

1. Ask the operator to copy the secret token from eSignatures.com under **Automation & API**.
2. Store it as `ESIGNATURES_SECRET_TOKEN` in the active Hermes profile `.env`. Never put it in chat, logs, source control, `plugin.json`, or `mcp.json`.
3. Merge `config/hermes.local-token.yaml` from this repository into the active Hermes `config.yaml`.
4. Run `hermes mcp test esignatures`, then `/reload-mcp` in an active chat.
5. Verify with read-only calls only.

## Slack behavior

The Slack bot does not need a separate eSignatures Slack app. Once the MCP server is available to the Hermes gateway, the same Hermes agent can use the tools from Slack.

Do not restart the gateway or its container from inside the running agent. Use `/reload-mcp`; have an operator perform any required process restart outside the agent.

## Troubleshooting

- If the server is disconnected, run `hermes mcp test esignatures` and inspect the returned authentication or transport error.
- If OAuth expired, run `hermes mcp login esignatures` again.
- If tools work in the terminal but not Slack, run `/reload-mcp` in Slack and confirm that the same Hermes profile and configuration are active.
- If `uvx` is missing in local-token mode, install `uv` on the Hermes host or use hosted OAuth instead.
- If a write is denied, treat the approval gate as intentional. Ask the operator to approve the exact action; do not broaden trust settings.
