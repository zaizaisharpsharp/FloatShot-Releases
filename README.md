# FloatShot for Windows

A clean, lightweight screenshot utility for Windows 10 and 11 with a floating screenshot shelf, annotation tools and an in-app updater.

**Latest stable release: v0.8.9**

[**Download FloatShot-Setup.exe**](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/download/v0.8.9/FloatShot-Setup.exe) · [All releases](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases)

Download the single Windows EXE and double-click to install. No ZIP extraction or .NET SDK is needed. FloatShot creates a Start menu shortcut and an entry in Windows **Settings → Installed apps**. Existing users can continue updating directly in the app.

## What's new in v0.8.9

- **Faster Capture History:** gallery previews decode lightweight thumbnails rather than 150 full-resolution screenshots at once. **Ctrl+F** focuses filename search.
- **Pin from History:** each saved screenshot has a Pin action. Pinned windows now display the complete original image instead of a square crop, and unpinning respects the floating shelf's size limits.
- **Correct multi-monitor capture:** Fullscreen captures the complete monitor under your pointer rather than an unnecessarily stitched virtual desktop. Turning off **Use the monitor where my cursor is** in Quick Access places cards on the primary monitor.
- **Reliable JPEG rename:** JPEG captures retain their JPEG extension rather than incorrectly becoming .png files.
- **Capture recovery:** transient clipboard contention is logged without preventing the capture from opening in the editor or being saved.
- **More regression coverage:** the Windows test checks thumbnail sizes (160–420px), stack gaps, middle-card reflow, thumbnail decoding, JPEG rename, pinned-window placement and original-image use.
- **Tidier History layout and documentation:** a compact three-column gallery on standard-sized Windows screens, and instructions that match the current tray gestures.

## What's new in v0.8.8

- **Left-click FloatShot's tray icon:** Starts Capture Area immediately without opening the menu. If a menu is already open, it closes that menu.
- **Right-click FloatShot's tray icon:** Opens the compact menu. Right-click it again to close the menu.
- **One-click menu dismissal:** Clicking anywhere outside the open menu, using either mouse button, closes it on the first click without consuming the click intended for the other application. Escape and right-click inside the menu also close it.
- **Hide FloatShot's tray icon:** The menu now says **Hide FloatShot Tray Icon**, replacing the confusing **Hide Desktop Icons** entry. This hides only FloatShot's notification icon and leaves the screenshot shortcuts working. **Open FloatShot from Windows Start** to restore the icon without launching a second copy. Windows still controls whether a visible icon lives beside Wi-Fi/battery or inside the ^ hidden-icons popup.
- **Fixed tray settings:** Settings → General shows the actual left/right gestures, not a menu-click setting that could conflict with them. Windows desktop shortcut visibility remains a separate option in Settings → Wallpaper.
- **Stable screenshot shelf:** The configured 160–420px square-card size and 0–32px gap now affect the real shelf instead of being ignored by a hardcoded six-slot cap. Closing one card leaves siblings open. Older captures are saved and retired only when there is no space.

## What's new in v0.8.6

- **Double-click a screenshot card:** If it was temporary, FloatShot saves it to your configured export folder and opens the original image in your default Windows photo viewer. This does **not** launch the annotation editor. The pencil/Edit action still opens FloatShot's annotation and redaction tools.
- **Clean floating cards:** Removed the heavy dark backing shadow in favor of a thin border and subtle depth. The image stays sharp; the drag preview has a softer, lighter shadow.
- **Larger thumbnail size:** **Settings → Quick Access → Thumbnail size** now supports **160–420px**, with **170px as the default**. The card stays square at all sizes and does not shrink merely to reserve empty stack slots.
- **Adjustable stack spacing:** The new **Stack spacing** slider supports **0–32px**, default **2px**. Older captures remain at the bottom; new screenshots stack above them without positional animation.
- **Independent close behavior:** Clicking the **X** on one floating screenshot dismisses **only that card**. Other cards remain in the stack and shift to fill its slot.
- **Lifetime controls:** Floating captures **never automatically expire by default**. Optional 30-second, 1-minute, 5-minute and custom-duration timers are available under Quick Access; each timer applies independently. Older preferences are migrated once to the safer Never default.
- **Consistent FloatShot branding:** Settings, About, History, editor, welcome, first-use guides and the Updates window explicitly load the new FloatShot Windows icon, rather than relying on Windows' cached executable icon.
- **Automatic-save path correction:** If saving every capture is enabled, FloatShot now keeps the correct persisted file path for viewing, editing and dragging.

