
# GPU?

    from tensorflow.python.client import device_lib
    [print(x.name) for x in device_lib.list_local_devices()]


See something like

```
/device:CPU:0
/device:GPU:0
```

