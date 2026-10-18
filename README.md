# FloatShot for Windows

**A lightweight Windows screenshot, annotation and screen-recording utility.** FloatShot keeps captures and recordings on your computer, with pixel-accurate PNG screenshots, a floating Quick Access shelf and a built-in updater.

Supports **Windows 10 (build 19041+) and Windows 11, x64**. Install using the standalone `FloatShot-Setup.exe`: no .NET SDK or ZIP extraction is needed.

<!-- FLOATSHOT:RELEASE-START -->
## Latest stable release: v0.14.2

[**Download FloatShot for Windows (.exe)**](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/download/v0.14.2/FloatShot-Setup.exe) · [Portable ZIP](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/download/v0.14.2/FloatShot-win-x64.zip) · [Release details](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/tag/v0.14.2) · [All releases](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases)

### What's new in v0.14.2

Clearer dark-taskbar icon, sleeker tray gestures and more natural annotation editing.

- Made the existing FloatShot symbol visible on dark Windows taskbars using the approved light mark. The original logo, installer icon and Start/Search branding remain unchanged.
- Replaced the oversized tray gesture controls with two compact, synchronized dropdowns for left-click and right-click actions. Selections take effect immediately and are saved.
- Numbered Step now stays active after each click, placing 1, 2, 3 and onward without returning to the toolbar.
- Drawing tools display distinct cursors for their shapes. Selected annotations show a small on-canvas Delete X; Undo restores deleted objects.
- Expanded Windows interaction and visual regression tests while preserving native-pixel PNG quality, recording, recovery, updates and installed user data.

### Recent releases

- [v0.14.2](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/tag/v0.14.2) (latest)
- [v0.14.1](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/tag/v0.14.1)
- [v0.14.0](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/tag/v0.14.0)
- [v0.13.0](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/tag/v0.13.0)
- [v0.12.11](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/tag/v0.12.11)

<!-- FLOATSHOT:RELEASE-END -->

## Get started

1. Install the latest [Windows installer](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/latest/download/FloatShot-Setup.exe), then open FloatShot from the Start menu.
2. Find the FloatShot icon in the Windows notification area, possibly under the **^** hidden-icons arrow.
3. **Default mouse gestures:** Left-click the FloatShot tray icon to select an area; right-click to open or dismiss the compact menu. Clicking outside the menu or pressing Esc also closes it.
4. To swap the gestures, open **Settings → General → Tray gestures** and select your preferred mapping. The change takes effect immediately and persists after restarting FloatShot.
5. Use **Ctrl+Shift+2** to capture an area, **Ctrl+Shift+3** for the monitor, or **Ctrl+Shift+4** for a window/accessible region.

## Features

- **Lossless image capture:** Full-resolution screenshots saved as PNG without losing captured pixels. JPEG is optional and lossy; zooming a preview cannot create missing detail.
- **Floating Quick Access:** Compact screenshot and video cards with Copy, Save and Pin actions; original-file drag-and-drop; saved capture History.
- **Screenshot editor:** Movable and editable text, lines, arrows, shapes, highlighting, pen marks and solid black redaction. Undo/Redo and full-resolution PNG exports are supported.
- **Screen recording:** Select and adjust a recording region; start after a countdown, then Pause, Resume or Stop. Preview MP4 recordings in the built-in player; recover unfinished drafts where possible.
- **More capture tools:** Window selection, local English OCR, and scrolling screenshots (some capture modes remain BETA).
- **Windows appearance:** Light, Dark and System modes.
- **Desktop icons:** The compact tray menu's **Hide/Show Desktop Icons** command controls Windows desktop shortcuts without hiding FloatShot's tray icon or deleting files.

**Recording audio, GIF export and video trimming are not yet included.** HDR displays, protected content, unusual display scaling and some applications may have Windows-specific capture limitations.

## Updating FloatShot

Open the tray menu → **Check for Updates**. When a newer release is available, download it, allow ZIP checksum verification, and choose **Restart & Install**. The updater safeguards existing data and uses a backup during replacement.

You can also install the latest setup EXE over a previous installation. Your exported screenshots, recordings and preferences are stored separately from the app. For a portable copy use the ZIP; it is not the same as the installer.

**Important:** The Windows installer is currently unsigned. Windows SmartScreen may identify it as an unknown publisher. Download only from this official [releases page](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases).

## Release history and verification

- [All releases, release notes and verified installers](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases)
- [Archive of older README release notes](docs/README_ARCHIVE_THROUGH_V0.13.0.md)
- [Source repository and Windows CI history](https://github.com/zaizaisharpsharp/FloatShot-Windows) (source access may be restricted)

GitHub's Windows release workflow builds and tests the application, installer, updater, rollback and archive integrity. Automated checks cannot cover every real monitor, driver, clipboard destination or input device.

## Troubleshooting

If the app icon is in Windows' hidden notification area, drag it beside the clock to make it easier to find. Windows controls the taskbar overflow placement.

For icon-cache problems after updating, unpin any outdated FloatShot taskbar shortcut and pin it again from the Windows Start menu.

Diagnostic logs are stored under `%LOCALAPPDATA%\FloatShot\logs\`. If the app cannot update, use the installer linked above rather than an unverified third-party download.

---

*The latest-release block above is automatically generated from the newest published GitHub Release. It updates when a release is published or edited; use [All releases](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases) for the complete changelog.*
