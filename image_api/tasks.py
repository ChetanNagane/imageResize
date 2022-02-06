from django_rq import job



@job('high')
def long_running_func():
    print("hiii")
    pass