
HOSTNAME=$(hostname)
CRITICAL=98     # greater than 98%
WARNING=90      # greater than 90%
CRITICALEMAIL="manageremail@domain.com"
WARNINGEMAIL="myemail@domain.com"
mkdir -p ./cpulist
LOGFILE=./cpulist/cpusage-`date +%h%d%y`.log

touch $LOGFILE
PATHS="/"

FOR path in $PATHS
do
CPULOAD=`top -b -n 2 -d1 | grep "Cpu(s)" | tail -n1 | awk '{print $2}' | awk -F. '{print $1}'`

if [ -n $WARING -a -n $CRITICAL ]  # if warning and critical are numbers.
then
if [ "$CPULOAD" -ge "$WARNING" -A  "$CPULOAD" -lt "$CRITICAL"]
then
echo "`date "+%F %H:%M:%S"` warning - $CPULOAD on host $HOSTNAME" >> $LOGFILE
echo "Warning Cpuload $CPULOAD Host is $HOSTNAME" | mail -s "CPULOAD is waning" $WARNINGEMAIL
exit 1
elif [ "$CPULOAD" -ge "$CRITICAL" ]
then
echo "`date "+%F %H:%M:%S"` critical - $CPULOAD on host $HOSTNAME" >> $LOGFILE
echo "Critical Cpuload $CPULOAD Host is $HOSTNAME" | mail -s "CPULOAD is critical" $CRITICALEMAIL
exit 2
else
echo "`date "+%F %H:%M:%S"` OK - $CPULOAD on $HOSTNAME" >> $LOGFILE
exit 0


# In crontab we can keep this file to execute to see cpu usage
#*/5 * * * * sh 14_real_time_cpu_util.sh

