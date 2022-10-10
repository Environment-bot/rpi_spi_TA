# daemon

Daemon is background running thread which does not care is the main thread alaive or not and keeps running even after main thread is terminated.

daemon threads can be asked from object thread via <b>thread.daemon</b> expression. it returns true or false regardin is the thread daemon

daemon can be created with threads by configuring thread at creation stage or via daemon parameter

```python
# create a daemon thread
thread = Thread(daemon=True)
# configure the thread to be a daemon
thread.daemon = True
```

# ident thread ID

thread has it unique identifier in python called ident. it can be accessed via <b>thread.ident</b> 

thread has it unique identifier in OS called native_id. it can be accessed via <b>thread.native_id</b> 

## current thread ID

Here is explaned spels for getting current threads id in python space and os space.

```python
#get os level process id of current thread
id = get_native_id()
#get python process level id of current thread
id = get_ident()
```

# Thread naming

each thread has to have unique name and this can be assigned by creator of the thread. 
Following parameter is needed to be added to thread object when it is created or via name parameter of the object

```python
thread = Thread(name='MyThread')
thread.name = "threadName"
```

## search all active thread
We can get a list of all active threads within a Python process.
This can be achieved via the threading.enumerate() function.

```python
# enumerate all active threads
import threading
# get a list of all active threads
threads = threading.enumerate()
# report the name of all active threads
for thread in threads:
    print(thread.name)
```


# thread count

We can discover the number of active threads in a Python process via following spell.

```python
# report the number of active threads
from threading import active_count
# get the number of active threads
count = active_count()
# report the number of active threads
print(count)
```


# Exceptions

if there in thread occures exception that needs to be handled. Normally if in thread is risen exception it does not affect to main thread which continues excecution.

## Exception hook

exception hooks are created for handling exceptions in threads which handles the exception which is risen at other thread. This way error can be handled proprietly.

```python
# custom exception hook
def custom_hook(args):
    # report the failure
    print(f'Thread failed: {args.exc_value}')

# set the exception hook
threading.excepthook = custom_hook
```

# Thread usecases

When ever there is blocking or repetable code excecuted in the mainthread threre could be used threas which spins load to othre thread to be handled in mean while.

# Data

## Thread-local data

Threads can store local data via an instance of the threading.local class. there needs to be created 