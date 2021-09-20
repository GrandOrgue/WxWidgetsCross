#
# spec file for package mingw64-wxWidgets-3_0
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mingw64-wxWidgets-3_0
Version:        3.0.2
Release:        12.996
Summary:        C++ Library for Cross-Platform Development
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://wxwidgets.org/

Source:         http://downloads.sf.net/wxwindows/wxWidgets-%{version}.tar.bz2
Patch1:         Fix-calculation-of-space-for-bitmap-in-wxButton.patch
Patch2:         soversion.diff
Patch3:         16849.diff
Patch4:         3.0.2-stc-gcc6.patch
Patch5:         16984-1.patch
Patch6:         16984-2.patch
Patch7:         0001-fix-msw-accessibility.patch
Patch8:         fix-msw-ConvertToImage-alpha.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  mingw64-cross-binutils
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-cross-gcc-c++
BuildRequires:  mingw64-cross-pkg-config
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-libexpat-devel
BuildRequires:  mingw64-libjpeg-devel
BuildRequires:  mingw64-libpng-devel
BuildRequires:  mingw64-libtiff-devel
BuildRequires:  mingw64-zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# %_mingw64_package_header_debug
BuildArch:      noarch
#!BuildIgnore:  post-build-checks
Requires:       mingw64-libwx_baseu_suse1
Requires:       mingw64-libwx_baseu_net_suse1
Requires:       mingw64-libwx_baseu_xml_suse1
Requires:       mingw64-libwx_mswu_adv_suse1
Requires:       mingw64-libwx_mswu_aui_suse1
Requires:       mingw64-libwx_mswu_core_suse1
Requires:       mingw64-libwx_mswu_gl_suse1
Requires:       mingw64-libwx_mswu_html_suse1
Requires:       mingw64-libwx_mswu_media_suse1
Requires:       mingw64-libwx_mswu_propgrid_suse1
Requires:       mingw64-libwx_mswu_qa_suse1
Requires:       mingw64-libwx_mswu_ribbon_suse1
Requires:       mingw64-libwx_mswu_richtext_suse1
Requires:       mingw64-libwx_mswu_stc_suse1
Requires:       mingw64-libwx_mswu_webview_suse1
Requires:       mingw64-libwx_mswu_xrc_suse1

%description
wxWidgets is a free C++ library for cross-platform GUI.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif, MS Windows, MacOS X, Windows CE, GPE) from the same source code.

%package -n mingw64-libwx_baseu_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_baseu_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_baseu_net_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_baseu_net_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_baseu_xml_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_baseu_xml_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_adv_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_adv_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_aui_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_aui_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_core_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_core_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_gl_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_gl_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_html_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_html_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_media_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_media_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_propgrid_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_propgrid_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_qa_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_qa_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_ribbon_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_ribbon_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_richtext_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_richtext_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_stc_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_stc_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_webview_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_webview_suse1
Library for the wxWidgets cross-platform GUI.

%package -n mingw64-libwx_mswu_xrc_suse1
Summary:        wxWidgets-wxMSW library
Group:          System/Libraries

%description -n mingw64-libwx_mswu_xrc_suse1
Library for the wxWidgets cross-platform GUI.

%package devel
Summary:        Everything needed for development with wxWidgets/wxMSW
Group:          Development/Libraries/C and C++

%description devel
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif, MS Windows, MacOS X, Windows CE, GPE) from the same source code.

This package contains all files needed for developing with wxMSW.

%lang_package
%_mingw64_debug_package

%prep
%setup -q -n wxWidgets-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p0

%build
%{_mingw64_configure} --enable-stl --enable-release --enable-debug --enable-accessibility \
	--enable-vendor=suse
make %{?_smp_mflags} -j2

