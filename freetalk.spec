Summary:	Console based Jabber client
Summary(pl.UTF-8):	Konsolowy klient Jabbera
Name:		freetalk
Version:	4.2
Release:	1
License:	GPL v3+
Group:		Applications/Communications
Source0:	https://ftp.gnu.org/gnu/freetalk/%{name}-%{version}.tar.gz
# Source0-md5:	98067ffdbcda9ec7f765fae4b7b23f79
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/freetalk/
BuildRequires:	glib2-devel >= 2.0
# supported: 2.0, 2.2, 3.0
BuildRequires:	guile-devel >= 2.0
BuildRequires:	loudmouth-devel >= 1.0
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freetalk is a console based Jabber client. It features a readline
interface with completion of buddy names, commands, and even ordinary
English words! Freetalk is extensible, configurable, and scriptable
through a Guile interface.

%description -l pl.UTF-8
Freetalk to konsolowy klient Jabbera. Ma interfejs readline z
dopełnianiem imion rozmówców, poleceń, a nawet zwykłych słów
angielskich. Freetalk jest rozszerzalny, konfigurowalny i skryptowalny
poprzez interfejs Guile.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/freetalk
%{_datadir}/freetalk
%{_docdir}/freetalk
%{_infodir}/freetalk.info*
%{_mandir}/man1/freetalk.1*
