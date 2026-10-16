# FloatShot for Windows

Official public downloads for **FloatShot**. Source code is kept private in `zaizaisharpsharp/FloatShot-Windows`.

## Install FloatShot

**Latest version: v0.8.0** (October 16, 2026)

**[Download FloatShot-Setup.exe](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/latest/download/FloatShot-Setup.exe)**

Download the single setup EXE and double-click it. The modern Windows installer:

- installs the self-contained app for the current Windows account without administrator rights;
- adds a Start menu shortcut and Windows **Settings → Installed apps → FloatShot** uninstall entry;
- offers a desktop shortcut and start-at-login option;
- launches FloatShot after setup.

No source ZIP, .NET SDK or build script is needed. Settings and screenshots survive upgrades or uninstalling. This setup is currently **unsigned**, so Windows SmartScreen may warn that it has an unknown publisher. Verify that you downloaded it from this official release repository.

## Update an existing installation

If FloatShot is already installed, you do **not** need to run the installer again.

Right-click FloatShot in the Windows notification area, choose **Check for Updates**, then **Download Update** and **Restart & Install** when ready. FloatShot checks the public release manifest and verifies the package SHA-256 digest before installing.

Each release includes:

- `FloatShot-Setup.exe`: standalone Windows setup for new installs and reinstalls.
- `FloatShot-win-x64.zip`: internal app files consumed by the in-app updater.
- `floatshot-update.json`: versioned update manifest containing the ZIP URL and SHA-256 checksum.

The updater reads `https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/latest/download/floatshot-update.json`.

## Build verification

The private repository's GitHub Actions workflow builds the self-contained Windows x64 application, creates the installer with Inno Setup 6, runs the installer on a clean Windows runner and verifies the installed executable, update marker, Start menu shortcut and Windows uninstall registration. It also validates the ZIP and manifest. The **v0.8.0** workflow completed successfully. Full interactive GUI behavior still needs desktop validation.

The publishing credential in GitHub Actions is scoped to this public release repository and expires January 14, 2027. It must be renewed for future automated publication.
