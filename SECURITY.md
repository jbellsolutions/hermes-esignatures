# Security policy

Do not open a public issue containing an eSignatures token, contract, signer email, signing link, OAuth callback, or other customer data.

If a secret was committed or posted:

1. Revoke or rotate it in eSignatures.com immediately.
2. Remove it from the active Hermes profile and replace it with the rotated value.
3. Treat affected logs and repository history as compromised even after the visible text is removed.

Keep `ESIGNATURES_SECRET_TOKEN` only in the active Hermes profile `.env` or an equivalent secret manager. The repository's examples reference the environment variable and must never contain its value.

For a vulnerability in eSignatures.com or Hermes Agent itself, use the upstream project's security-reporting process.
