Summary:      A Gnome filemanager similar to the Norton Commander(TM) 
Name:         gnome-commander
Version:      0.9.7
Release:      1
URL: 	      http://gnome-commander.sourceforge.net
Source0:      %{name}-%{version}.tar.gz
License:      GPL
Group:        Applications/File
BuildRoot:    %{_tmppath}/%{name}-root

Distribution: Any

%description
Gnome Commander is a filemanager that just like the classical Norton commander (TM) lets you do everything with the keyboard. It can perform all standard fileoperations and some extra features like ftp support.
%prep
%setup -q

%build
./autogen.sh
./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander
mkdir -p $RPM_BUILD_ROOT/usr/share/gnome/apps/Applications
install -s -m 755 src/gnome-commander $RPM_BUILD_ROOT/usr/bin/gnome-commander
install -m 644 gnome-commander.desktop $RPM_BUILD_ROOT/usr/share/gnome/apps/Applications/gnome-commander.desktop 
install -m 644 pixmaps/32_gnome-cmd.png $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/32_gnome-cmd.png
install -m 644 pixmaps/cvs_fish_small.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/cvs_fish_small.xpm
install -m 644 pixmaps/cvs_fish.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/cvs_fish.xpm
install -m 644 pixmaps/exec.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/exec.xpm
install -m 644 pixmaps/file_type_block_device_big.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_block_device_big.xpm
install -m 644 pixmaps/file_type_block_device.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_block_device.xpm
install -m 644 pixmaps/file_type_char_device_big.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_char_device_big.xpm
install -m 644 pixmaps/file_type_char_device.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_char_device.xpm
install -m 644 pixmaps/file_type_dir_big.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_dir_big.xpm
install -m 644 pixmaps/file_type_dir.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_dir.xpm
install -m 644 pixmaps/file_type_exe_big.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_exe_big.xpm
install -m 644 pixmaps/file_type_fifo_big.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_fifo_big.xpm
install -m 644 pixmaps/file_type_fifo.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_fifo.xpm
install -m 644 pixmaps/file_type_regular_big.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_regular_big.xpm
install -m 644 pixmaps/file_type_regular.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_regular.xpm
install -m 644 pixmaps/file_type_socket_big.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_socket_big.xpm
install -m 644 pixmaps/file_type_socket.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_socket.xpm
install -m 644 pixmaps/file_type_sym_block_device.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_sym_block_device.xpm
install -m 644 pixmaps/file_type_sym_char_device.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_sym_char_device.xpm
install -m 644 pixmaps/file_type_sym_dir.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_sym_dir.xpm
install -m 644 pixmaps/file_type_sym_fifo.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_sym_fifo.xpm
install -m 644 pixmaps/file_type_sym_regular.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_sym_regular.xpm
install -m 644 pixmaps/file_type_sym_socket.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/file_type_sym_socket.xpm
install -m 644 pixmaps/ftp.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/ftp.xpm
install -m 644 pixmaps/gnome_cmd_arrow_blank.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/gnome_cmd_arrow_blank.xpm
install -m 644 pixmaps/gnome_cmd_arrow_down.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/gnome_cmd_arrow_down.xpm
install -m 644 pixmaps/gnome_cmd_arrow_up.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/gnome_cmd_arrow_up.xpm
install -m 644 pixmaps/gnome-cmd.png $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/gnome-cmd.png
install -m 644 pixmaps/gnome-cmd.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/gnome-cmd.xpm
install -m 644 pixmaps/key.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/key.xpm
install -m 644 pixmaps/lock.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/lock.xpm
install -m 644 pixmaps/logo.png $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/logo.png
install -m 644 pixmaps/menu_cvs_add.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_add.xpm
install -m 644 pixmaps/menu_cvs_checkout.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_checkout.xpm
install -m 644 pixmaps/menu_cvs_commit_all.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_commit_all.xpm
install -m 644 pixmaps/menu_cvs_commit.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_commit.xpm
install -m 644 pixmaps/menu_cvs_diff.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_diff.xpm
install -m 644 pixmaps/menu_cvs_import.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_import.xpm
install -m 644 pixmaps/menu_cvs_login.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_login.xpm
install -m 644 pixmaps/menu_cvs_logout.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_logout.xpm
install -m 644 pixmaps/menu_cvs_log.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_log.xpm
install -m 644 pixmaps/menu_cvs_remove.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_remove.xpm
install -m 644 pixmaps/menu_cvs_update.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_cvs_update.xpm
install -m 644 pixmaps/menu_ftp_connect.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_ftp_connect.xpm
install -m 644 pixmaps/menu_ftp_disconnect.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/menu_ftp_disconnect.xpm
install -m 644 pixmaps/mkdir.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/mkdir.xpm
install -m 644 pixmaps/server.xpm $RPM_BUILD_ROOT/usr/share/pixmaps/gnome-commander/server.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO COPYING ChangeLog
/usr/bin/gnome-commander
/usr/share/gnome/apps/Applications/gnome-commander.desktop
/usr/share/pixmaps/gnome-commander/32_gnome-cmd.png
/usr/share/pixmaps/gnome-commander/cvs_fish_small.xpm
/usr/share/pixmaps/gnome-commander/cvs_fish.xpm
/usr/share/pixmaps/gnome-commander/exec.xpm
/usr/share/pixmaps/gnome-commander/file_type_block_device_big.xpm
/usr/share/pixmaps/gnome-commander/file_type_block_device.xpm
/usr/share/pixmaps/gnome-commander/file_type_char_device_big.xpm
/usr/share/pixmaps/gnome-commander/file_type_char_device.xpm
/usr/share/pixmaps/gnome-commander/file_type_dir_big.xpm
/usr/share/pixmaps/gnome-commander/file_type_dir.xpm
/usr/share/pixmaps/gnome-commander/file_type_exe_big.xpm
/usr/share/pixmaps/gnome-commander/file_type_fifo_big.xpm
/usr/share/pixmaps/gnome-commander/file_type_fifo.xpm
/usr/share/pixmaps/gnome-commander/file_type_regular_big.xpm
/usr/share/pixmaps/gnome-commander/file_type_regular.xpm
/usr/share/pixmaps/gnome-commander/file_type_socket_big.xpm
/usr/share/pixmaps/gnome-commander/file_type_socket.xpm
/usr/share/pixmaps/gnome-commander/file_type_sym_block_device.xpm
/usr/share/pixmaps/gnome-commander/file_type_sym_char_device.xpm
/usr/share/pixmaps/gnome-commander/file_type_sym_dir.xpm
/usr/share/pixmaps/gnome-commander/file_type_sym_fifo.xpm
/usr/share/pixmaps/gnome-commander/file_type_sym_regular.xpm
/usr/share/pixmaps/gnome-commander/file_type_sym_socket.xpm
/usr/share/pixmaps/gnome-commander/ftp.xpm
/usr/share/pixmaps/gnome-commander/gnome_cmd_arrow_blank.xpm
/usr/share/pixmaps/gnome-commander/gnome_cmd_arrow_down.xpm
/usr/share/pixmaps/gnome-commander/gnome_cmd_arrow_up.xpm
/usr/share/pixmaps/gnome-commander/gnome-cmd.png
/usr/share/pixmaps/gnome-commander/gnome-cmd.xpm
/usr/share/pixmaps/gnome-commander/key.xpm
/usr/share/pixmaps/gnome-commander/lock.xpm
/usr/share/pixmaps/gnome-commander/logo.png
/usr/share/pixmaps/gnome-commander/menu_cvs_add.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_checkout.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_commit_all.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_commit.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_diff.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_import.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_login.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_logout.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_log.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_remove.xpm
/usr/share/pixmaps/gnome-commander/menu_cvs_update.xpm
/usr/share/pixmaps/gnome-commander/menu_ftp_connect.xpm
/usr/share/pixmaps/gnome-commander/menu_ftp_disconnect.xpm
/usr/share/pixmaps/gnome-commander/mkdir.xpm
/usr/share/pixmaps/gnome-commander/server.xpm

%changelog
* Sat Mar  9 2002 Marcus Bjurman <marbj499@student.liu.se>
- Pumped up the version nr

* Sun Nov  4 2001 Marcus Bjurman <marbj499@student.liu.se>
- Initial build.
