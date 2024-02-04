# encoding: utf-8
# module gevent.libev._corecffi.lib
# from /home/kadosh/.local/lib/python3.10/site-packages/gevent/libev/_corecffi.abi3.so
# by generator 1.147
# no doc

# imports
from _cffi_backend import (_syserr_cb, gevent_noop, python_callback, 
    python_check_callback, python_handle_error, python_prepare_callback, 
    python_stop)


# Variables with simple values

EVBACKEND_ALL = 255
EVBACKEND_DEVPOLL = 16
EVBACKEND_EPOLL = 4
EVBACKEND_IOURING = 128
EVBACKEND_KQUEUE = 8
EVBACKEND_LINUXAIO = 64
EVBACKEND_MASK = 65535
EVBACKEND_POLL = 2
EVBACKEND_PORT = 32
EVBACKEND_SELECT = 1

EVBREAK_ALL = 2
EVBREAK_CANCEL = 0
EVBREAK_ONE = 1

EVFLAG_AUTO = 0
EVFLAG_FORKCHECK = 33554432
EVFLAG_NOENV = 16777216
EVFLAG_NOINOTIFY = 1048576
EVFLAG_NOSIGMASK = 4194304
EVFLAG_SIGNALFD = 2097152

EVRUN_NOWAIT = 1
EVRUN_ONCE = 2

EV_ASYNC = 524288
EV_CHECK = 32768
EV_CHILD = 2048
EV_CLEANUP = 262144
EV_CUSTOM = 16777216
EV_EMBED = 65536
EV_ERROR = -2147483648
EV_FORK = 131072
EV_IDLE = 8192
EV_MAXPRI = 2
EV_MINPRI = -2
EV_NONE = 0
EV_PERIODIC = 512
EV_PREPARE = 16384
EV_READ = 1
EV_SIGNAL = 1024
EV_STAT = 4096
EV_TIMER = 256
EV_UNDEF = -1

EV_VERSION_MAJOR = 4
EV_VERSION_MINOR = 33

EV_WRITE = 2

EV__IOFDSET = 128

LIBEV_EMBED = 1

# functions

