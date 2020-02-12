Name:		latte-dock
Summary:	Latte is a dock based on plasma frameworks
Version:	0.9.8.1
Release:	1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://github.com/psifidotos/Latte-Dock
Source0:	http://download.kde.org/stable/latte-dock/%{name}-%{version}.tar.xz
Patch0:		latte-dock-default-config.patch
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5PlasmaQuick)
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5Package)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5SysGuard)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(sm)
BuildRequires:	qt5-qtgraphicaleffects
Requires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtquickcontrols
Requires:	qt5-qtquickcontrols
BuildRequires:	plasma-framework
Requires:	plasma-framework

%description
Latte is a dock based on plasma frameworks that provides 
an elegant and intuitive experience for your tasks and 
plasmoids. It animates its contents by using parabolic 
zoom effect and tries to be there only when it is needed.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%doc README.md
%{_sysconfdir}/xdg/latte-indicators.knsrc
%{_libdir}/qt5/plugins/kpackage/packagestructure/latte_packagestructure_indicator.so
%{_datadir}/kservicetypes5/latte-indicator.desktop
%{_datadir}/latte
%{_bindir}/%{name}
%{_libdir}/qt5/qml/org/kde/latte
%{_datadir}/plasma/shells/org.kde.latte.shell
%{_datadir}/plasma/plasmoids/org.kde.latte.*
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/org.kde.latte-dock.desktop
%{_iconsdir}/hicolor/*/apps/*.svg
%{_iconsdir}/breeze/*/*/*.svg
%{_datadir}/kservices5/*.desktop
%{_datadir}/knotifications5/lattedock.notifyrc
%{_datadir}/dbus-1/interfaces/org.kde.LatteDock.xml
%{_sysconfdir}/xdg/latte-layouts.knsrc
%{_libdir}/qt5/plugins/plasma_containmentactions_lattecontextmenu.so
