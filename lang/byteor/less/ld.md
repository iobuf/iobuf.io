# ld

### Link all object files

> gcc -v -o a.out hello.o

```
[p@thinkpad kiss]$ gcc -v -o a.out hello.o
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/lto-wrapper
Target: x86_64-pc-linux-gnu
Configured with: /build/gcc/src/gcc/configure --prefix=/usr --libdir=/usr/lib --libexecdir=/usr/lib --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=https://bugs.archlinux.org/ --enable-languages=c,c++,ada,fortran,go,lto,objc,obj-c++ --enable-shared --enable-threads=posix --enable-libmpx --with-system-zlib --with-isl --enable-__cxa_atexit --disable-libunwind-exceptions --enable-clocale=gnu --disable-libstdcxx-pch --disable-libssp --enable-gnu-unique-object --enable-linker-build-id --enable-lto --enable-plugin --enable-install-libiberty --with-linker-hash-style=gnu --enable-gnu-indirect-function --disable-multilib --disable-werror --enable-checking=release
Thread model: posix
gcc version 6.1.1 20160602 (GCC)
COMPILER_PATH=/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/:/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/:/usr/lib/gcc/x86_64-pc-linux-gnu/:/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/:/usr/lib/gcc/x86_64-pc-linux-gnu/
LIBRARY_PATH=/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/:/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/../../../../lib/:/lib/../lib/:/usr/lib/../lib/:/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/../../../:/lib/:/usr/lib/
COLLECT_GCC_OPTIONS='-v' '-o' 'a.out' '-mtune=generic' '-march=x86-64'
 /usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/collect2 -plugin /usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/lto-wrapper -plugin-opt=-fresolution=/tmp/ccmuuPo4.res -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s --build-id --eh-frame-hdr --hash-style=gnu -m elf_x86_64 -dynamic-linker /lib64/ld-linux-x86-64.so.2 -o a.out /usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/../../../../lib/crt1.o /usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/../../../../lib/crti.o /usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/crtbegin.o -L/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1 -L/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/../../../../lib -L/lib/../lib -L/usr/lib/../lib -L/usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/../../.. hello.o -lgcc --as-needed -lgcc_s --no-as-needed -lc -lgcc --as-needed -lgcc_s --no-as-needed /usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/crtend.o /usr/lib/gcc/x86_64-pc-linux-gnu/6.1.1/../../../../lib/crtn.o
COLLECT_GCC_OPTIONS='-v' '-o' 'a.out' '-mtune=generic' '-march=x86-64'
```

```
[p@thinkpad kiss]$ ./a.out
Hello, world!
```