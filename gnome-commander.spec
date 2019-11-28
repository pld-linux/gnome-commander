Summary:	A GNOME filemanager similar to the Midnight Commander
Summary(pl.UTF-8):	Zarządca plików dla środowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	1.10.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-commander/1.10/%{name}-%{version}.tar.xz
# Source0-md5:	e1ce66c5e64972943fcb51a3a9a74731
Patch0:		%{name}-flags.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-gsf.patch
URL:		https://gcmd.github.io/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	chmlib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exiv2-devel >= 0.14
BuildRequires:	flex
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnome-keyring-devel >= 2.22
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libgsf-devel >= 1.14.26
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	libunique-devel >= 0.9.3
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	poppler-devel >= 0.18
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.44.0
Requires:	exiv2-libs >= 0.14
Requires:	glib2 >= 1:2.44.0
Requires:	gtk+2 >= 2:2.18.0
Requires:	libgnome-keyring >= 2.22
Requires:	libgnomeui >= 2.4.0
Requires:	libgsf >= 1.14.26
Requires:	libunique >= 0.9.3
Requires:	poppler >= 0.18
Requires:	taglib >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# symbol main_win_widget is provided by gnome-commander binary
%define		skip_post_check_so	libgcmd.so.*

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
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-scrollkeeper \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/{plugins/,}*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas

%postun
/sbin/ldconfig
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gcmd-block
%attr(755,root,root) %{_bindir}/gnome-commander
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/libgcmd.so*
%attr(755,root,root) %{_libdir}/%{name}/plugins/libfileroller.so
%{_datadir}/appdata/gnome-commander.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander.gschema.xml
%{_datadir}/gnome-commander
%{_desktopdir}/gnome-commander.desktop
%{_pixmapsdir}/gnome-commander.svg
%{_pixmapsdir}/gnome-commander
%{_mandir}/man1/gnome-commander.1*
