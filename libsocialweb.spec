%define	major 0
%define	client_major 2
%define	gir_major 0.25
%define	libname %mklibname socialweb %{major}
%define	libclient %mklibname socialweb-client %{client_major}
%define	girclient %mklibname socialweb-client-gir %{gir_major}
%define	develname %mklibname socialweb -d

Name:		libsocialweb
Version:	0.25.20
Release:	2
License:	LGPLv2.1
Summary:	A personal social data server
Group:		System/Libraries
Url:		http://git.gnome.org/browse/libsocialweb/
Source0:	http://download.gnome.org/sources/libsocialweb/0.25/%{name}-%{version}.tar.xz

BuildRequires:  intltool
BuildRequires:  vala
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnm-glib)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(rest-extras-0.7)

%description
Libsocialweb is a personal social data server, that can interact with
social web services, like Flickr, Last.fm, Twitter and Vimeo.

%package -n %{libname}
Summary:        A personal social data server -- Library for Services
License:        LGPLv2.1
Group:          System/Libraries

%description -n %{libname}
This package contains libraries used by libsocialweb services.

%package -n %{libclient}
Summary:        A personal social data server -- Client Library
License:        LGPLv2.1
Group:          System/Libraries

%description -n %{libclient}
This package contains libraries used by clients willing to use
libsocialweb features.

%package -n %{girclient}
Summary:    GObject Introspection interface description for %{name}-client
Group:      System/Libraries
Requires:   %{libclient} = %{version}-%{release}

%description -n %{girclient}
GObject Introspection interface description for %{name}-client.

%package -n %{develname}
Summary:        A personal social data server -- Development Files
License:        LGPLv2.1
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Requires:       %{libclient} = %{version}-%{release}

%description -n %{develname}
Libsocialweb is a personal social data server, that can interact with
social web services, like Flickr, Last.fm, Twitter and Vimeo.

%prep
%setup -q

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
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
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
%{_libdir}/libsocialweb-keyfob.so.%{major}*
%{_libdir}/libsocialweb-keystore.so.%{major}*

%files -n %{libclient}
%{_libdir}/libsocialweb-client.so.%{client_major}*

%files -n %{girclient}
%{_libdir}/girepository-1.0/SocialWebClient-0.25.typelib

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/libsocialweb/
%{_libdir}/pkgconfig/libsocialweb-client.pc
%{_libdir}/pkgconfig/libsocialweb-keyfob.pc
%{_libdir}/pkgconfig/libsocialweb-keystore.pc
%{_libdir}/pkgconfig/libsocialweb-module.pc
%{_datadir}/gir-1.0/SocialWebClient-0.25.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi
%doc %{_datadir}/gtk-doc/html/libsocialweb/
%doc %{_datadir}/gtk-doc/html/libsocialweb-dbus/
%doc %{_datadir}/gtk-doc/html/libsocialweb-client/
