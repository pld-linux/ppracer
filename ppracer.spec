Summary:	Race down mountainous terrain with Tux!
Summary(pl):	Zje¿d¿aj z Tuksem w górzystym terenie!
Summary(pt_BR):	Corra montanha abaixo com o Tux!
Name:		ppracer
Version:	0.2.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.berlios.de/ppracer/%{name}-%{version}.tar.bz2
# Source0-md5:	0cd8e9731191d8c1a359c8d0f86d8f20
Source1:	http://download.berlios.de/ppracer/%{name}-data-%{version}.tar.bz2
# Source1-md5:	a0b3f40b2d875a5578a1605c6b6ecfed
Source2:	%{name}.desktop
Source3:	%{name}.png
URL:		http://racer.planetpenguin.de/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	tcl-devel >= 8.4.3
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
PP Racer lets you take on the role of Tux the Linux Penguin as he
races down steep, snow-covered mountains. Enter cups and compete to
win the title! PP Racer includes a variety of options for gameplay,
including the ability to race courses in fog, at night, and under high
winds.

%description -l pl
PP Racer pozwala wcieliæ siê w rolê Tuksa, linuksowego Pingwina
podczas zjazdu w dó³ pokrytych ¶niegiem gór. We¼ udzia³ w zawodach i
zdob±d¼ tytu³! PP Racer zawiera wiele opcji, miêdzy innymi mo¿liwo¶æ
zje¿d¿ania we mgle, w nocy i podczas silnego wiatru.

%description -l pt_BR
O objetivo do PP Racer é diversão! Corra montanha abaixo tão rápido 
quanto possível e capture peixes para aumentar sua pontuação!

%prep
%setup -q -a1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="%{rpmcflags} -DGLX_GLXEXT_LEGACY"
%configure \
	--with-data-dir=%{_datadir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

mv -f %{name}-data-%{version}/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
