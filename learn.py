def f(*args, var='/'):
    return var.join(args)
print(f("Yesterday", "Today","Tomorrow"))