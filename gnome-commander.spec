Summary:	A Gnome filemanager similar to the Midnight Commander
Summary(pl):	Zarz±dca plików dla ¶rodowiska GNOME w stylu Midnight Commandera
Name:		gnome-commander
Version:	0.9.8
Release:	0.1
License:	GPL
Group:		X11/Applications/File
Source0:	http://freesoftware.fsf.org/download/gcmd/gcmd.pkg/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gdk-pixbuf-devel >= 0.8
BuildRequires:  GConf-devel
BuildRequires:  gnome-libs-devel
URL:		http://savannah.gnu.org/projects/gcmd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_applnkdir}/Utilities

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT
install gnome-commander.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Utilities/gnome-commander.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO INSTALL NEWS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/%{name}/*
%attr(0644,root,root) %{_applnkdir}/Utilities/*
