# Port Scanner
A simple Python script to perform port scanning on specified target based on a range of ports.

## Explanation
The `socket` module is what's used to connect to the target and the respective port and determines whether the port is open or not based on trying to establish a connection using the `connect()` function.

The `threading` module is used to optimize the port scan as it allows to create multiple threads using `Thread()` inside a loop to run multiple instances of the scan at once.

The `queue` module is then used to create a queue list of the port range that is to be scanned and pops out the ports that have been scanned so that the different threads only scan ports that have not been scanned yet.

## References
The code has been taken from this [tutorial](https://youtu.be/FGdiSJakIS4?si=FhPUwgaGQ4pqlS75&t=1649).