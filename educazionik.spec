# Basic macros
%define name    educazionik 
%define version 2.0.0
%define prerel	beta1

Name:           %{name}
Version:        %{version}
Summary:        Italian educational project
Summary(it):    Raccolta di programmi educativi
Release:        %mkrel 0.1
License:        GPLv2+
Group:          Education
URL:            http://sourceforge.net/projects/educazionik/

Source0:        %{name}-%{version}-%{prerel}.tar.bz2

BuildRoot:      %_tmppath/%name-%version-%release-buildroot

BuildRequires: qt4-devel
BuildRequires: cmake

%description
Educazionik is an educational project for (at the moment)
Italian primary school students.

%description -l it
Educazionik è unaraccolta di programmi educativi rivolta
agli studenti delle scuole primarie

%files 
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/apps/%{name}/*
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png


#--------------------------------------------------------------------

%prep
%setup -q  -n %{name}-%{version}-%{prerel}

%build

%cmake
%make


%install
rm -rf %buildroot
cd build
make DESTDIR=%buildroot install
#make CMAKE_INSTALL_PREFIX=%buildroot install
cd ..
install -m644 common/educazionik16x16.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 common/educazionik32x32.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 common/educazionik48x48.png -D %{buildroot}%{_liconsdir}/%{name}.png

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

