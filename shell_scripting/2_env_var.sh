

echo $PATH

# PATH will have all executables path, like /bin,usr/sbin, /sbin. If PATH is not configured properly, ls, cat commands
# will not be executed, since executable path is not configured properly. Then use /bin/ls, /bin/ps

/bin/ls

# If PATH=$PATH:/abs_path/until/this/folder            # Files under this folder will be executed any where.
# > 2_env_var.sh     # This file will execute under any dir since Path is added to PATH variable.
