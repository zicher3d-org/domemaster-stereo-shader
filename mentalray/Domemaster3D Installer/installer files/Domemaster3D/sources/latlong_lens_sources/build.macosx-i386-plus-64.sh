#!/bin/bash
# Compile Script

mkdir -p i386 && ( cd i386
g++ -c -O3 -mtune=pentiumpro -fexpensive-optimizations -fforce-mem -finline-functions -funroll-loops -fomit-frame-pointer -frerun-cse-after-loop -fstrength-reduce -fforce-addr -fPIC -std=c++98 -dynamic -m32 -fno-common -DQMC -DMI_MODULE= -DMI_PRODUCT_RAY -DMACOSX -D_REENTRANT -DEVIL_ENDIAN -DX86 -DHYPERTHREAD -I.. -I../ -I/Applications/Autodesk/maya2011/devkit/mentalray/include/ ../latlong_lens.cpp
g++ -flat_namespace -m32 -DX86 -undefined suppress -dynamiclib -o latlong_lens.dylib latlong_lens.o
)

mkdir -p i386x64 && ( cd i386x64
g++-4.0 -c -O3 -fexpensive-optimizations -finline-functions -funroll-loops -fomit-frame-pointer -frerun-cse-after-loop -fstrength-reduce -fforce-addr -fPIC -std=c++98 -dynamic -fno-common -m64 -DQMC -DMI_MODULE= -DMI_PRODUCT_RAY -DMACOSX -D_REENTRANT -DEVIL_ENDIAN -DX86 -DHYPERTHREAD -DBIT64 -I.. -I../ -I/Applications/Autodesk/maya2011/devkit/mentalray/include/ ../latlong_lens.cpp
g++-4.0 -flat_namespace -m64 -DX86 -undefined suppress -dynamiclib -o latlong_lens.dylib latlong_lens.o
)

mkdir -p i386-plus-64-compiled
lipo -output i386-plus-64-compiled/latlong_lens.dylib -create i386/latlong_lens.dylib i386x64/latlong_lens.dylib
