Summary:	A GNOME filemanager similar to the Midnight Commander
Summary(pl):	Zarz±dca plików dla ¶rodowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	1.1.6
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.1/%{name}-%{version}.tar.bz2
# Source0-md5:	972e976ea01663f5b60e8a16721a5348
Patch0:		%{name}-clist.patch
URL:		http://www.nongnu.org/gcmd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libgnome-devel
BuildRequires:	libgnomeui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Commander is a filemanager that just like the classical Midnight
commander lets you do everything with the keyboard. It can perform all
standard fileoperations and some extra features like ftp support.

%description -l pl
GNOME Commander to zarz±dca plików, który podobnie do klasycznego
Midnight Commandera umo¿liwia pe³n± obs³ugê przy pomocy klawiatury.
Zapewnia wykonanie wszystkich typowych operacji na plikach, a tak¿e
kilka dodatkowych jak np. klienta ftp

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize -c -f
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/{plugins/,}/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/lib*
%attr(755,root,root) %{_libdir}/%{name}/plugins/lib*
%{_pixmapsdir}/%{name}
%{_desktopdir}/gnome-commander.desktop
