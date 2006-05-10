Summary:	A GNOME filemanager similar to the Midnight Commander
Summary(pl):	Zarz±dca plików dla ¶rodowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-commander/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	2f34596e4c8a927efdb4ab987b82c7f0
Patch0:		%{name}-desktop.patch
URL:		http://www.nongnu.org/gcmd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.31
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Commander is a filemanager that just like the classical Midnight
commander lets you do everything with the keyboard. It can perform all
standard fileoperations and some extra features like FTP support.

%description -l pl
GNOME Commander to zarz±dca plików, który podobnie do klasycznego
Midnight Commandera umo¿liwia pe³n± obs³ugê przy pomocy klawiatury.
Zapewnia wykonanie wszystkich typowych operacji na plikach, a tak¿e
kilka dodatkowych jak np. klienta FTP.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/{plugins/,}/*.{la,a}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*.so*
%{_pixmapsdir}/*
%{_desktopdir}/gnome-commander.desktop
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
