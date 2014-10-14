Summary:	Simple DirectMedia Layer - Sample Mixer Library
Name:		SDL_mixer
Version:	1.2.12
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_mixer/release/%{name}-%{version}.tar.gz
# Source0-md5:	e03ff73d77a55e3572ad0217131dc4a1
Patch0:		double-free-crash.patch
URL:		http://www.libsdl.org/projects/SDL_mixer/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	smpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%package devel
Summary:	Header files and more to develop SDL_mixer applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and more to develop SDL_mixer applications.

%prep
%setup -q
%patch0 -p1

%{__sed} -i "s|AC_CONFIG_AUX_DIRS.*||" configure.in

%build
cp /usr/share/automake/mkinstalldirs .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install install-bin \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/playmus
%attr(755,root,root) %{_bindir}/playwave
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/SDL/*
%{_pkgconfigdir}/*.pc

