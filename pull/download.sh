        sudo apt update
        sudo apt -y install xmltv retry
        go install github.com/aquilax/m3u-combine@latest
        cd /home/runner/work/newf276/junk/pull
        wget -O pluto.xml https://i.mjh.nz/PlutoTV/all.xml
        wget -O roku.xml https://i.mjh.nz/Roku/epg.xml
        wget -O epg_ripper_CA1.xml https://epgshare01.online/epgshare01/epg_ripper_CA1.xml.gz
        gunzip epg_ripper_CA1.xml.gz
        
