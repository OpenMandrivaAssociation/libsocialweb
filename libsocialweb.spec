%define url_ver %(echo %{version}|cut -d. -f1,2)

%define	major 0
%define	client_major 2
%define	gimajor 0.25
%define	libname %mklibname socialweb %{major}
%define libkeyfob %mklibname socialweb-keyfob %{major}
%define libkeystore %mklibname socialweb-keystore %{major}
%define	libclient %mklibname socialweb-client %{client_major}
%define	girclient %mklibname socialweb-client-gir %{gimajor}
%define	devname %mklibname socialweb -d

Summary:	A personal social data server
Name:		libsocialweb
Version:	0.25.21
Release:	8
License:	LGPLv2.1
Group:		System/Libraries
Url:		http://git.gnome.org/browse/libsocialweb/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsocialweb/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		libsocialweb-0.25.20-linkage.patch
Patch1:		libsocialweb-0.25.21-strfmt.patch

BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(rest-extras-0.7)

%description
Libsocialweb is a personal social data server, that can interact with
social web services, like Flickr, Last.fm, Twitter and Vimeo.

%package -n %{libname}
Summary:	A personal social data server -- Library for Services
Group:		System/Libraries

%description -n %{libname}
This package contains libraries used by libsocialweb services.

%package -n %{libkeyfob}
Summary:	A personal social data server -- Library for Services
Group:		System/Libraries
Conflicts:	%{_lib}socialweb0 < 0.25.21-2

%description -n %{libkeyfob}
This package contains libraries used by libsocialweb services.

%package -n %{libkeystore}
Summary:	A personal social data server -- Library for Services
Group:		System/Libraries
Conflicts:	%{_lib}socialweb0 < 0.25.21-2

%description -n %{libkeystore}
This package contains libraries used by libsocialweb services.

%package -n %{libclient}
Summary:	A personal social data server -- Client Library
Group:		System/Libraries

%description -n %{libclient}
This package contains libraries used by clients willing to use
libsocialweb features.

%package -n %{girclient}
Summary:	GObject Introspection interface description for %{name}-client
Group:		System/Libraries

%description -n %{girclient}
GObject Introspection interface description for %{name}-client.

%package -n %{devname}
Summary:	A personal social data server -- Development Files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libkeyfob} = %{version}-%{release}
Requires:	%{libkeystore} = %{version}-%{release}
Requires:	%{libclient} = %{version}-%{release}
Requires:	%{girclient} = %{version}-%{release}

%description -n %{devname}
Libsocialweb is a personal social data server, that can interact with
social web services, like Flickr, Last.fm, Twitter and Vimeo.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--with-gnome \
	--with-online=networkmanager \
	--enable-vala-bindings \
	--enable-all-services

%make

%install
%makeinstall_std
%find_lang %{name}

# Create directory where API keys will be stored
mkdir %{buildroot}%{_datadir}/libsocialweb/keys

%files -f %{name}.lang
%doc AUTHORS COPYING README
# dbus core service
%{_libexecdir}/libsocialweb-core
%{_datadir}/dbus-1/services/libsocialweb.service
%dir %{_libdir}/libsocialweb
%dir %{_libdir}/libsocialweb/services
%dir %{_datadir}/libsocialweb
%dir %{_datadir}/libsocialweb/keys
%dir %{_datadir}/libsocialweb/services
# plugins for various web services
# Explicitly list services to make sure we don't lose any
%{_libdir}/libsocialweb/services/libfacebook.so
%{_datadir}/libsocialweb/services/facebook.keys
%{_libdir}/libsocialweb/services/libflickr.so
%{_datadir}/libsocialweb/services/flickr.keys
%{_libdir}/libsocialweb/services/liblastfm.so
%{_datadir}/libsocialweb/services/lastfm.keys
%{_datadir}/libsocialweb/services/lastfm.png
%{_libdir}/libsocialweb/services/libmyspace.so
%{_datadir}/libsocialweb/services/myspace.keys
%{_datadir}/libsocialweb/services/myspace.png
%{_libdir}/libsocialweb/services/libphotobucket.so
%{_datadir}/libsocialweb/services/photobucket.keys
%{_libdir}/libsocialweb/services/libplurk.so
%{_datadir}/libsocialweb/services/plurk.keys
%{_datadir}/libsocialweb/services/plurk.png
%{_libdir}/libsocialweb/services/libsina.so
%{_datadir}/libsocialweb/services/sina.keys
%{_datadir}/libsocialweb/services/sina.png
%{_libdir}/libsocialweb/services/libsmugmug.so
%{_datadir}/libsocialweb/services/smugmug.keys
%{_libdir}/libsocialweb/services/libtwitter.so
%{_datadir}/libsocialweb/services/twitter.keys
%{_datadir}/libsocialweb/services/twitter.png
%{_libdir}/libsocialweb/services/libvimeo.so
%{_datadir}/libsocialweb/services/vimeo.keys
%{_datadir}/libsocialweb/services/vimeo.png
%{_libdir}/libsocialweb/services/libyoutube.so
%{_datadir}/libsocialweb/services/youtube.keys
%{_datadir}/libsocialweb/services/youtube.png

%files -n %{libname}
%{_libdir}/libsocialweb.so.%{major}*

%files -n %{libkeyfob}
%{_libdir}/libsocialweb-keyfob.so.%{major}*

%files -n %{libkeystore}
%{_libdir}/libsocialweb-keystore.so.%{major}*

%files -n %{libclient}
%{_libdir}/libsocialweb-client.so.%{client_major}*

%files -n %{girclient}
%{_libdir}/girepository-1.0/SocialWebClient-%{gimajor}.typelib

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/libsocialweb/
%{_libdir}/pkgconfig/libsocialweb-client.pc
%{_libdir}/pkgconfig/libsocialweb-keyfob.pc
%{_libdir}/pkgconfig/libsocialweb-keystore.pc
%{_libdir}/pkgconfig/libsocialweb-module.pc
%{_datadir}/gir-1.0/SocialWebClient-%{gimajor}.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
%doc %{_datadir}/gtk-doc/html/libsocialweb/
%doc %{_datadir}/gtk-doc/html/libsocialweb-dbus/
%doc %{_datadir}/gtk-doc/html/libsocialweb-client/