def ev_async_init(struct_ev_async, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_async_init(struct ev_async *, void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_async_pending(struct_ev_async, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ev_async_pending(struct ev_async *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_async_send(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_async_send(struct ev_loop *, struct ev_async *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_async_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_async_start(struct ev_loop *, struct ev_async *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_async_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_async_stop(struct ev_loop *, struct ev_async *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_backend(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned int ev_backend(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_break(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_break(struct ev_loop *, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_check_init(struct_ev_check, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_check_init(struct ev_check *, void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_check_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_check_start(struct ev_loop *, struct ev_check *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_check_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_check_stop(struct ev_loop *, struct ev_check *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_child_init(struct_ev_child, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_child_init(struct ev_child *, void *, int, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_child_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_child_start(struct ev_loop *, struct ev_child *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_child_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_child_stop(struct ev_loop *, struct ev_child *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_default_loop(unsigned_int): # real signature unknown; restored from __doc__
    """
    struct ev_loop *ev_default_loop(unsigned int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_depth(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned int ev_depth(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_embeddable_backends(): # real signature unknown; restored from __doc__
    """
    unsigned int ev_embeddable_backends();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    return 0

def ev_feed_event(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_feed_event(struct ev_loop *, void *, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_feed_fd_event(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_feed_fd_event(struct ev_loop *, int, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_fork_init(struct_ev_fork, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_fork_init(struct ev_fork *, void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_fork_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_fork_start(struct ev_loop *, struct ev_fork *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_fork_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_fork_stop(struct ev_loop *, struct ev_fork *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_idle_init(struct_ev_idle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_idle_init(struct ev_idle *, void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_idle_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_idle_start(struct ev_loop *, struct ev_idle *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_idle_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_idle_stop(struct ev_loop *, struct ev_idle *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_io_init(struct_ev_io, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_io_init(struct ev_io *, void *, int, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_io_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_io_start(struct ev_loop *, struct ev_io *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_io_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_io_stop(struct ev_loop *, struct ev_io *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_is_active(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ev_is_active(void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_is_default_loop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ev_is_default_loop(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_is_pending(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ev_is_pending(void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_iteration(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned int ev_iteration(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_loop_destroy(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_loop_destroy(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_loop_fork(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_loop_fork(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_loop_new(unsigned_int): # real signature unknown; restored from __doc__
    """
    struct ev_loop *ev_loop_new(unsigned int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_now(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    double ev_now(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_now_update(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_now_update(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_pending_count(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unsigned int ev_pending_count(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_prepare_init(struct_ev_prepare, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_prepare_init(struct ev_prepare *, void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_prepare_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_prepare_start(struct ev_loop *, struct ev_prepare *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_prepare_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_prepare_stop(struct ev_loop *, struct ev_prepare *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_priority(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    int ev_priority(void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_recommended_backends(): # real signature unknown; restored from __doc__
    """
    unsigned int ev_recommended_backends();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    return 0

def ev_ref(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_ref(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_run(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_run(struct ev_loop *, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_set_priority(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_set_priority(void *, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_set_syserr_cb(void, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_set_syserr_cb(void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_set_userdata(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_set_userdata(struct ev_loop *, void *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_signal_init(struct_ev_signal, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_signal_init(struct ev_signal *, void *, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_signal_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_signal_start(struct ev_loop *, struct ev_signal *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_signal_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_signal_stop(struct ev_loop *, struct ev_signal *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_sleep(double): # real signature unknown; restored from __doc__
    """
    void ev_sleep(double);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_stat_init(struct_ev_stat, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_stat_init(struct ev_stat *, void *, char *, double);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_stat_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_stat_start(struct ev_loop *, struct ev_stat *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_stat_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_stat_stop(struct ev_loop *, struct ev_stat *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_supported_backends(): # real signature unknown; restored from __doc__
    """
    unsigned int ev_supported_backends();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    return 0

def ev_time(): # real signature unknown; restored from __doc__
    """
    double ev_time();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    return 0.0

def ev_timer_again(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_timer_again(struct ev_loop *, struct ev_timer *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_timer_init(struct_ev_timer, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_timer_init(struct ev_timer *, void *, double, double);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_timer_start(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_timer_start(struct ev_loop *, struct ev_timer *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_timer_stop(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_timer_stop(struct ev_loop *, struct ev_timer *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_unref(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_unref(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_userdata(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void *ev_userdata(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_verify(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void ev_verify(struct ev_loop *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def ev_version_major(): # real signature unknown; restored from __doc__
    """
    int ev_version_major();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    return 0

def ev_version_minor(): # real signature unknown; restored from __doc__
    """
    int ev_version_minor();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    return 0

def gevent_ev_default_loop(unsigned_int): # real signature unknown; restored from __doc__
    """
    struct ev_loop *gevent_ev_default_loop(unsigned int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def gevent_install_sigchld_handler(): # real signature unknown; restored from __doc__
    """
    void gevent_install_sigchld_handler();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def gevent_reset_sigchld_handler(): # real signature unknown; restored from __doc__
    """
    void gevent_reset_sigchld_handler();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def gevent_set_ev_alloc(): # real signature unknown; restored from __doc__
    """
    void gevent_set_ev_alloc();
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def gevent_zero_check(struct_ev_check, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_zero_check(struct ev_check *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def gevent_zero_prepare(struct_ev_prepare, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_zero_prepare(struct ev_prepare *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def gevent_zero_timer(struct_ev_timer, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void gevent_zero_timer(struct ev_timer *);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

def _gevent_generic_callback(struct_ev_loop, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    void _gevent_generic_callback(struct ev_loop *, struct ev_watcher *, int);
    
    CFFI C function from gevent.libev._corecffi.lib
    """
    pass

# no classes
