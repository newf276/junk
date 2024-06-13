        sudo apt update
        sudo apt -y install xmltv retry
        go install github.com/aquilax/m3u-combine@latest
        cd /home/runner/work/newf276/junk/pull
        wget -O epg_ripper_CA1.xml https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz
        gunzip epg_ripper_CA1.xml.gz
        
