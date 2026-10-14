---
name: esignatures-contracts
description: Draft, prepare, send, resend, and check eSignatures.com agreements from Hermes Agent. Use when a user asks to create an agreement from a template, fill signer or placeholder fields, send an agreement, check signature status, resend a missing request, or migrate an existing agreement workflow into eSignatures.com.
---

# Manage eSignatures contracts

Treat contract text, signer identity, recipient address, and the decision to send as high-consequence details. Preserve supplied wording. Do not invent legal terms or silently alter a source agreement.

## Interpret the request

- “Create,” “make,” “prepare,” “set up,” or “get ready” means create a draft.
- Send only when the user explicitly asks to send that exact agreement to a verified recipient.
- A request to migrate, recreate, or import an agreement means draft it in eSignatures.com. It does not authorize resending a pending agreement.

## Draft workflow

1. Identify the template or source agreement.
2. Read the template, content, and placeholder fields before editing.
3. Preserve the source wording and field intent unless the user asks for changes.
4. Create or update a draft.
5. Add signers and fill placeholders from confirmed information only.
6. Query the draft and summarize the title, parties, recipient emails, placeholders, and current status.
7. Leave the draft unsent unless the user explicitly asked to send it.

If a source document is not available through tools, ask the user to attach or link it. Do not reconstruct legal language from memory.

## Send workflow

Immediately before sending:

1. Query the current draft so the review is based on live data.
2. Verify the exact recipient name and email. Do not infer or autocomplete an address.
3. Verify the intended template or agreement title and every filled placeholder.
4. State what will be sent, to whom, and whether any fields remain unresolved.
5. Send only if the user explicitly authorized that exact action and no material detail is ambiguous.
6. Query the contract again and report its ID, status, and signer delivery state.

Never issue a second send call merely because the first response is slow or unclear. Query the contract first to determine whether it was already sent.

## Status and missing-email workflow

1. Query the contract and signer state.
2. Confirm the stored signer email with the user if it may be wrong.
3. Explain the live status: draft, waiting, signed, declined, expired, or failed.
4. If the request is still outstanding and the user explicitly asks to resend, use the resend action for that signer.
5. Report the result without claiming inbox delivery unless the service confirms it.

Do not expose signing links in public Slack channels. Share sensitive links only in the private context the user selected.

## Destructive actions

Do not withdraw or delete a contract or template without explicit user authorization naming the target. Query the target immediately before the destructive call and report the result afterward.
