Summary:	A Gnome filemanager similar to the Norton Commander(TM)
Summary(pl):	Menad¿er plików dla GNOME podobny do Norton Commandera(TM)
Name:		gnome-commander
Version:	0.9.7
Release:	1
License:	GPL
Group:		X11/Applications/File
# Source URL to check...
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/gnome-commander/%{name}-%{version}.tar.gz
URL:		http://gnome-commander.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard fileoperations and some extra features like ftp
support.

%description -l pl
Gnome Commander to menad¿er plików, który podobnie do klasycznego
Norton Commandera(TM), pozwala zrobiæ wszystko z klawiatury. Mo¿e
wykonywaæ wszystkie standardowe operacje na plikach oraz kilka innych
czynno¶ci, jak obs³uga ftp.

%prep
%setup -q

%build
./autogen.sh
%configure
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir}/gnome-commander,%{_applnkdir}/Applications}

install src/gnome-commander $RPM_BUILD_ROOT%{_bindir}/gnome-commander

install gnome-commander.desktop $RPM_BUILD_ROOT%{_applnkdir}/Applications/gnome-commander.desktop

cd pixmaps
install 32_gnome-cmd.png cvs_fish_small.xpm cvs_fish.xpm exec.xpm \
	file_type_block_device_big.xpm file_type_block_device.xpm \
	file_type_char_device_big.xpm file_type_char_device.xpm file_type_dir_big.xpm \
	file_type_dir.xpm file_type_exe_big.xpm file_type_fifo_big.xpm \
	file_type_fifo.xpm file_type_regular_big.xpm file_type_regular.xpm \
	file_type_socket_big.xpm file_type_socket.xpm file_type_sym_block_device.xpm \
	file_type_sym_char_device.xpm file_type_sym_dir.xpm file_type_sym_fifo.xpm \
	file_type_sym_regular.xpm file_type_sym_socket.xpm ftp.xpm  \
	gnome_cmd_arrow_blank.xpm gnome_cmd_arrow_down.xpm gnome_cmd_arrow_up.xpm \
	gnome-cmd.png gnome-cmd.xpm key.xpm lock.xpm logo.png menu_cvs_add.xpm \
	menu_cvs_checkout.xpm menu_cvs_commit_all.xpm menu_cvs_commit.xpm \
	menu_cvs_diff.xpm menu_cvs_import.xpm menu_cvs_login.xpm menu_cvs_logout.xpm \
	menu_cvs_log.xpm menu_cvs_remove.xpm menu_cvs_update.xpm menu_ftp_connect.xpm \
	menu_ftp_disconnect.xpm mkdir.xpm server.xpm \
	$RPM_BUILD_ROOT%{_pixmapsdir}/gnome-commander

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO COPYING ChangeLog
%attr(755,root,root) %{_bindir}/gnome-commander
%{_applnkdir}/Applications/gnome-commander.desktop
%{_pixmapsdir}/gnome-commander
