Name: libsocialweb
Version: 0.25.7
Release: %mkrel 1
Summary: A social network data aggregator
Group: Applications/Internet
License: LGPLv2
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/gnome/sources/%{name}/0.25/%{name}-%{version}.tar.bz2
Source1: flickr
Source2: twitter
Source3: lastfm
Source4: twitpic
Requires: %{name}-keys = %{version}-%{release}
BuildRequires: dbus-glib-devel
BuildRequires: glib2-devel
BuildRequires: libGConf2-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: libsoup-devel
BuildRequires: libjson-glib-devel
BuildRequires: libnm-glib-devel
BuildRequires: librest-devel >= 0.7.0
BuildRequires: intltool
Provides: mojito = %{version}

%description
libsocialweb is a social data server which fetches data from the "social web", 
such as your friend's blog posts and photos, upcoming events, recently played 
tracks, and pending eBay* auctions. It also provides a service to update 
your status on web services which support it, such as MySpace* and Twitter*.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Files for development with %{name}.

%package keys
Summary: API keys for %{name}
Group: Applications/Internet
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description keys
Keys allowing access to various web services through libsocialweb.

%prep
%setup -q

chmod 644 examples/*.py 

%build
%configure --with-gnome --with-online=networkmanager --disable-static --enable-all-services

# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives and static libs.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

mkdir -p %{buildroot}/%{_datadir}/libsocialweb/keys
cp %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{buildroot}/%{_datadir}/libsocialweb/keys

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING TODO
%{_libdir}/libsocialweb*.so.*
%{_libdir}/libsocialweb/
%dir %{_datadir}/libsocialweb/
%{_datadir}/libsocialweb/services/
%{_datadir}/dbus-1/services/libsocialweb.service
%{_libexecdir}/libsocialweb-core

%files devel
%defattr(-,root,root,-)
%doc tests/*.c examples/*c examples/*.py
%doc %{_datadir}/gtk-doc/html/libsocialweb
%doc %{_datadir}/gtk-doc/html/libsocialweb-client
%doc %{_datadir}/gtk-doc/html/libsocialweb-dbus
%{_includedir}/libsocialweb
%{_libdir}/pkgconfig/libsocialweb*
%{_libdir}/libsocialweb*so

%files keys
%defattr(-,root,root,-)
%{_datadir}/libsocialweb/keys

