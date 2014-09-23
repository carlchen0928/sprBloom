sprBloom
========

##Scalable Bloom Filter with Redis
根据[python redis bloom filter](https://github.com/seomoz/pyreBloom)改写，在基础上实现了scalable的功能，同时也提供原来的非scalable的pyreBloom功能，使用redis中string作为存储，hash函数使用c语言编写，cython做了一层包装，效率比完全python写提高3-5倍。


#Installation
You will need `hiredis` installed, and a C compiler. You also need `Cython` installed, which will generate C code for `.pyx` file. Than install with command:
```bash
```

##Hiredis
```bash
git clone https://github.com/redis/hiredis
cd hiredis && make && sudo make install
sudo ldconfig
```
