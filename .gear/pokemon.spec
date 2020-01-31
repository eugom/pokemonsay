Name: pokemonsay
Version: 1.0.0
Release: alt1

Summary: Spec file for pokemonsay
Summary(ru_RU.UTF-8): Спек-файл для pokemonsay

License: MIT
Group: Other
Url: https://github.com/possatti/pokemonsay

Source: %name-%version.tar
#Patch0: %name-1.0-alt-makefile-fixes.patch

%description
This specfile is provided as sample specfile for packages with programs.
It contains most of usual tags and constructions used in such specfiles.

%description -l ru_RU.UTF-8
Этот спек-файл является примером спек-файла для пакета с программой. Он содержит
основные теги и конструкции, используемые в подобных спек-файлах.

%prep
%setup
sed -i 's@install_path=.*@install_path="%buildroot/usr/share/%name"@' ./install.sh
sed -i 's@bin_path=.*@bin_path="%buildroot/usr/bin/%name"@' ./install.sh

#patch0 -p1

%build

%install
#cp file %buildroot/etc
./install.sh

%files
%doc LICENSE
/usr/share/%name/
/usr/bin/%name/

#%_bindir/*
#%_man1dir/*

%changelog
* Thu Jan 30 2020 Eugene Omelyanovich <regatio@etersoft.ru> 1.0.0-alt1
- Initial build

