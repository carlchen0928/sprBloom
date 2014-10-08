sprBloom
========

#Scalable Bloom Filter with Redis
根据[python redis bloom filter](https://github.com/seomoz/pyreBloom)改写，
在基础上实现了scalable的功能，同时也提供原来的非scalable的pyreBloom功能，
使用redis中string作为存储，hash函数使用c语言编写，cython做了一层包装，效
率比完全python写提高3-5倍。


#Installation
You will need `hiredis` installed, and a C compiler. You also need `Cython` 
installed, which will generate C code for `.pyx` file. Than install with 
command:
```bash
pip install -r requirements.txt
sudo python setup.py install
```

##Redis
```bash
git clone https://github.com/antirez/redis
cd redis && make && sudo make install
```

##Cython
```bash
# On Ubuntu
sudo apt-get install cython
```

##Hiredis
```bash
git clone https://github.com/redis/hiredis
cd hiredis && make && sudo make install
sudo ldconfig
```

#Usage
###create a bloom filter
```python
from sprBloom import sprBloom
f = sprBloom('myfilter', capacity=100000, 
              err_rate=0.001, sprBloom.SMALL_SET_GROWTH,
              host='127.0.0.1', port=6379,
              password='')
```
`SMALL_SET_GROWTH` means capacity increase by double.
`LARGE_SET_GROWTH` means capacity increase by fourth times.
`capacity` means initial capacity, **I suggest you specify it not too small**, you can't all rely on self increase.
`err_rate` means bloom filter error rate, when capacity increase, **it guarantee that error rate will not increase**.
`host` is redis host address.

###add item
```python
f.add(key)                  #if key already in bloom filter, will return True, else will return False
```

###get bloom filter property
```python
print f.capacitt
print f.count
print len(f)
```

###test key in bloom filter
```python
print key in f              #will print True or False
```
