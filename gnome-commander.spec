Summary:	A GNOME filemanager similar to the Midnight Commander
Summary(pl.UTF-8):	Zarządca plików dla środowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	1.2.8.17
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-commander/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	9e1fe09fc965f54d706895fecb2b06f4
Patch0:		%{name}-flags.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-gsf.patch
URL:		http://www.nongnu.org/gcmd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	chmlib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exiv2-devel >= 0.14
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libgsf-devel >= 1.12.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	poppler-devel >= 0.6
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	exiv2 >= 0.14
Requires:	glib2 >= 1:2.6.0
Requires:	gtk+2 >= 2:2.8.0
Requires:	libgsf >= 1.12.0
Requires:	taglib >= 1.4
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
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

%{__mv} $RPM_BUILD_ROOT%{_localedir}/sr@{Latn,latin}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gcmd-block
%attr(755,root,root) %{_bindir}/gnome-commander
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/plugins/*.py*
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so*
%{_pixmapsdir}/gnome-commander.png
%{_pixmapsdir}/gnome-commander
%{_desktopdir}/gnome-commander.desktop
%{_mandir}/man1/gnome-commander.1*
%{_omf_dest_dir}/%{name}
