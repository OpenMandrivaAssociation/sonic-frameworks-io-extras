#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major %(echo %{version} |cut -d. -f1)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define plasmaver %(echo %{version} |cut -d. -f1-3)

Name: sonic-frameworks-io-extras
Version:	26.04.1
Release:	%{?git:0.%{git}.}1
URL:      https://github.com/Sonic-DE/sonic-frameworks-io-extras
Source0:  %url/archive/%version/%name-%version.tar.gz
Source1000: %{name}.rpmlintrc
# https://bugzilla.samba.org/show_bug.cgi?id=12466
Patch1: sonic-frameworks-io-extras-smb_anon.patch
Patch2: sonic-frameworks-io-extras-libproxy-header-location.patch
Summary: SonicDE I/O Extras
License: GPL
Group: System/Libraries
BuildRequires: gperf
BuildRequires: openslp-devel
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(libmtp)
BuildRequires: pkgconfig(libtirpc)
BuildRequires: pkgconfig(OpenEXR)
BuildRequires: pkgconfig(phonon4qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(QCoro6)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: pkgconfig(libssh) >= 0.8.6
BuildRequires: pkgconfig(smbclient)
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(libplist-2.0)
BuildRequires: pkgconfig(libappimage)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6IconThemes)

# pending rename
# BuildRequires: cmake(KF6KIO)
# BuildRequires: cmake(PlasmaActivities)
BuildRequires: %{_lib}SonicFrameworksIO-devel
BuildRequires: %{_lib}SonicActivities-devel

BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(PlasmaActivitiesStats)
BuildRequires: cmake(KExiv2Qt6)
BuildRequires: cmake(KDSoapWSDiscoveryClient)
BuildRequires: cmake(KF6Notifications)
BuildRequires: kdsoap-qt6-devel
Requires: %{mklibname sonicio_archive6} = %{EVRD}
Requires: sonic-frameworks-io
%define sonicio_archive_devel %{mklibname -d sonicio_archive6}

Conflicts: kio-extras

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
%summary

%libpackage sonicio_archive6 6

%package -n %{sonicio_archive_devel}
Summary: Development files for the Sonic Frameworks IO Archive library
Group: Development/SonicDE and Qt
Requires: %{mklibname sonic-io_archive6} = %{EVRD}

%description -n %{sonicio_archive_devel}
%summary

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kio-extras.categories
%{_qtdir}/plugins/*.so
%{_qtdir}/plugins/kf6/kio/*.so
%{_qtdir}/plugins/kf6/kiod/*.so
%{_qtdir}/plugins/kf6/kded/*.so
%{_qtdir}/plugins/kf6/kfileitemaction/kactivitymanagerd_fileitem_linking_plugin.so
%{_qtdir}/plugins/kf6/kfileitemaction/forgetfileitemaction.so
%{_qtdir}/plugins/kf6/thumbcreator
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_netpref.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_proxy.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_webshortcuts.so
%{_datadir}/mime/packages/org.kde.kio.smb.xml
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/dbus-1/services/*.service
%{_datadir}/remoteview
%{_datadir}/kio_info
%{_datadir}/konqueror/dirtree/remote/*.desktop
%{_datadir}/solid/actions/solid_mtp.desktop
%{_datadir}/solid/actions/solid_afc.desktop
%{_datadir}/qlogging-categories6/kio-extras.renamecategories
%{_libdir}/libexec/kf6/smbnotifier
%{_datadir}/applications/kcm_netpref.desktop
%{_datadir}/applications/kcm_proxy.desktop
%{_datadir}/applications/kcm_trash.desktop
%{_datadir}/applications/kcm_webshortcuts.desktop
%{_datadir}/kio_filenamesearch
%{_libdir}/libexec/wpad-detector-helper

%files -n %{sonicio_archive_devel}
%{_includedir}/KioArchive6
%{_libdir}/cmake/KioArchive6
