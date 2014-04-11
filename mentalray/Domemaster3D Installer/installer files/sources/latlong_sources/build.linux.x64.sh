#!/bin/bash
# Mental Ray Shader Compile Script

gcc -c -O3 -fPIC -Bsymbolic -DBIT64 -I/usr/local/mi/ray-3.8.1.28/include ./latlong_lens.cpp
ld -export-dynamic -shared -o latlong_lens.so latlong_lens.o