The earlier fixes remain: the bottom-right menu, clean annotation window, full-monitor screenshots, selected-window capture, searchable history, user onboarding and **All-In-One** selection toolbar.

## Using FloatShot

After installing, locate FloatShot near the **^** hidden-icons arrow beside your Windows clock. You can enable its visibility in **Windows Settings → Personalization → Taskbar → Other system tray icons**, if available on your Windows version. Windows controls which notification icons remain visible; FloatShot cannot force itself into the Wi-Fi/battery group.

Left-click the FloatShot notification icon to enter Capture Area immediately. Right-click it to open or close the menu. Click outside the menu once, or press Escape, to dismiss it. Use **Ctrl+Shift+2** to select a screenshot area; the default fullscreen and window shortcuts are **Ctrl+Shift+3** and **Ctrl+Shift+4**.

For floating captures:

1. **Copy** puts the screenshot on the clipboard.
2. **Save** exports it to your chosen folder.
3. **Double-click** opens it in the default Windows image viewer, saving it first if necessary.
4. **Pencil/Edit** opens the FloatShot annotation tool.
5. **X** dismisses just that thumbnail. By default, all others remain until manually dismissed.
6. **Drag & drop** sends the screenshot to another application without saving it to your permanent screenshot folder unless you explicitly save.

When the shelf is full for the current screen and thumbnail size, the oldest card is automatically saved and retired to make room. You can use **Settings → Quick Access** to choose a smaller size or tighter spacing.

**Capture History** shows your saved screenshots with lighter previews, Open, Copy, Edit, Pin and Delete. Press **Ctrl+F** to search filenames. **Settings → About → View FloatShot release information** opens this page for feature descriptions, build verification and help.

## How updates work

Open FloatShot → **Check for Updates**. If a new version is available, choose **Download Update**, wait for checksum verification, then **Restart & Install**. The app doesn't close just because the download finishes.

For a clean reinstall or when the in-app updater is inaccessible, use **FloatShot-Setup.exe** above. The setup installs over existing versions while preserving your preferences and exported screenshots.

## Build verification

The v0.8.9 public release passed the full Windows pipeline:

- Self-contained .NET 8 x64 WPF compilation and creation of the branded Windows icons.
- Real Windows window creation and tray-menu dispatch checks, including **left-click Capture Area**, **right-click menu toggle**, **outside-click dismissal**, **hidden tray icon restoration**, Settings, About, Capture History, window selection and monitor/window capture dimension tests.
- **Screenshot regressions:** three floating cards were created, independent middle-card dismissal and shelf reflow were verified, adjustable size/gap settings were exercised, and pinned full-image rendering was checked.
- Inno Setup EXE compilation, silent Windows installation, executable/marker/Start-menu verification and Windows uninstall registration checks.
- Version validation, ZIP integrity, and SHA-256 update-manifest checks.

[**View the successful v0.8.9 Windows build**](https://github.com/zaizaisharpsharp/FloatShot-Windows/actions/runs/39001510754) (private source repository; requires authorized access).

Automated tests don't replace visual testing on every monitor or third-party app. Capture behavior with protected or hardware-accelerated windows can vary due to Windows limitations.

## Troubleshooting

If a command fails, diagnostics are stored at
`%LOCALAPPDATA%\FloatShot\logs\diagnostics.log`.

If you selected **Hide FloatShot Tray Icon**, reopen FloatShot from Windows Start to restore it. This does not forcibly pin the icon beside the battery; the Windows taskbar controls overflow placement.

If Windows still shows an old taskbar icon after the new version is installed, unpin the old shortcut and pin FloatShot again from the Start menu. Windows may cache pinned shortcut icons.

FloatShot does not currently support cloud upload, scrolling capture, OCR or screen recording. Those items are unavailable until the relevant features are implemented.

**Installation note:** This setup EXE is not yet code signed. Windows SmartScreen may show an *Unknown publisher* warning; download only from this official repository.
