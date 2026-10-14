# eSignatures for Hermes Agent

A portable Hermes Agent plugin that connects Hermes—including a Hermes bot in Slack—to eSignatures.com through the official hosted MCP endpoint.

It packages two guarded skills:

- `esignatures-hermes-setup`: authentication, verification, and troubleshooting
- `esignatures-contracts`: draft, send, resend, status, and migration workflows

The default connection uses OAuth. No API key, agreement, email address, signer information, or customer data belongs in this repository.

## What you need

- A Hermes Agent release with Portable Agent Plugin support
- An eSignatures.com account
- Shell access to the host that runs Hermes for initial installation and authentication

## Install

```bash
hermes plugins install jbellsolutions/hermes-esignatures --no-enable
hermes plugins enable esignatures
hermes mcp login esignatures
hermes mcp test esignatures
```

If Hermes is on a remote or headless machine, open the authorization URL on your own computer and paste the final callback URL back into the terminal when prompted.

In an already-running Hermes conversation, use:

```text
/reload-mcp
```

Verify the connection with a read-only request:

```text
List my eSignatures templates and five most recent contracts. Do not create, change, or send anything.
```

Do not use a real send as a connection test.

## Use it from Slack

No separate eSignatures Slack application is required. The Slack bot uses the same tools exposed to its Hermes gateway.

Examples:

```text
Create a draft agreement from the Standard Client Agreement template for Acme. Do not send it.
```

```text
Show me the current signer status for the Acme agreement.
```

```text
Send the reviewed Acme agreement to Pat at pat@example.com.
```

The included contract skill treats “create,” “make,” and “prepare” as draft-only. Sending requires an explicit instruction with a verified recipient.

## Manual configuration

If your Hermes installation does not use portable plugins, merge [`config/hermes.oauth.yaml`](config/hermes.oauth.yaml) into the active Hermes `config.yaml`, then run the same login and test commands.

For an always-on or unattended deployment, [`config/hermes.local-token.yaml`](config/hermes.local-token.yaml) runs the official `mcp-server-esignatures` package through `uvx`. Store the token as `ESIGNATURES_SECRET_TOKEN` in the active Hermes profile `.env`—never in YAML or source control.

Both manual configurations use a narrow tool allowlist and mark the server `untrusted`, so write-capable tool calls remain approval-gated. They intentionally omit deletion, withdrawal, public contract-link, collaborator, and user-management tools.

## Migrating from SignWell

Use the source agreement as the legal source of truth. Recreate its exact wording and signing-field intent as an eSignatures template or draft, review it, and send only after explicit authorization. A migration request does not authorize resending agreements that are already pending elsewhere.

This repository deliberately contains no agreements or account exports.

## Safety model

- Draft by default; send only on an explicit instruction.
- Re-read a draft immediately before sending.
- Verify the recipient address rather than inferring or autocompleting it.
- Query after a send before retrying, which reduces accidental duplicates.
- Never expose signing links in public Slack channels.
- Never withdraw or delete without explicit authorization naming the target.
- Reload MCP configuration with `/reload-mcp`; do not have the running agent restart its own gateway or container.

## Validate changes

```bash
python3 scripts/check.py
```

## Upstream documentation

- [eSignatures MCP documentation](https://esignatures.com/docs/mcp)
- [Official eSignatures MCP server](https://github.com/esignaturescom/mcp-server-esignatures)
- [Hermes Portable Agent Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/plugins)
- [Hermes MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)

## Status and support

This is an independent integration package, not an official eSignatures.com or Nous Research product. eSignatures.com, Hermes Agent, and their marks belong to their respective owners.

See [`SECURITY.md`](SECURITY.md) before reporting a suspected credential leak.
