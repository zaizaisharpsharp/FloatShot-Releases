# FloatShot for Windows

A clean, lightweight screenshot utility for Windows 10 and 11 with a floating screenshot shelf, annotation tools and an in-app updater.

**Latest stable release: v0.12.0**

[**Download FloatShot-Setup.exe**](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases/download/v0.12.0/FloatShot-Setup.exe) · [All releases](https://github.com/zaizaisharpsharp/FloatShot-Releases/releases)

Download the single Windows EXE and double-click to install. No ZIP extraction or .NET SDK is needed. FloatShot creates a Start menu shortcut and an entry in Windows **Settings → Installed apps**. Existing users can continue updating directly in the app.

## What's new in v0.12.0

**Region video recording, floating video thumbnails, improved scrolling capture, and a high-contrast selection cursor.**

- **Capture a video region:** Choose Record Screen, drag an area within one monitor, and record only that selection.
- **Recording controls:** Pause, Resume, Stop & Preview, and Delete are available during recording. Video is exported to local H.264 MP4 using a bundled, verified encoder.
- **Video Quick Access:** A floating thumbnail appears after stopping, with an actual recorded video frame and Play, Save As, Done, and Delete.
- **Scrolling screenshots:** After selecting content, choose Manual Scroll or Auto-scroll. Finish assembles aligned sections, while Cancel discards them; a single unscrolled image is not saved as a scrolling capture.
- **Better visibility:** The selection cursor has white and black contrast so it can be seen against bright and dark backgrounds.
- **Update recovery:** Portable or nonstandard installations now show an active Get Installer button rather than a disabled Download Update button.
- **Verification:** Windows interaction tests, an actual region recording with Pause/Resume, playable MP4 validation, thumbnail frame extraction, installer installation, updater package and checksum checks all passed.

**Current limitations:** Video recording does not yet include microphone or system sound. Scrolling capture may require Manual mode and smaller steps for animated, sticky-header, or virtualized content. Automated Windows tests passed, but physical mouse interactions and scrolling reliability on each device still require confirmation.

[**View the successful v0.12.0 Windows release build**](https://github.com/zaizaisharpsharp/FloatShot-Windows/actions/runs/39013328692)

## What's new in v0.11.2

**Reliable updates and a new What's New experience.** This release repairs a stuck Restart & Install flow and shows a compact list of improvements before the user downloads an update.

- **Updater no longer freezes behind floating cards:** Already-captured screenshot cards are safely saved to the capture folder and dismissed before restarting, while unfinished edits and recordings remain protected.
- **Check Again and retry now work:** A verified download no longer blocks checking the official channel, and a newer version can replace an older staged download.
- **Recover interrupted updates:** Verified staged downloads are remembered across app restarts. If replacement fails, the updater records the failure, restores the previous installed version where possible, and offers another attempt.
- **New release highlights:** The Updates window displays scrollable version-specific What's New bullets and a link to full release notes, using the new release manifest metadata.
- **Installer safety and diagnostics:** Transactional file replacement, a retained backup, restart checks, and logged errors.
- **Tested on Windows:** The build exercised updater view state, filesystem rollback, saved screenshot preservation, WPF editor/capture regression tests, silent installer installation, and SHA-256 integrity of the update ZIP.

**For users whose previous updater is stuck:** Install v0.11.2 once using the installer link above. After that, future versions can use the revised update process. Saved screenshots and app settings are retained by the per-user installer. Automated tests cannot guarantee every machine-specific startup/antivirus interaction, so any failed attempt will be logged.

[**View the successful v0.11.2 Windows build**](https://github.com/zaizaisharpsharp/FloatShot-Windows/actions/runs/39009886285)

## What's new in v0.11.1

**Editor selection, resize and deletion repair, with a slimmer annotation inspector**

- **Fixed object manipulation:** Completing a circle, redaction or other annotation automatically switches to Select. Clicking an existing annotation selects it, even if a drawing tool was previously active, instead of drawing another shape.
- **Move and resize:** Drag inside an annotation to move it; drag a corner or edge handle to resize the existing object. Screenshot pixels and export resolution remain unchanged.
- **Delete selection:** A dedicated **⌫ Delete** toolbar action and the **Delete** or **Backspace** keys remove the selected annotation. Undo restores it.
- **Compact controls:** Small color swatches, custom color picker, narrow stroke-width inspector, and contextual font controls replace the large styling row.
- **Stronger Windows regression tests:** A real pointer-operation state machine check covers drawing, reselecting, dragging, resizing, toolbar deletion, Backspace, Undo and redaction repositioning. Existing screenshot export, recorder, OCR, scrolling, WPF, installer and update-integrity tests remain in the Windows build pipeline.

The Windows CI suite passed. Please also test the mouse gestures on your device; CI does not replicate every DPI configuration or input driver.

## What's new in v0.11.0

**Window targeting and three native capture workflows.** This version adds built-in local text recognition, a scrolling screenshot workflow, and MP4 recording, alongside stronger visible-window selection.

- **Smarter Window Capture:** Ignores minimized, cloaked, off-screen, and stale controls. Uses pixels currently visible on-screen instead of attempting to capture hidden internal window surfaces. Hover to select an accessible item, use Tab/Space to change target level, or drag an exact region.
- **Capture Text (OCR):** Select a region and recognize English text locally. Correct the extracted text, copy it, or save a `.txt` file. No cloud upload is required.
- **Scrolling Capture:** Select a content area, let FloatShot scroll and match overlapping image strips, and save a tall screenshot. The stitcher stops when it cannot safely align the content rather than insert fabricated image rows.
- **Record Screen:** Records a **silent whole-monitor MP4** from the monitor under the cursor with a floating Stop control. Files are saved locally under `FloatShot Captures/Recordings`. **Region-cropped recording and microphone/system audio are not yet supported.**
- **Validation:** Windows build, real OCR recognition, a short MP4 recording, scroll-stitch pixel comparisons, installer installation, update ZIP, and SHA-256 integrity checks passed.

**Compatibility note:** Capture targets vary by app and display configuration. Some custom UI, protected applications, animated pages, and virtualized scrolling lists may require manual area capture. Windows Graphics Capture support and video encoding capability are required for recording. The release has passed automated Windows tests; interactive behavior across individual PCs still needs real-device confirmation.

[**View successful v0.11.0 Windows release build**](https://github.com/zaizaisharpsharp/FloatShot-Windows/actions/runs/39007635459)

## What's new in v0.10.0

**Professional screenshot editor overhaul:** The editor has been rebuilt to correct lost annotations and stretched shapes. It now stores markup as editable objects until export and renders the final image at the source screenshot's exact resolution.

- **Done really applies your work.** It saves the actual flattened edited image and updates the existing floating screenshot preview to the new version. The unedited original stays untouched as a backup.
- **Redaction and shapes no longer distort the screenshot.** Solid redaction exports fully opaque black pixels. Circles, rectangles, arrows, pen strokes and highlights are rendered independently of display zoom.
- **Move, resize, restyle.** Select an annotation, drag it, use the eight resize handles, change its color (including a custom color), adjust stroke thickness, nudge with arrow keys, or Delete. Ctrl+Z/Ctrl+Y support Undo/Redo.
- **Text formatting.** Add text, double-click to edit it, drag to reposition, resize the text box, choose fonts, font size, text color and bold.
- **Modern editor commands.** Compact annotation tools, Save as..., Done, Copy, Pin, Quick Access, Drag Me and Fit/50–200% zoom. Zoom changes the editor preview, not export dimensions.
- **Combine 2–4 images.** Choose Combine in the editor, select up to three more images, reorder them, and arrange into a two-column grid, horizontal row or vertical stack. Change gaps, padding and light/dark background. Proportions are preserved, and the combined result opens for further annotation.
- **Regression tests expanded.** Windows CI checks exported redaction pixels, moved redaction, ellipse colors, text content and movement, Undo/Redo, four-tile grid placement and whether Done actually replaces the original floating card. It also tests Windows UI startup, installer registration and updater ZIP/checksum integrity.

**Note:** Editor markup remains editable while the window is open. Saving a PNG/JPEG flattens it, and there is not yet a separate persistent editable project format. Windows CI validates functionality but cannot replace hands-on mouse and visual tests across every DPI/display configuration.

## What's new in v0.9.1

**Smart subwindow capture**, based on feedback that previous versions could highlight only entire app windows:

- **Hover over an accessible control, navigation item, sidebar, or section:** The selection outline changes to the smaller UI region rather than always covering the entire browser or app.
- **Click** to capture the highlighted area, without taking a screenshot of the whole containing window.
- **Tab** steps through larger enclosing regions and **Shift+Tab** moves inward. Press **Space** to toggle complete-window selection; **Enter** to capture; **Esc** to cancel.
- **Drag** to capture any exact rectangle manually, including content that doesn't expose accessibility boundaries.
- **Background detection:** Accessibility inspection runs off the user-interface thread; the selection rectangle and cursor remain responsive.
- **Target-specific Windows regression:** The CI test constructs two distinct navigation controls and verifies the selector detects subregions at each position, rather than returning only the whole parent window. The installer and updater integrity tests also passed.

This is a Windows accessibility-based best-effort feature, not a claim that every custom-drawn webpage exposes UI-element bounds. Chrome/Edge and desktop apps usually support UI Automation, but custom canvases, games and protected windows may need manual drag. While the picker is active, the underlying site may not receive new hover-triggered mouse events.

## What's new in v0.9.0

- **Window targeting with a live camera badge:** Choose Capture Window or press **Ctrl+Shift+4**, move the pointer over the window you want, and click the highlighted window to capture. Esc cancels. This replaces the old delayed foreground-window guess.
- **All-In-One immediately shows an editable crop:** The screen dims around a clear preselected rectangle with eight grab handles. Move the area by dragging inside; resize at a handle/edge; drag outside to start a new selection. Press Enter or click Capture area to finish, Esc to cancel. Fullscreen, Window and Timer modes remain available from its compact dock.
- **Choose what double-clicking a floating thumbnail does:** In **Settings → Quick Access → Double-click**, choose **Save + Windows viewer**, **Windows viewer (temporary)**, or **Open FloatShot editor**. The pencil continues to open the editor regardless of that setting.
- **Refined annotation workspace:** More compact icon tools for pen, highlighter, redaction, shapes, arrows and text. **Save as...** chooses a filename/location, and **Done** saves an edited copy to the configured capture folder.
- **Zoom and sharing from the editor:** **Fit**, 50%, 67%, 100%, 125%, 150% and 200% zoom are display-only; exported screenshots remain at original pixel size. The bottom bar offers Copy, Pin, Quick Access, and **Drag Me** for dragging the edited screenshot as a real file into another application.
- **Windows regression checks:** The updated CI smoke checks that All-In-One opens with a real adjustable crop, that the editor route works from Quick Access, and that the existing shelf, tray, window capture, installer and update integrity tests continue to pass.

**Not yet available:** CleanShot-style scrolling capture, OCR, full video/audio recording, editable project files, and background templates. FloatShot does not claim these are working.

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

**Capture History** shows your saved screenshots with lighter previews, Open, Copy, Edit, Pin and Delete. **Settings → Quick Access → Double-click** can now route the preview to the FloatShot annotation editor instead of the default Windows viewer. Press **Ctrl+F** to search filenames. **Settings → About → View FloatShot release information** opens this page for feature descriptions, build verification and help.

## How updates work

Open FloatShot → **Check for Updates**. If a new version is available, choose **Download Update**, wait for checksum verification, then **Restart & Install**. The app doesn't close just because the download finishes.

For a clean reinstall or when the in-app updater is inaccessible, use **FloatShot-Setup.exe** above. The setup installs over existing versions while preserving your preferences and exported screenshots.

## Build verification

The v0.12.0 public release passed the full Windows pipeline:

- Self-contained .NET 8 x64 WPF compilation and creation of the branded Windows icons.
- Real Windows window creation and tray-menu dispatch checks, including **left-click Capture Area**, **right-click menu toggle**, **outside-click dismissal**, **hidden tray icon restoration**, Settings, About, Capture History, window selection and monitor/window capture dimension tests.
- **Screenshot regressions:** three floating cards were created, independent middle-card dismissal and shelf reflow were verified, adjustable size/gap settings were exercised, and pinned full-image rendering was checked.
- Inno Setup EXE compilation, silent Windows installation, executable/marker/Start-menu verification and Windows uninstall registration checks.
- Version validation, ZIP integrity, and SHA-256 update-manifest checks.

[**View the successful v0.11.1 Windows build**](https://github.com/zaizaisharpsharp/FloatShot-Windows/actions/runs/39008465680) (private source repository; requires authorized access).

Automated tests don't replace visual testing on every monitor or third-party app. Capture behavior with protected or hardware-accelerated windows can vary due to Windows limitations.

## Troubleshooting

If a command fails, diagnostics are stored at
`%LOCALAPPDATA%\FloatShot\logs\diagnostics.log`.

If you selected **Hide FloatShot Tray Icon**, reopen FloatShot from Windows Start to restore it. This does not forcibly pin the icon beside the battery; the Windows taskbar controls overflow placement.

If Windows still shows an old taskbar icon after the new version is installed, unpin the old shortcut and pin FloatShot again from the Start menu. Windows may cache pinned shortcut icons.

FloatShot does not currently include cloud upload or video recording with microphone/system audio. v0.12.0 supports silent cropped-region MP4 recording, local English OCR, and manual/automatic scrolling screenshots; supported behavior depends on Windows and target-app capabilities.

**Installation note:** This setup EXE is not yet code signed. Windows SmartScreen may show an *Unknown publisher* warning; download only from this official repository.
