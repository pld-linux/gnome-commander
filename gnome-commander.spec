Summary:	A GNOME filemanager similar to the Midnight Commander
Summary(pl.UTF-8):	Zarządca plików dla środowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	1.2.8.15
Release:	8
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-commander/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	da2f36851f96bc9b2ea7ea363875efed
Patch0:		%{name}-flags.patch
Patch1:		%{name}-1.2.8.15-poppler024.patch
Patch2:		%{name}-gcc47.patch
Patch3:		%{name}-format-security.patch
Patch4:		%{name}-am.patch
Patch5:		%{name}-const-cast.patch
Patch6:		%{name}-gsf.patch
URL:		http://www.nongnu.org/gcmd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	chmlib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exiv2-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.31
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	poppler-devel
BuildRequires:	python-devel
BuildRequires:	taglib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/{plugins/,}/*.{la,a}

[ -d $RPM_BUILD_ROOT%{_localedir}/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_localedir}/sr@{Latn,latin}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gcmd-block
%attr(755,root,root) %{_bindir}/gnome-commander
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/plugins/*.py*
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so*
%{_pixmapsdir}/*
%{_desktopdir}/gnome-commander.desktop
%{_mandir}/man1/gnome-commander.1*
%{_omf_dest_dir}/%{name}
