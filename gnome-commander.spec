Summary:	A Gnome filemanager similar to the Midnight Commander
Summary(pl):	Zarz±dca plików dla ¶rodowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	0.9.12
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://savannah.nongnu.org/download/gcmd/gcmd.pkg/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ef0152c3014689ba76c3b67609ec3c69
BuildRequires:	GConf-devel
BuildRequires:	gdk-pixbuf-devel >= 0.8
# glib-gettextize
BuildRequires:	glib2-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gnome-vfs-devel
URL:		http://savannah.gnu.org/projects/gcmd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Commander is a filemanager that just like the classical Midnight
commander lets you do everything with the keyboard. It can perform all
standard fileoperations and some extra features like ftp support.

%description -l pl
Gnome Commander to zarz±dca plików, który podobnie do klasycznego
Midnight Commandera umo¿liwia pe³n± obs³ugê przy pomocy klawiatury.
Zapewnia wykonanie wszystkich typowych operacji na plikach, a tak¿e
kilka dodatkowych jak np. klienta ftp

%prep
%setup -q

%build
glib-gettextize -c -f
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-fam
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install gnome-commander.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities/gnome-commander.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/%{name}
%{_applnkdir}/Utilities/*
