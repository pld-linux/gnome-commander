Summary:	A GNOME filemanager similar to the Midnight Commander
Summary(pl.UTF-8):	Zarządca plików dla środowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	1.18.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gnome-commander/1.18/%{name}-%{version}.tar.xz
# Source0-md5:	ce35495159319579c086a5c79d9969da
Patch1:		%{name}-gsf.patch
URL:		https://gcmd.github.io/
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exiv2-devel >= 0.14
BuildRequires:	flex >= 2.6.0
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.70.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libgsf-devel >= 1.14.26
BuildRequires:	libsmbclient-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.18
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.70.0
Requires:	exiv2-libs >= 0.14
Requires:	glib2 >= 1:2.70.0
Requires:	gtk+3 >= 3.24.0
Requires:	libgsf >= 1.14.26
Requires:	poppler-glib >= 0.18
Requires:	taglib >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Commander is a filemanager that just like the classical Midnight
commander lets you do everything with the keyboard. It can perform all
standard fileoperations and some extra features like FTP support.

%description -l pl.UTF-8
GNOME Commander to zarządca plików, który podobnie do klasycznego
Midnight Commandera umożliwia pełną obsługę przy pomocy klawiatury.
Zapewnia wykonanie wszystkich typowych operacji na plikach, a także
kilka dodatkowych jak np. klienta FTP.

%prep
%setup -q
%patch -P1 -p1

%build
%meson \
	-Dexiv2=enabled \
	-Dlibgsf=enabled \
	-Dpoppler=enabled \
	-Dsamba=enabled \
	-Dtaglib=enabled \
	-Dtests=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS MAINTAINERS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/gcmd-block
%attr(755,root,root) %{_bindir}/gnome-commander
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/libfilerollerplugin.so
%{_libdir}/%{name}/plugins/file-roller*.xpm
%attr(755,root,root) %{_libdir}/%{name}/plugins/libtestplugin.so
%{_libdir}/%{name}/plugins/test-plugin.xpm
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander.gschema.xml
%{_datadir}/metainfo/org.gnome.gnome-commander.appdata.xml
%{_desktopdir}/org.gnome.gnome-commander.desktop
%{_iconsdir}/hicolor/scalable/apps/gnome-commander.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-commander-internal-viewer.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-commander-symbolic.svg
%{_pixmapsdir}/gnome-commander
%{_mandir}/man1/gnome-commander.1*
