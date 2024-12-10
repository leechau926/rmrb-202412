
#!/bin/bash

echo "**************************************"

def=$1

# date definition
year=${def:0:4}
month=${def:4:2}
day=${def:6:2}
echo ${year}
echo ${month}
echo ${day}

echo "`date '+%Y-%m-%d %H:%M:%S'` process started."

# download files
# wget -i /home/user/down.txt -P /home/user/rmrb -a /home/user/rmrb/rmrb_down.log
# echo "`date '+%Y-%m-%d %H:%M:%S'` download files completed."

# merge pdf files
pdftk /home/user/rmrb/*.pdf cat output /home/user/rmrb${year}${month}${day}.pdf
echo "`date '+%Y-%m-%d %H:%M:%S'` merge files completed."


# rm files
rm /home/user/rmrb/*.pdf
echo "`date '+%Y-%m-%d %H:%M:%S'` delete files completed."

