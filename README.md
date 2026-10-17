# FloatShot for Windows

Official public downloads for **FloatShot**. Source code is kept private in `zaizaisharpsharp/FloatShot-Windows`.

## Install FloatShot

**Latest version: v0.8.5** (October 16, 2026)

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

The private repository's GitHub Actions workflow builds the self-contained Windows x64 application, creates the installer with Inno Setup 6, runs the installer on a clean Windows runner and verifies the installed executable, update marker, Start menu shortcut and Windows uninstall registration. It also validates the ZIP and manifest. The **v0.8.2** workflow completed successfully. Full interactive GUI behavior still needs desktop validation.

The publishing credential in GitHub Actions is scoped to this public release repository and expires January 14, 2027. It must be renewed for future automated publication.


## What's new in v0.8.1

**All-In-One opens a floating capture-mode toolbar**, not an automatic fullscreen screenshot. Supported modes are Area (select, resize/move, show pixel dimensions, press Enter or Capture), Fullscreen, Window and Timer. Standalone Capture Fullscreen still captures immediately. Scrolling capture, OCR and recording remain disabled until implemented.

Supported functions now show original two-step **first-use help guides** with a Got it button. Once acknowledged, the guide won't interrupt that tool again. Reopen any guide from **Help & Tips** in the tray menu or **Settings → About**.

Current users can install v0.8.1 through FloatShot's **Check for Updates → Download Update → Restart & Install** without downloading the setup EXE. The GitHub Actions workflow compiled v0.8.1, installed the EXE on a Windows runner and verified the ZIP, manifest and public release. Live interface behavior still requires testing on a Windows desktop.


## v0.8.2: Stability and compact tray menu

This release corrects the tray-menu command lifecycle. Choosing an action hides the menu first, allows the mouse event to finish, and safely closes the menu and dispatches the action. Errors no longer silently terminate the app for ordinary recoverable WPF failures; diagnostics are stored at `%LOCALAPPDATA%\\FloatShot\\logs\\diagnostics.log`.

The menu is narrower, shorter, with more compact rows and typography. The Windows release workflow now tests the menu dispatch path plus Settings, About, History, and All-In-One WPF window creation, in addition to installing and verifying the setup EXE.

**If an older FloatShot crashes when you use its menu:** close it from Task Manager if still running and download and run the latest `FloatShot-Setup.exe` **over the existing installation**. No need to uninstall or remove saved screenshots. Future updates remain available in-app.

## What's new in v0.8.4

- **Official FloatShot branding:** the tray, app icon, screenshot capture-area tools and Settings About page use the supplied slim FloatShot symbol.
- **First-launch orientation:** a welcome window explains where to find FloatShot in Windows' notification area. To show it beside Wi-Fi and battery, open the **^** hidden-icons menu and drag the FloatShot icon into the visible notification area; Windows manages which icons stay pinned.
- **Tray menu:** anchored at the bottom-right of the active display, with the shorter **Quit** item and no cloud-upload menu.
- **Larger screenshot previews:** default square thumbnail size is 220px, user-adjustable from 175–270px. The shelf retains readable cards instead of shrinking all six in advance. Oldest unsaved cards are saved when the available slots are full.
- **Capture Fullscreen:** captures the entire monitor under the cursor in physical pixels. For multiple monitors, move the cursor to the desired screen first.
- **Capture Window:** click the intended window in a visual picker. FloatShot attempts whole-window rendering, with an on-screen fallback for apps that block Windows PrintWindow.
- **Modern windows:** Settings, History and first-use tips use normal Windows minimize/close/resize controls; Capture History is a searchable thumbnail gallery. The annotation window has a lighter, compact toolbar.
- **Full-resolution preview:** double-click the floating thumbnail to open the image with the default Windows viewer; use **Edit** to annotate.
- **Lean installer:** self-contained setup EXE is approximately 47 MB (49.2 MB in decimal units), compared with v0.8.3's 65.7 MB.

The private Windows CI workflow successfully built and installed v0.8.4, generated the provided icon, exercised the WPF windows and menu, checked the window/screen capture pixel dimensions, verified the updater ZIP SHA-256 hash, and published this release. Display scaling and visual experience on individual machines should still be tested directly.

### User guidance

To open FloatShot: click the **^** arrow next to the Windows clock, find the FloatShot icon, and right-click to open its menu. To keep it visible, drag it from the popup onto the taskbar notification area. Apps cannot force their own icon into Windows' always-visible notification set.

For future updates: open FloatShot → **Check for Updates** → **Download Update** → **Restart & Install**. You only need the setup EXE for the first installation, a clean reinstall, or to repair a broken existing installation.


## v0.8.5: Fixed right-edge tray menu

FloatShot now opens its notification-area popup at the **far right of the active monitor's taskbar work area**, with a consistent edge gap, regardless of the mouse cursor's position. The menu's last item is **Quit**. Windows CI now verifies actual right-edge placement when the WPF menu is shown, plus its existing menu command, capture, EXE installer and update integrity tests. Already-installed users can update through **Check for Updates**; first-time users can download `FloatShot-Setup.exe`.
