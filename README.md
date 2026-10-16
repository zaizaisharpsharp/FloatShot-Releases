# FloatShot Releases

Official **public binary releases** for FloatShot, the Windows screenshot app. Source code remains in the private `zaizaisharpsharp/FloatShot-Windows` repository.

## Latest available

**v0.7.6** — published October 16, 2026.

[Download the latest Windows ZIP](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/latest)

## Updating FloatShot

For an already installed FloatShot with the new release channel configured:

1. Right-click the FloatShot icon in the Windows system tray.
2. Open **Updates → Check for Updates...**
3. The app shows the installed version and latest version.
4. Click **Download Update** when a newer version is available. FloatShot downloads it and verifies the SHA-256 checksum without closing.\n5. Click **Install & Restart** and confirm the prompt. FloatShot closes, installs the verified update and reopens. Floating screenshots and editors must be closed before installation.

The app checks `https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/latest/download/floatshot-update.json` automatically; there is no GitHub repository setting in its UI.

Releases include `FloatShot-win-x64.zip` and `floatshot-update.json`. The ZIP is not itself a one-click installer. New installations should use the project's one-time Windows installer, which sets the installed-app marker, startup shortcut, and update target.

## Release security

The private source repository's Windows GitHub Actions workflow compiles the app, verifies the executable version, checks the archive, creates a SHA-256 manifest, then publishes. The release token is stored in GitHub Actions secrets and scoped to this public repository.

The token currently expires **January 14, 2027**, and must be renewed to keep future publishing automated. Existing published downloads will remain available.

**Validation:** Versions v0.7.3 through v0.7.6 passed Windows compilation, packaging and integrity checks. The new opt-in install flow and bottom-up screenshot shelf are in v0.7.6; actual Windows UI and restart behavior require a live client test.