%install
b=%{buildroot}
make DESTDIR="$b" install %{?_smp_mflags}
mkdir -p "$b/%{_mingw64_bindir}"
mv -v "$b/%{_mingw64_libdir}"/*.dll "$b/%{_mingw64_bindir}/"
mkdir -p "$b/%{_prefix}/%{_mingw64_target}/bin"
ln -s "%{_mingw64_bindir}/wx-config" "$b/%{_prefix}/%{_mingw64_target}/bin/"
%find_lang wxmsw
%find_lang wxstd

%files
%defattr(-,root,root)

%files -n mingw64-libwx_baseu_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_baseu_gcc_suse-1.dll

%files -n mingw64-libwx_baseu_net_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_baseu_net_gcc_suse-1.dll

%files -n mingw64-libwx_baseu_xml_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_baseu_xml_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_adv_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_adv_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_aui_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_aui_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_core_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_core_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_gl_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_gl_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_html_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_html_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_media_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_media_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_propgrid_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_propgrid_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_qa_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_qa_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_ribbon_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_ribbon_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_richtext_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_richtext_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_stc_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_stc_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_webview_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_webview_gcc_suse-1.dll

%files -n mingw64-libwx_mswu_xrc_suse1
%defattr(-,root,root)
%_mingw64_bindir/libwx_mswu_xrc_gcc_suse-1.dll

%files devel
%defattr(-,root,root)
# Complete documentation is available in the docs packages.
%doc docs/*.txt
%{_prefix}/%{_mingw64_target}/bin/wx*
%{_mingw64_bindir}/wx-config*
%{_mingw64_bindir}/wxrc*
%{_mingw64_includedir}/wx*
%{_mingw64_libdir}/libwx*.dll.a
%{_mingw64_libdir}/wx/
%{_mingw64_datadir}/aclocal/
%{_mingw64_datadir}/bakefile/

%files lang -f wxmsw.lang -f wxstd.lang

%changelog
* Wed May 13 2015 martin.koegler@chello.at
- Fix #16984
- Provide missing package
* Fri Nov  7 2014 jengelh@inai.de
- Update to new upstream release 3.0.2
  * Generic:
  * Fix silent data loss in wx[F]File::Write(wxString) if conversion
  fails.
  * Make wxString::FromCDouble() work when the global C++ locale is
  not the C one.
  * Fix mouse handling in wxNotebook containing wxListCtrl.
  * wxMSW:
  * Fix background of wxRadioBox buttons and wxSlider.
  * Fix appearance of wxToggleButtons with non default colours.
  * Fix drawing on wxDC when using right-to-left layout.
  * Fix wxGrid appearance and behaviour in RTL.
  * Fix creating wxBitmap from monochrome wxIcon or wxCursor.
  * Fix handling of bitmaps with alpha in wxImageList.
  * Add paragraph spacing attributes support to wxTextCtrl.
  * Show new style directory selector even for non existent paths.
  * Fix order of radial gradient stops.
  * Fix font created using wxFont(wxFontInfo()) ctor.
  * Fix wxFileName::GetShortcutTarget() in console applications.
  * Fix wxFileName::MakeRelativeTo() for shortcut files.
  * Fix height of initially empty wxBitmapComboBox.
  * Fix setting label of submenu items.
  * Fix using Esc as accelerator in the menus.
  * Fix wrong initial status bar height in some cases.
- Bump SONAME due to changed ABI, add soversion.diff.
* Mon Jun 16 2014 jengelh@inai.de
- Update to new upstream release 3.0.1
  * wxHTML displays tables much faster now.
  * Double clicking wxGrid columns doesn't make them too small
  any more.
  * Fix bugs when dragging columns in wxGrid with hidden columns.
  * Loading ICO files with PNG data is now supported.
  * wxBitmapComboBox works again and doesn't just remain blank.
  * Checkboxes in wxDataViewCtrl work again too now.
  * wxCheckListBox appears correctly when using large fonts.
  * There are also many other bug fixes, including many improvements
  to alpha transparency handling in different places.
* Fri Jun  6 2014 jengelh@inai.de
- Put host tools in /usr/i686-w64-mingw32/bin
* Thu Jun  5 2014 jengelh@inai.de
- Use system libraries instead of bundled versions:
  libexpat, libjpeg, libpng, libtiff, zlib
* Thu Mar  6 2014 fstrba@suse.com
- Remove the *-static package
  * The policy of this repo is not to provide static libraries
    with very few exceptions (win_iconv for instance).
* Thu Nov 14 2013 jengelh@inai.de
- Update to new upstream release 3.0.0
  * wxWidgets is now always built with Unicode support but provides
  the same simple (i.e. "char *"-tolerant) API as was available
  in ANSI build in the past.
  * wxWidgets may now use either wchar_t (UTF-16/32) or UTF-8
  internally, depending on what is optimal for the target
  platform.
  * New webview library, implementing wxWebView: a wrapper for the
  native platform web engine with full support for HTML and
  JavaScript.
  * New propgrid library containing wxPropertyGrid and related
  classes.
  * New ribbon library for advanced toolbars.
  * Event loops, timers and sockets can now be used in wxBase,
  without GUI.
  * Events can now be connected to any functor, not necessarily a
  method of wxEvtHandler-derived class. The compile-time safety
  was also improved.
  * Documentation for wxWidgets has been converted from LaTex to
  C++ headers with Doxygen comments and significantly improved in
  the process (screenshots of various controls were added, more
  identifiers are now linked to their definition &c).
  * Support for persistent objects automatically saving and
  restoring their state was added.
- Drop wxWidgets-to-wxpython-2.9.4.0.patch (merged upstream)
* Thu Aug 22 2013 jengelh@inai.de
- Use %%_smp_mflags for parallel build and better make install call.
* Thu Apr 11 2013 fisiu@opensuse.org
- Build wxWidgets with webview support.
* Thu Oct 25 2012 sbrabec@suse.cz
- Provide wxWidgets-3_0*-devel for future compatibility.
- Add "API version" in %%description.
- Backported fixes from 2.8 branch.
- Included post-release fixes from wxpython.
* Thu Sep 20 2012 coolo@suse.com
- add explicit buildrequire on pkgconfig(glu)
* Mon Jul 23 2012 sbrabec@suse.cz
- Fixed wx-config symlink (bnc#772528).
* Thu Jul 19 2012 sbrabec@suse.cz
- Update to version 2.9.4.
* Fri Apr 27 2012 sbrabec@suse.cz
- Backported fixes of the dependency generator from 2.8 branch
  (bnc#757124, bnc#759287#c3).
* Thu Apr 19 2012 sbrabec@suse.cz
- Added support for Fedora compatible 24c variants (bnc#660438).
- Change name of compat-lib-config virtual provide to not clash
  with package name, fix requires/provides generator (bnc#757124).
* Mon Apr  2 2012 sbrabec@suse.cz
- Update to version 2.9.3.
* Wed Dec 21 2011 coolo@suse.com
- own aclocal directory, there is no other reason to buildrequire
  automake
* Mon Oct 17 2011 coolo@suse.com
- fix whitespace of spec file
* Wed Aug  3 2011 sbrabec@suse.cz
- Updated to version 2.9.2.
* Tue Jul 26 2011 aj@suse.de
- Recommend instead of require lang package.
* Tue May 17 2011 sbrabec@suse.cz
- Create synthetic .la files to work-around libtool failures when
  linking third level libraries or binaries (bnc#690952).
* Fri Apr  8 2011 sbrabec@suse.cz
- Do not use bash coproc on system with bash-3.
* Tue Mar 29 2011 sbrabec@suse.cz
- Fixed find-wx-requires to check directories instead of library
  name. Provide find-wx-provides. (bnc#681409)
* Thu Dec 23 2010 sbrabec@suse.cz
- Updated to version 2.9.1.
- Rename package to wxWidgets to follow upstream base name.
- Split wxPython documentation to a separate package.
- Build Unicode/ANSI, standard/debug and STL/wx container versions
  separately.
- Spec file completely rewritten.
* Sun Aug 15 2010 termim@gmail.com
-  Updated to version 2.8.11.0
  Adds Python 2.7 builds, PySlices, new pubsub implementation,
  lots of updates to AGW, and lots of bugs fixed.
-  Removed wxGTK-GSocket-clash.patch and wxGTK-editra-ebmlib.patch
  as already fixed.
* Tue Jun 15 2010 sbrabec@suse.cz
- Added --enable-graphics_ctx to fix Editra (bnc#580060).
- Added ebmlib file required by Editra (bnc#580060,
  patch from Salix).
* Mon Feb 22 2010 crrodriguez@opensuse.org
- build with PIC
* Thu Jan 28 2010 sbrabec@suse.cz
- Enabled media libraries (bnc#565039).
* Fri Sep 25 2009 sbrabec@suse.cz
- Disabled STL (bnc#530027). See also
  http://lists.opensuse.org/opensuse-factory/2009-09/msg00386.html
- Removed obsolete RPATH.
- The GSocket symbol clash fix replaced by the upstream one.
* Thu Sep 17 2009 matejcik@suse.cz
- fixed pth file to point to platlib
* Sat Sep  5 2009 sbrabec@suse.cz
- Fixed for the latest python package.
* Fri Aug  7 2009 sbrabec@suse.cz
- Updated to version 2.8.10.1:
  * Incompatible change in wxTreeCtrl behaviour!
  * Added several functions forward compatible with wxWidgets 3.0.
  * Add wxBU_EXACTFIT support to wxToggleButton XRC handler.
  * wxHashMap::insert() doesn't update the value if it didn't
    insert the element any more.
  * Correct bug in wxTimeSpan::Format() for negative spans.
  * Correct several bugs in wxList using end() iterators.
  * Translation updates.
  * Fix wxURL::GetInputStream() for URLs with special characters in
    credentials.
  * Fix wxURI::GetUser() for URIs without password.
  * Correct wxDateTime DST computation for 2006 and later.
  * wxRTC: fixed a problem with HTML list generation.
  * wxRTC: no longer deletes a character when content is selected
  before pressing Delete.
  * wxRTC: fixed inability to select no superscript and no
  subscript in formatting dialog.
  * wxRTC: fixed centering and right-justification when combined
    with left indentation.
  * wxRTC: fixed lack of right margin when centering or
    right-justifying.
  * wxRTC: fixed wrong descent when wrapping lines with different
    font sizes.
  * wxRTC: fixed wrapping problem for long lines.
  * wxRTC: all buffer margins now respected.
  * wxRTC: Added wxRE_CENTRE_CARET to centre the caret line
    vertically.
  * Fixed wxHTML's pagebreaks computation in tables.
  * Fixed wxHtmlWindow::SelectionToText() to correctly insert
    newlines after single-cell paragraphs.
  * Fixed wxHTML's line breaks handling in <pre> blocks.
  * wxHTML: don't include extra whitespace in table cells.
  * Implemented wxWindow::DragAcceptFiles() on all platforms.
  * Added wxAUI_MGR_LIVE_RESIZE flag to wxAuiManager.
  * Use bitmap mask in wxSplashScreen.
  * Translate "(c)" and "(C)" to the real copyright sign in
    wxAboutBox.
  * Fix painting of highlight border for merged cells in wxGrid.
  * Fix handling of long lines in wxGridCellAutoWrapStringRenderer.
  * Return false from wxSingleInstanceChecker::IsAnotherRunning()
    if an error occurred while opening or reading the lock file.
  * Fixed printing to use fonts sizes adjustment consistent with
    wxMSW.
  * Make colours used by list, tree and status bar controls more
    consistent with the system theme settings.
  * Worked around bug in GTK+ < 2.14 where enabling some controls
    such as wxButton didn't re-enable sensitivity until the mouse
    was moved.
* Thu Jun 18 2009 sbrabec@suse.cz
- Worked-around GSocket name conflict with GIO.
* Tue Feb 17 2009 crrodriguez@suse.de
- build require libexpat-devel so we dont use the bundled one
* Wed Feb  4 2009 pth@suse.de
- Disable the use of precompiled headers as the way wxWidgets uses
  them is not supported by current GCC.
* Tue Feb  3 2009 pth@suse.de
- Update to 2.8.9.1:
  * Optimize wxString::Replace() for single character arguments.
  * Updated Hindi translation.
  * Use tr1::unordered_{map,set} for wxHash{Map,Set} implementation if available
    in STL build; in particular do not use deprecated hash_{map,set} which
    results in a lot of warnings from newer g++.
  * Added support for reading alpha channel in BMP format.
  * Fixed help viewer bug whereby the splitter sash in wxHtmlHelpWindow could
    go underneath the left-hand pane, permanently, after resizing the
    help window.
  * Fixed wxHTML default font size for printing to be 12pt regardless of the
    platform, instead of depending on GUI toolkit's screen configuration.
  * Support wxDP_ALLOWNONE style in generic wxDatePickerCtrl version.
  * Set wxKeyEvent::m_uniChar correctly in the events generated by generic
    wxListCtrl.
  * Fix changing size of merged cells in wxGrid.
  * Fixed wrapping bug in wxRichTextCtrl when there were images present;
    now sets the cursor to the next line after pressing Shift+Enter.
  * Fixed Cmd+Back, Cmd+Del word deletion behaviour in wxRichTextCtrl.
  * Fix crash when reading malformed PCX images.
  * Fix bug with wrong transparency in GIF animations.
  * Store palette information for XPM images in wxImage.
  * Fixed selection bugs and auto list numbering in wxRichTextCtrl.
  * Significantly optimize wxGrid::BlockToDeviceRect() for large grids.
  * Introduced new wxAuiToolBar class for better integration and look-and-feel.
  * Fix a crash in wxAuiFrameManager when Update() was called in between mouse-up
    and mouse-down events
  * wxAUI: added various NULL-ptr asserts.
  * Fixed problem with Floatable(false) not working in wxAuiFrameManager.
  * Fixed maximize bug in wxAUI.
  * Allow period in link anchors in wxHTML.
  * Fixed memory corruption in wxHTML when parsing "&;" in the markup.
  * Fixed event type in EVT_GRID_CMD_COL_MOVE and EVT_GRID_COL_MOVE.
  * wxGrid doesn't steal focus when hiding editor any more.
  * MIME types reading fixed when running under GNOME, reading .desktop
    files and also the default application list.
  * Added filesys.no-mimetypesmanager system option so that applications that
    must load an XRC file at program startup don't have to incur the
    mime types manager initialization penalty.
  * Fixed masking of disabled bitmaps in wxMenuItem and wxStaticBitmap.
  * Fixed generation of events for an initially empty wxDirPickerCtrl.
  * Fixed detection of Meta key state so that NumLock isn't misdetected
    as Meta (requires GTK+ 2.10).
  * Fix changing font/colour of label in buttons with images.
- Make funtion return a value.
* Wed Sep  3 2008 sbrabec@suse.cz
- Updated to version 2.8.8.1:
  * many API-compatible fixes and improvements, see
    docs/changes.txt for complete list
* Mon Sep  1 2008 sbrabec@suse.cz
- Dropped obsolete ODBC support (bnc#397044).
* Fri May  2 2008 sbrabec@suse.cz
- Don't unload libgnomevfs-2.so.0 on exit (bnc#380267).
- Removed obsolete configure options (bnc#380267#c7).
* Fri Mar 28 2008 sbrabec@suse.cz
- Updated to version 2.8.7.1:
  * many API-compatible crash fixes, improvements and other fixes,
    see docs/changes.txt for complete list
* Tue Oct  2 2007 sbrabec@suse.cz
- Updated to version 2.8.6.0:
  * many API-compatible crash fixes, improvements and orger fixes,
    see docs/changes.txt for complete list
  * fixed bugs and inconsistencies in wxWidgets and wxPython
* Thu Sep 13 2007 prusnak@suse.cz
- corrected last patch (gtk_border_free.patch) [#294693]
* Wed Sep  5 2007 bwalle@suse.de
- fix crash on startup on x86_64 (#294693)
* Wed Aug 29 2007 prusnak@suse.cz
- pack non-unicode libraries as wxGTK-compat package (again)
- run ldconfig in post/postun scriptlets
* Wed May 23 2007 prusnak@suse.cz
- update to 2.8.4.0
  * changes are too numerous to list, see changes.txt for full list
- drop non-unicode libraries (not used anymore)
- cleaned spec file
* Mon Mar  5 2007 pth@suse.de
- Don't hardcode lib64 in .spec file.
- Replace contrib/samples/applet/monitors.c once again (see #203607).
* Thu Mar  1 2007 pth@suse.de
- Update to 2.8.1.1. Changes are too numerous to list, see
  changes.txt for a full list.
- fix use of uninitialised variables wxPython_int.h
- Correct spelling in README.unicode
* Mon Dec 11 2006 sbrabec@suse.cz
- Source code cleanup (#226403).
* Tue Sep  5 2006 sbrabec@suse.cz
- Repackaged without undistributable monitors.c (#203607).
* Mon Aug  7 2006 sbrabec@suse.cz
- Updated to version 2.6.3.3 (#162198):
  * Fixed crash when loading message catalogs in Unicode build.
  * Fixed crash in wxList code when building with wxUSE_STL=1
  * Spurious error message from wxLaunchDefaultBrowser fixed.
  * Compilation fixes for (more strict) g++ 4.1
  * Speed improvements to wxRegEx
  * Fix regerror and regfree name conficts
  * wxCondition::WaitTimeout() now returns correct value
  * Bug in wxLogStream::DoLogString in Unicode builds fixed
  * wxFileName now also looks for TMPDIR on Unix
  * Fixed occasional wxThread cleanup crash
  * wxImage::Copy() forgot the alpha channel
  * Fixed wxSocketBase::InterruptWait on wxBase
  * wxSocket::_Read continues reading from socket after exhausting
    pushback buffer
  * Fixed abort() on loading invalid PNG image
  * Added space after list item number in wxHTML
  * wxCalendarCtrl drawing, positioning and hit-testing fixes
  * More checking of image validity before loading into wxImage
  * Added double-buffering to wxVListBox and fixed scrolling
  * More than one filter allowed in in wxDocTemplate filter
  * Fixed infinite loop in tab traversal code with wxUSE_STL==1
  * In wxScrolledWindow:DoGetBestSize, no longer adds difference
    between client and total size
  * Fixed problem with zoom setting in print preview
  * Fixed problem with choice editor in wxGrid
  * Fixed problem trying to print from a preview
  * Polygon and line drawing speeded up if there is no scaling
  * Fixed problems with CJK input method (reverted)
  * Fixed wxNotebook::HitTest when the leftmost visible tab is not
    the actual first tab
  * Send wxSetCursorEvent
  * Fix RequestMore for idle events
  * Implement user dashes for PS and GNOME printing
  * Correct update region code
  * Change wxMimeTypesManager code to just read the MIME-types
  * Speed up reading MIME database
  * wxClipboard fixes
  * Support underlined fonts in wxTextCtrl
  * wxWindow and wxScrolledWindow now generate all scroll events
  * Implemented wxToggleButton
  * Fixed wxDb::DBMS() indicating DB2 dBase databases
  * Fixed buffer overflow problem in Unicode builds
- Fixed slash typo patch.
- Do not delete no more generated doslex.c.
* Mon Jul 17 2006 mkudlvasr@suse.cz
- fixed a problem in makefiles.in and configure.in. In many cases
  the variable top_builddir was not separated by a slash. This caused
  many 'file not found' errors.
* Fri Apr  7 2006 mmarek@suse.cz
- fix array subscript out of range in src/common/db.cpp
* Thu Mar  9 2006 bk@suse.de
- Add esound-devel to BuildRequires (was implicily by SDL-devel)
- Add explicit gcc-c++ to BuildRequires (was implicit by SDL-devel)
* Tue Feb 28 2006 jmatejek@suse.cz
- updated to reflect python changes due to #149809
* Wed Feb 22 2006 sbrabec@suse.cz
- Moved pywxrc to python-wxGTK (Andreas Hanke, #152573).
* Sun Feb 19 2006 aj@suse.de
- Reduce BuildRequires.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Jan 20 2006 sbrabec@suse.cz
- Package wxrc (#143258, Andreas Hanke).
- Updated README.unicode (#144090, Andreas Hanke).
- Moved bakefile to devel subpackage (#144094, Andreas Hanke).
* Mon Jan 16 2006 sbrabec@suse.cz
- Updated to version 2.6.2.1.
* Mon Sep 19 2005 sbrabec@suse.cz
- Force re-creating the old lex code in doslex.c.
* Fri Aug 19 2005 sbrabec@suse.cz
- Removed references to no more provided PangoRenderX calls.
* Mon Aug  1 2005 sbrabec@suse.cz
- Updated to version 2.6.1.0.
* Sat May 14 2005 schwab@suse.de
- Fix undefined operation.
* Wed Apr 27 2005 mcihar@suse.cz
- update to 2.6.0.0
* Fri Apr 15 2005 mcihar@suse.de
- build with system libtiff
- enabled SDL and sound support
* Wed Apr 13 2005 mcihar@suse.cz
- fix filelist
- fix build on 64-bit machines
* Tue Apr 12 2005 mcihar@suse.cz
- disable SDL support, it seems to be broken in this version
* Tue Apr 12 2005 mcihar@suse.cz
- update to 2.5.5.1
* Fri Feb  4 2005 tiwai@suse.de
- fixed the confliction of ATTRIBUTE_PRINTF* macros.
* Wed Dec 22 2004 mcihar@suse.cz
- fix python-wxGTK requires
* Fri Nov 19 2004 mcihar@suse.cz
- update to 2.5.3.1
* Wed Oct 20 2004 mcihar@suse.cz
- fixed file conflict between python-wxGTK and wxGTK-devel
* Fri Sep 17 2004 mcihar@suse.cz
- really build wxPython version against unicode wxGTK (bug #45539)
* Tue Aug 31 2004 mcihar@suse.cz
- update to 2.5.2.8
* Mon Aug 16 2004 mcihar@suse.cz
- update to 2.5.2.7
* Fri Jul 30 2004 mcihar@suse.cz
- also build non unicode libraries and ship them in wxGTK-compat package
  to allow compilation of application, that weren't written in respect
  to unicode possibility
* Wed Jun  2 2004 mcihar@suse.cz
- add missing wxPython licenses
* Thu Apr 22 2004 mcihar@suse.cz
- ${prefix} was intentional
* Wed Apr 21 2004 mcihar@suse.cz
- correct libdir on lib64
* Tue Apr 20 2004 mcihar@suse.cz
- solved conflict between wxGTK-devel and python-wxGTK
* Wed Apr 14 2004 mcihar@suse.cz
- moved sound_sdl-2.5.1.so from devel package
* Wed Apr 14 2004 mcihar@suse.cz
- build with -fPIC
- add libmspack support (enables access to MS HTML help files - *.chm)
* Tue Apr 13 2004 mcihar@suse.cz
- update to 2.5.1.5
- enable unicode support
- enabled build of contrib libraries
* Thu Mar 18 2004 mcihar@suse.cz
- make files in bin executable (bug #36331)
* Fri Mar  5 2004 mcihar@suse.cz
- little spec file cleanup, debug build can be enabled
* Wed Mar  3 2004 tiwai@suse.de
- fixed wxwin.m4 for the recent autoconf.
- moved wxwin.m4 to devel subpackage.
* Tue Jan 13 2004 mcihar@suse.cz
- enabled build with GTK 2
* Thu Oct 16 2003 mcihar@suse.cz
- do not build as root
- remove orig and rej files that should not be installed
* Wed Oct 15 2003 mcihar@suse.cz
- update to 2.4.2.4
* Fri Aug 29 2003 tiwai@suse.de
- fixed the segfault on 64bit architectures.
* Sat Aug 23 2003 ro@suse.de
- fix build on lib64
* Wed Aug 20 2003 mcihar@suse.cz
- now builds together with wxPython
- created patch for DESTDIR support
- now lives in /usr and not /usr/X11
- build all python bindings (fixes #26138 and #27349)
* Wed Jul 30 2003 adrian@suse.de
- update to version 2.4.1
- add %%run_ldconfig
* Tue May 13 2003 mmj@suse.de
- Package forgotten files
* Tue Mar  4 2003 mmj@suse.de
- Add patch to have wxFileConfigGroup::DeleteSubgroup() not seg-
  fault with pGroup == 0. Triggered by audacity but might affect
  other wxGTK programs. [#24401]
* Tue Feb 25 2003 hhetter@suse.de
- devel package requires gtk-devel (Bug Id#22479)
* Mon Feb 17 2003 hhetter@suse.de
- package gl-header files too ( Bug Id#23094 )
* Wed Jan 22 2003 meissner@suse.de
- Fixed for lib64 platforms.
* Tue Jan 14 2003 hhetter@suse.de
- updated to version 2.4.0
- updated documentation to 2.4.0 revision
- remove all outdated patches
* Tue Nov 12 2002 tcrhak@suse.cz
- fixed for bison 1.75: end rules with semicolons
* Mon Aug 12 2002 garloff@suse.de
- Fix multiple delete[] in wxHtmlTagsModule::OnExit().
* Fri Jul 26 2002 adrian@suse.de
- fix neededforbuild
* Wed May  1 2002 kukuk@suse.de
- Remove superfluous libmpeg from neededforbuild
* Fri Apr 26 2002 coolo@suse.de
- use %%_libdir
* Mon Apr 15 2002 tiwai@suse.de
- fixed build with gcc 3.1.
* Tue Feb 19 2002 hhetter@suse.de
- applied the real patch for the wxgtk-mutex performance problem
* Fri Feb 15 2002 hhetter@suse.de
- configure with --enable-std_iostreams for better support
  for C++ sources using C++ iostreams
- apply patch to fix perfomance problem with multithreaded apps
  (accepted and already in the wxGTK CVS)
* Thu Jan 31 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Thu Jan 24 2002 tiwai@suse.de
- updated to version 2.2.9.
- fixed neededforbuild for libwx_gtk_gl.
- added locale files to filelist.
- added --enable-soname to ensure the correct linking.
- clean up the spec file.
* Mon May  7 2001 mfabian@suse.de
- bzip2 source
* Fri Mar 30 2001 pthomas@suse.de
- Update to 2.2.6
- Renamed to wxGTK
- Split off devel package.
- Build the OpenGl add-on lib.
- Install sample code in docdir.
- Change Makefiles to use DESTDIR.
- Include both HTML and PDF Versions of the manuals.
- Eliminate warnings in C++ code.
- Build with -W -Wall -Wstrict-prototypes -Wpointer-aritth
* Fri Jan 26 2001 hhetter@suse.de
- Update to 2.2.4
* Sat Dec  9 2000 mfabian@suse.de
- Add /usr/X11R6/bin/wxgtk-config to filelist
* Sun Nov  5 2000 ro@suse.de
- fixed neededforbuild
* Fri Jun  9 2000 ro@suse.de
- up to 2.1.16
* Mon Feb 21 2000 uli@suse.de
- now builds with RPM_OPT_FLAGS
* Mon Feb 21 2000 ro@suse.de
- update to 2.1.13
- use suse_update_config macro
- patch to compile with newest gtk
* Fri Jan 14 2000 freitag@suse.de
- update to 2.1.12, URL, doc in seperate tarball
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Aug 19 1999 kukuk@suse.de
- Add /usr/X11R6/bin/wx-config to filelist
* Tue Jul 13 1999 bs@suse.de
- use gtk and glib instead of gtkn and glibn
* Mon May 31 1999 ray@suse.de
- new package
