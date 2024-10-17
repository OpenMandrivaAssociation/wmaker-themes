%define	name	wmaker-themes
%define	version	0.1
%define	release	%mkrel 7
%define	summary	Windowmaker Desktop Themes
%define path    /usr/X11R6/share

Summary:	%{summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphical desktop/Other
URL:		https://www.windowmaker.org
Source0:	http://download.freshmeat.net/themes/wall/wall-0.52.tar.gz   
Source1:	http://download.freshmeat.net/themes/galaxy__/galaxy__-0.60.0.tar.gz
Source2:	http://download.freshmeat.net/themes/3dlines/3dlines-0.60.0.tar.gz 
Source3:	http://themes.freshmeat.net/redir/afeelingofrain/39187/url_tgz/afeelingofrain-default.tar.gz
Source4:	http://themes.freshmeat.net/redir/abyssofred/38909/url_tgz/abyssofred-default.tar.gz
Source5:	http://themes.freshmeat.net/redir/fandust/29110/url_tgz/fandust-default.tar.gz
Source6:	http://download.freshmeat.net/themes/casyopeia/casyopeia-0.60.0.tar.gz
Source7:	http://themes.freshmeat.net/redir/giraffe/37586/url_tgz/giraffe-default-0.2.tar.gz
Source8:	http://themes.freshmeat.net/redir/glenwood/35184/url_tgz/Glenwood-default.tar.gz
Source9:	http://themes.freshmeat.net/redir/gnulisten/35292/url_tgz/gnulisten-default-1.0.tar.gz
Source10:	http://themes.freshmeat.net/redir/huangshan_wm_theme/39070/url_tgz/huangshan_wm_theme-default-0.1.tar.gz
Source11:	http://themes.freshmeat.net/redir/killall/30834/url_tgz/killall-default-0.1.tar.gz
Source12:	http://themes.freshmeat.net/redir/mercurysplat/37866/url_tgz/mercurysplat-default.tar.gz
Source13:	http://themes.freshmeat.net/redir/advisorylinux/30090/url_tgz/advisorylinux-1.0.tar.gz
Source14:	http://themes.freshmeat.net/redir/raingutter/36887/url_tgz/raingutter-default-1.0.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	WindowMaker

%description
Additional themes for the Windowmaker desktop and background images.

%prep
%setup -q -c -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a13 -a14 

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{path}/WindowMaker/Themes
cp -a * $RPM_BUILD_ROOT%{path}/WindowMaker/Themes
#Just to shut up rpmlint
cat > README << EOF
%{summary}
EOF

# remove .xvpics
rm -rf $RPM_BUILD_ROOT%{path}/WindowMaker/Themes/KillAll.themed/.xvpics

# fix permissions
find $RPM_BUILD_ROOT%{path} -type f -exec chmod 644 {} \;
find $RPM_BUILD_ROOT%{path} -type d -exec chmod 755 {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{path}/WindowMaker/Themes*

